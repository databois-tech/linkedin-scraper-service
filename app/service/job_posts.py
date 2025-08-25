from ..util.random_session_picker import fetch_random_session
from ..util.data_cleaner import data_filler, transform_urn
from ..util.random_x_li_track import get_random_x_li_track
import concurrent.futures
import json



def geotag_location(session, csrf):

    url = "https://www.linkedin.com/voyager/api/graphql?variables=(keywords:kolkata,query:(typeaheadFilterQuery:(geoSearchTypes:List(POSTCODE_1,POSTCODE_2,POPULATED_PLACE,ADMIN_DIVISION_1,ADMIN_DIVISION_2,COUNTRY_REGION,MARKET_AREA,COUNTRY_CLUSTER)),typeaheadUseCase:JOBS),type:GEO)&queryId=voyagerSearchDashReusableTypeahead.4c7caa85341b17b470153ad3d1a29caf"

    payload = {}
    headers = {
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Csrf-Token': csrf.replace('"', ''),
        'X-Li-Track': get_random_x_li_track(),
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Lang': 'en_US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'X-Li-Pem-Metadata': 'Voyager - Search Single Typeahead=jobs-geo',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
    }

    response = session.get(url, headers=headers, data=payload)
    json_response = json.loads(response.text)
    elements = json_response.get("data", "").get("data", "").get("searchDashReusableTypeaheadByType", "").get("elements", "")
    if elements and len(elements) > 0:
        tracking_urn = elements[0].get("trackingUrn", "")
        return tracking_urn.split("geo:")[1]

def fetch_job_ids(session, csrf, location_id):

    print("here is location id", location_id)
    print("here is csrf", csrf)
    print("here is session", session)
    # url = f"https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-220&count=25&q=jobSearch&query=(origin:JOB_SEARCH_PAGE_SEARCH_BUTTON,keywords:data%20engineer,locationUnion:(geoId:{location_id}),spellCorrectionEnabled:true)&start=0"
    # url = "https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-220&count=25&q=jobSearch&query=(origin:JOB_SEARCH_PAGE_SEARCH_BUTTON,keywords:data%20engineer,locationUnion:(geoId:111795395),spellCorrectionEnabled:true)&start=0"
    url = "https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-220&count=25&q=jobSearch&query=(origin:SWITCH_SEARCH_VERTICAL,keywords:data%20engineer,spellCorrectionEnabled:true)&start=0"
    
    payload = {}
    headers = {
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Csrf-Token': csrf.replace('"', ''),
        'X-Li-Track': get_random_x_li_track(),
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Lang': 'en_US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'X-Li-Pem-Metadata': 'Voyager - Careers - Jobs Search=jobs-search-results,Voyager - Careers - Critical - careers-api=jobs-search-results',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
        }


    response = session.get(url, headers=headers, data=payload)
    print("here is the response", response)
    print("here",response.text)
    json_response = json.loads(response.text)
    job_posting_cards = json_response.get("data", "").get("metadata", "").get("jobCardPrefetchQueries", "")[0].get("prefetchJobPostingCardUrns", "")

    return job_posting_cards

def fetch_company_info(session, csrf, job_urn):
    job_urn = transform_urn(job_urn)

    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(cardSectionTypes:List(COMPANY_CARD),jobPostingUrn:{job_urn},includeSecondaryActionsV2:true)&queryId=voyagerJobsDashJobPostingDetailSections.5b0469809f45002e8d68c712fd6e6285"

    payload = {}
    headers = {
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Csrf-Token': csrf.replace('"', ''),
        'X-Li-Track': get_random_x_li_track(),
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Lang': 'en_US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'X-Li-Pem-Metadata': 'Voyager - Organization - LCP_Member=job-about-company-card',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
    }

    response = session.get(url, headers=headers, data=payload)
    json_response = json.loads(response.text)
    included_section = json_response.get("included", "")
    company_info = {}
    print(included_section)
    for included_section_data in included_section:
        if "followerCount" in included_section_data:
            company_info["company_follower_count"] = included_section_data.get("followerCount", "")
        elif "entityUrn" in included_section_data and "industry" in included_section_data["entityUrn"]:
            company_info["company_business_domain"] = included_section_data.get("name", "")
        elif "description" in included_section_data:
            company_info["company_description"] = included_section_data.get("description", "")
            company_info["company_employee_strength"] = f"{included_section_data.get('employeeCountRange', {}).get('start', '')} - {included_section_data.get('employeeCountRange', {}).get('end', '')} employees"

            company_info["company_name"] = included_section_data.get("name", "")

    return company_info


# urn:li:fsd_jobPostingCard:(4279617116,JOB_DETAILS)
# urn%3Ali%3Afsd_jobPosting%3A4279617116

def find_job_detailed_info(session, csrf, job_urn):

    job_urn = transform_urn(job_urn)

    print("here is the job urn", job_urn)

    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(jobPostingUrn:{job_urn})&queryId=voyagerJobsDashJobPostings.891aed7916d7453a37e4bbf5f1f60de4"

    payload = {}
    headers = {
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138"',
        'Csrf-Token': csrf.replace('"', ''),
        'X-Li-Track': get_random_x_li_track(),
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Lang': 'en_US',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'X-Li-Pem-Metadata': 'Voyager - Careers - Job Details=job-posting',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
    }

    response = session.get(url, headers=headers, data=payload)
    json_response = json.loads(response.text)
    included_section = json_response.get("included", "")
    for included_section_iterator in included_section:
        if "description" in included_section_iterator:
            job_description = included_section_iterator.get("description", "").get("text", "")
            return job_description




