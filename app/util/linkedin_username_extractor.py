import re


def extract_linkedin_username(url):
    pattern = r'https://(?:www|[a-z]{2})\.linkedin\.com/in/([^/?&]+)/?'
    
    match = re.search(pattern, url)

    if match:
        return match.group(1)
    else:
        return None