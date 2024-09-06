import requests, re, json, urllib.parse
from ..util.linkedin_username_extractor import extract_linkedin_username

# Helper function to convert timeline to minutes
def get_minutes_from_timeline(timeline):
    value, unit = timeline.split()[:2]  # Get the number and the time unit
    num = int(value)

    if unit in ['second', 'seconds']:
        return num  # 1 second = 1 second
    elif unit in ['minute', 'minutes']:
        return num * 60  # 1 minute = 60 seconds
    elif unit in ['hour', 'hours']:
        return num * 60 * 60  # 1 hour = 3600 seconds
    elif unit in ['day', 'days']:
        return num * 60 * 60 * 24  # 1 day = 86400 seconds
    elif unit in ['month', 'months']:
        return num * 60 * 60 * 24 * 30  # 1 month = 30 days
    elif unit in ['year', 'years']:
        return num * 60 * 60 * 24 * 365  # 1 year = 365 days
    else:
        return 0  # Fallback if unit is unrecognized
    
def clean_reaction_data(reaction_data):
    cleaned_data = []

    for reaction in reaction_data:
        cleaned_reaction = {k: v for k, v in reaction.items() if k not in ["$recipeTypes", "$type"]}
        cleaned_data.append(cleaned_reaction)

    return cleaned_data

def fetch_profile_urn_number(profile_url, cookies, csrf):
    # profile_url = extract_linkedin_username(profile_url)
    
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(vanityName:{profile_url})&queryId=voyagerIdentityDashProfiles.4d9e161cdf3cf64b1c9a7a7c1fc94cff"
    
    payload = {}
    headers = {
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
        'cookie': cookies,
        'csrf-token': csrf.replace('"', ''),
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',  
    }
    
    # print(cookies)

    response = requests.request("GET", url, headers=headers, data=payload)
    # print("HEEEREEE1",response.text)
    jsonResponse = json.loads(response.text)
    # print("HEEEREEE",jsonResponse)
    return jsonResponse["data"]["data"]["identityDashProfilesByMemberIdentity"]["*elements"][0]


def parse_interactive_data(json_data, json_response):
    original_post_image_url = ""
    progressive_stream_url = ""
    source_profile_image_url = ""
    if "content" in json_data.keys() and json_data["content"]:
        if json_data["content"]["imageComponent"]:
            vector_image = json_data["content"]["imageComponent"]["images"][0]["attributes"][0]["detailData"]["vectorImage"]
            post_root_image_url = vector_image["rootUrl"]
            post_artifact_image_url = vector_image["artifacts"][0]["fileIdentifyingUrlPathSegment"]
            original_post_image_url = post_root_image_url + post_artifact_image_url
        elif json_data["content"]["linkedInVideoComponent"]:
            video_meta_data = json_data["content"]["linkedInVideoComponent"]["*videoPlayMetadata"]
            for json_data in json_response:
                if "progressiveStreams" in json_data.keys() and json_data["media"] == video_meta_data:
                    progressive_stream_url = json_data["progressiveStreams"][0]["streamingLocations"][0]["url"]
                    break


    if "actor" in json_data.keys() and json_data["actor"]:
        vector_image = json_data["actor"]["image"]["attributes"][0]["detailData"]["nonEntityProfilePicture"]["vectorImage"]
        profile_root_image_url = vector_image["rootUrl"]
        profile_artifact_image_url = vector_image["artifacts"][0]["fileIdentifyingUrlPathSegment"]
        source_profile_image_url = profile_root_image_url + profile_artifact_image_url

    return original_post_image_url, progressive_stream_url, source_profile_image_url

def parse_source_account_info(json_data):
    if "actor" in json_data.keys():
        description_text = json_data["actor"]["description"]["accessibilityText"]
        source_account_name = json_data["actor"]["name"]["text"]
        post_upload_timeline = json_data["actor"]["subDescription"]["accessibilityText"]
        source_account_url = json_data["actor"]["navigationContext"]["actionTarget"]
        
    return description_text, source_account_name, post_upload_timeline, source_account_url