def fetch_data_updated(session, csrf):
    # session.cookies.set("li_at", "AQEDAVJmCCcDOSnwAAABks9c0mkAAAGXkw_gBlYAuu3iAG0_tHtcXO0KkUVrSrnEibv50intDIiJckzoGcOBUS4O7UR4amVs5tQrEy3Y6MWSbR7eR0sRnMirahPZvGLzfHOb-m71-x3AeGWo7jpqlcx9")
    url = "(start:0,origin:SWITCH_SEARCH_VERTICAL,query:(keywords:air%20india,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(CONTENT))),includeFiltersInResponse:false),count:3)&queryId=voyagerSearchDashClusters.5ba32757c00b31aea747c8bebb92855c"
    url = "https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(start:0,origin:GLOBAL_SEARCH_HEADER,query:(keywords:air%20india,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(ALL))),includeFiltersInResponse:false),count:3)&queryId=voyagerSearchDashClusters.5ba32757c00b31aea747c8bebb92855c"
    url = "https://www.linkedin.com/voyager/api/graphql?variables=(start:0,origin:SWITCH_SEARCH_VERTICAL,query:(keywords:air%20india,flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(CONTENT))),includeFiltersInResponse:false),count:50)&queryId=voyagerSearchDashClusters.5ba32757c00b31aea747c8bebb92855c"
    payload = {}
    headers = {
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'X-Li-Lang': 'en_US',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'Csrf-Token': csrf.replace('"', ''),
        'X-Li-Track': get_random_x_li_track(),
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Pem-Metadata': 'Voyager - Search Results Page=search-results',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.linkedin.com/feed/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i'
    }

    response = session.get(url, headers=headers)

    # Process the response
    # print(response.text)
    scraper_result = data_filler(response_text=response.text)
    
    # Return the result (an array)
    return scraper_result



def fetch_data(start_index, search_query, csrf, session):
    # url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{start_index},origin:SWITCH_SEARCH_VERTICAL,query:(keywords:{search_query},flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(CONTENT))),includeFiltersInResponse:false),count:3)&queryId=voyagerSearchDashClusters.8832876bc08b96972d2c68331a27ba76"
    print("HERE2", search_query)
    url = f"https://www.linkedin.com/voyager/api/graphql?variables=(start:{start_index},origin:SWITCH_SEARCH_VERTICAL,query:(keywords:{search_query},flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:resultType,value:List(CONTENT))),includeFiltersInResponse:false),count:3)&queryId=voyagerSearchDashClusters.8832876bc08b96972d2c68331a27ba76"
    headers = {
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7,bn;q=0.6',
        'csrf-token': csrf.replace('"', ''),
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Host': 'www.linkedin.com',
        'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'X-Li-Lang': 'en_US',
        'Sec-Ch-Ua-Mobile': '?0',
        'Accept': 'application/vnd.linkedin.normalized+json+2.1',
        'X-Li-Track': get_random_x_li_track(),
        'X-Restli-Protocol-Version': '2.0.0',
        'X-Li-Pem-Metadata': 'Voyager - Content SRP=search-results',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
    }
    
    # Send the request
    response = session.get(url, headers=headers)
    
    # Process the response
    print(response.text)
    scraper_result = data_filler(response_text=response.text)
    
    # Return the result (an array)
    return scraper_result


# Function to run multithreading for all start indices
def fetch_all_data_multithreaded(search_query, csrf, session):
    aggregrated_data = []
    max_index = 500  # Max index for the loop
    step_size = 30  # You can modify this based on how many results you fetch per request

    # Create a list of start indices
    start_indices = list(range(0, max_index + 1, step_size))

    # Use ThreadPoolExecutor to run requests in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit all tasks to the executor
        future_to_index = {
            executor.submit(fetch_data, start_index, search_query, csrf, session): start_index
            for start_index in start_indices
        }
        
        # Collect results as they are completed
        for future in concurrent.futures.as_completed(future_to_index):
            start_index = future_to_index[future]
            try:
                result_array = future.result()  # This returns an array

                # Iterate through the array and append each object to aggregrated_data
                for result in result_array:
                    aggregrated_data.append(result)
            except Exception as exc:
                print(f"Error fetching data for start_index {start_index}: {exc}")
    
    # Sort the aggregated data by the sum of num_likes, num_comments, and num_shares
    sorted_data = sorted(
        aggregrated_data, 
        key=lambda x: x.get('num_likes', 0) + x.get('num_comments', 0) + x.get('num_shares', 0), 
        reverse=True
    )
    
    return sorted_data



def driver_function(data):
    search_query = data.query_string
    # cookie = cookie
    # print(cookie)
    # csrf = data.csrf
    search_query = search_query.replace(" ", "%20")
    print("HERE1", search_query)
    session, csrf = fetch_random_session()
    geotag_id = geotag_location(session, csrf)
    job_posting_cards = fetch_job_ids(session, csrf, geotag_id)
    result = []
    for job_posting_card in job_posting_cards[0:1]:
        job_description = find_job_detailed_info(session, csrf, job_posting_card)
        company_description = fetch_company_info(session, csrf, job_posting_card)
        result.append({
            "company_info": company_description,
            "job_info": job_description
        })

    return {"data": result}

