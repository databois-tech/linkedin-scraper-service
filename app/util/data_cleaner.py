import json

def parse_pagination_token(json_response):
    metadata = json_response["data"]["data"]["feedDashProfileUpdatesByMemberShareFeed"]["metadata"]

    return metadata.get("paginationToken", "")


def clean_reaction_data(reaction_data):
    cleaned_data = []

    for reaction in reaction_data:
        cleaned_reaction = {k: v for k, v in reaction.items() if k not in ["$recipeTypes", "$type"]}
        cleaned_data.append(cleaned_reaction)

    return cleaned_data

def parse_source_account_info(json_data):
    if "actor" in json_data.keys():
        description_text = json_data["actor"]["description"]["accessibilityText"]
        source_account_name = json_data["actor"]["name"]["text"]
        post_upload_timeline = json_data["actor"]["subDescription"]["accessibilityText"]
        source_account_url = json_data["actor"]["navigationContext"]["actionTarget"]
        
    return description_text, source_account_name, post_upload_timeline, source_account_url


def parse_interactive_data(json_data, json_response):
    original_post_image_url = None
    progressive_stream_url = None
    source_profile_image_url = None

    # Safely parse content-related data
    if json_data.get("content"):
        image_component = json_data["content"].get("imageComponent")
        video_component = json_data["content"].get("linkedInVideoComponent")
        
        # Handle post image
        if image_component:
            try:
                vector_image = image_component["images"][0]["attributes"][0]["detailData"]["vectorImage"]
                post_root_image_url = vector_image["rootUrl"]
                post_artifact_image_url = vector_image["artifacts"][0]["fileIdentifyingUrlPathSegment"]
                original_post_image_url = post_root_image_url + post_artifact_image_url
            except (KeyError, IndexError, TypeError):
                original_post_image_url = None  # Assign None if parsing fails

        # Handle video component
        elif video_component:
            try:
                video_meta_data = video_component["*videoPlayMetadata"]
                for json_data_item in json_response:
                    if json_data_item.get("progressiveStreams") and json_data_item.get("media") == video_meta_data:
                        progressive_stream_url = json_data_item["progressiveStreams"][0]["streamingLocations"][0]["url"]
                        break
            except (KeyError, IndexError, TypeError):
                progressive_stream_url = None  # Assign None if parsing fails

    # Safely parse actor-related data
    if json_data.get("actor"):
        try:
            vector_image = json_data["actor"]["image"]["attributes"][0]["detailData"]["nonEntityProfilePicture"]["vectorImage"]
            profile_root_image_url = vector_image["rootUrl"]
            profile_artifact_image_url = vector_image["artifacts"][0]["fileIdentifyingUrlPathSegment"]
            source_profile_image_url = profile_root_image_url + profile_artifact_image_url
        except (KeyError, IndexError, TypeError):
            source_profile_image_url = None  # Assign None if parsing fails

    # Return the parsed results
    return original_post_image_url, progressive_stream_url, source_profile_image_url



def data_filler(response_text):
    # print(response_text)
    json_response = json.loads(response_text)["included"]
    print(json_response)
    # pagination_token = parse_pagination_token(json.loads(response_text))
    reaction_data = []
    aggregated_reaction_data = [
        # {
        # "pagination_token": "pagination_token"
    # }
    ]
    # print(json_response)
    for data in json_response:
        if "numLikes" in data.keys():
            reaction_data.append(data)
        # print("REEAAACC", reaction_data)
    print(len(reaction_data))
    for reaction_count in reaction_data:
        aggregated_reaction_data.append({
            "total_engagement": reaction_count.get("numLikes", 0) + reaction_count.get("numComments", 0) + reaction_count.get("numShares", 0),
            "num_likes" : reaction_count.get("numLikes", 0),
            "urn": reaction_count["urn"],
            "predash_entity_urn" : reaction_count["preDashEntityUrn"].split("urn:li:fs_socialActivityCounts:")[1],
            "num_comments": reaction_count.get("numComments", 0),
            "like_types": clean_reaction_data(reaction_count["reactionTypeCounts"]),
            "num_shares": reaction_count.get("numShares", 0)
        })
    print(aggregated_reaction_data)
    for individual_reaction_data in aggregated_reaction_data[1:]:
        # print("INDIVIDUAL",individual_reaction_data)
        
        for data in json_response:
            # print(data)
            if "metadata" in data.keys() and (data["metadata"]["backendUrn"] == individual_reaction_data["urn"] or data["metadata"]["shareUrn"] == individual_reaction_data["predash_entity_urn"] ):
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
    return filtered_data