# def parse_post_share_url(json_data):
#     share_url = json_data["socialContent"]["shareUrl"]
#     return 


def parse_pagination_token(json_response):
    metadata = json_response["data"]["data"]["feedDashProfileUpdatesByMemberShareFeed"]["metadata"]

    return metadata.get("paginationToken", "")



def fetch_posts(profile_urn, cookie, csrf, start_page, pagination_token):
    
    profile_urn = urllib.parse.quote(profile_urn, safe='')

    if start_page == "0":
        # print("came here")
        url = f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(count:20,start:0,profileUrn:{profile_urn})&queryId=voyagerFeedDashProfileUpdates.41245a475ad32dd4c26d1e5660ea1394"
    else:
        url = f"https://www.linkedin.com/voyager/api/graphql?variables=(count:20,start:{start_page},profileUrn:{profile_urn},paginationToken:{pagination_token})&queryId=voyagerFeedDashProfileUpdates.41245a475ad32dd4c26d1e5660ea1394"
   
    payload = {}
    headers = {
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
        'cookie': cookie,
        'csrf-token': csrf.replace('"', ''),
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    json_response = json.loads(response.text)["included"]
    pagination_token = parse_pagination_token(json.loads(response.text))
    reaction_data = []
    aggregated_reaction_data = [{
        "pagination_token": pagination_token
    }
    ]
    # print(json_response)
    for data in json_response:
        if "numLikes" in data.keys():
            reaction_data.append(data)
        # print("REEAAACC", reaction_data)
    # print(len(reaction_data))
    for reaction_count in reaction_data:
        aggregated_reaction_data.append({
            "num_likes" : reaction_count["numLikes"],
            "urn": reaction_count["urn"],
            "predash_entity_urn" : reaction_count["preDashEntityUrn"].split("urn:li:fs_socialActivityCounts:")[1],
            "num_comments": reaction_count["numComments"],
            "like_types": clean_reaction_data(reaction_count["reactionTypeCounts"]),
            "num_shares": reaction_count["numShares"]
        })
    # print(aggregated_reaction_data)
    for individual_reaction_data in aggregated_reaction_data[1:]:
        # print("INDIVIDUAL",individual_reaction_data)
        
        for data in json_response:
            # print(data)
            if "metadata" in data.keys() and (data["metadata"]["backendUrn"] == individual_reaction_data["urn"] or data["metadata"]["shareUrn"] == individual_reaction_data["predash_entity_urn"] ):
                print(individual_reaction_data["predash_entity_urn"])
                commentary_text = data["commentary"]["text"]["text"]
                individual_reaction_data["author_text"] = commentary_text
                original_post_image_url, progressive_stream_url, source_profile_image_url = parse_interactive_data(data, json_response)
                description_text, source_account_name, post_upload_timeline, source_account_url = parse_source_account_info(data)
                individual_reaction_data["description_text"] = description_text
                individual_reaction_data["source_account_name"] = source_account_name
                individual_reaction_data["post_upload_timeline"] = post_upload_timeline
                individual_reaction_data["source_account_url"] = source_account_url
                individual_reaction_data["original_post_image_url"] = original_post_image_url
                individual_reaction_data["progressive_stream_url"] = progressive_stream_url
                individual_reaction_data["source_profile_image_url"] = source_profile_image_url
                individual_reaction_data["post_share_url"] = data["socialContent"]["shareUrl"]
    
    # Assuming aggregated_reaction_data is your list of dictionaries
    filtered_data = [item for item in aggregated_reaction_data if 'author_text' in item]
    # Now return the filtered data
    print(filtered_data)
    return filtered_data




def driver_function(data, cookie):
    linkedinUrl = data.linkedinUrl
    cookie = cookie
    csrf = data.csrf


    
    profileUrn = fetch_profile_urn_number(linkedinUrl, f'''{cookie}''', csrf)
    return fetch_posts(profileUrn, f'''{cookie}''', csrf, '0' , "")




