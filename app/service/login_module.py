# import random, requests, time
# import asyncio
# from bs4 import BeautifulSoup
# from playwright.async_api import async_playwright
# from playwright_stealth import stealth_async
# from urllib.parse import quote
# from .user_posts import driver_function
# from ..config.mongo_config import connect_db
# from ..util.logger import logger

# SERVICE_NAME = "*** LINKEDIN AUTOMATED LOGIN SERVIC E ***"

# mongo_client = connect_db()
# DB_INSTANCE = mongo_client["scraper_service"]

# async def random_delay(min_time=1, max_time=3):
#     await asyncio.sleep(random.uniform(min_time, max_time))

# async def move_mouse_randomly(page):
#     logger.info(f"{SERVICE_NAME} moving mouse")
#     for _ in range(random.randint(2, 5)):
#         x = random.randint(0, 1280)
#         y = random.randint(0, 800)
#         await page.mouse.move(x, y)
#         await random_delay(0.1, 0.5)

# async def login_and_get_cookies(username, password):
#     logger.info(f"{SERVICE_NAME} started login service")
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)  # Non-headless mode
#         context = await browser.new_context(
#             locale='en-US',
#             user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#             geolocation={'latitude': 40.7128, 'longitude': -74.0060},
#             permissions=['geolocation']
#         )
#         page = await context.new_page()
        
#         # Apply stealth
#         await stealth_async(page)
        
#         # Set viewport and other browser-like behavior
#         await page.set_viewport_size({"width": 1280, "height": 800})

#         # Go to LinkedIn login
#         await page.goto('https://www.linkedin.com/login')

#         # Fill username and password
#         await page.fill('input#username', username)
#         await random_delay()
#         await page.fill('input#password', password)
#         await random_delay()

#         # Move mouse randomly before submitting
#         await move_mouse_randomly(page)

#         # Submit form
#         await page.click('button[type="submit"]')
        
#         # Wait for navigation and cookies
#         await page.wait_for_load_state('networkidle')
#         cookies = await page.context.cookies()

#         await browser.close()

#         return cookies

# async def run_login_automation(email_id):
#     email_id = email_id.replace("@", "%40")
#     session = requests.Session()

#     url = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"

#     payload = {}
#     headers = {
#         'Host': 'www.linkedin.com',
#         'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
#         'Sec-Ch-Ua-Mobile': '?0',
#         'Sec-Ch-Ua-Platform': '"Linux"',
#         'Accept-Language': 'en-GB,en;q=0.9',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'Sec-Fetch-Site': 'none',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-User': '?1',
#         'Sec-Fetch-Dest': 'document',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Priority': 'u=0, i',
#         'Connection': 'keep-alive',
#     }

#     response = session.get(url, headers=headers, data=payload)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     sid_string_val = soup.find('input', {"name": "sIdString"}).get("value")
#     csrf_token_val = soup.find('input', {"name": "csrfToken"}).get("value").replace(":", "%3A")
#     login_csrf_param_val = soup.find('input', {"name": "loginCsrfParam"}).get("value")


#     url = "https://www.linkedin.com/checkpoint/lg/login-submit"
#     payload = f"csrfToken={csrf_token_val}&session_key=official.prithidevghosh%40gmail.com&ac=0&loginFailureCount=0&sIdString={sid_string_val}&pkSupported=true&parentPageKey=d_checkpoint_lg_consumerLogin&trk=&authUUID=&session_redirect=&loginCsrfParam={login_csrf_param_val}&fp_data=default&_d=d&showGoogleOneTapLogin=true&showAppleLogin=true&showMicrosoftLogin=true&controlId=d_checkpoint_lg_consumerLogin-login_submit_button&session_password=Ghosh%4039039820"
#     # payload = f"csrfToken={csrf_token_val}&session_key={email_id}&ac=0&loginFailureCount=0&sIdString={sid_string_val}&pkSupported=true&parentPageKey=d_checkpoint_lg_consumerLogin&trk=&authUUID=&session_redirect=&loginCsrfParam={login_csrf_param_val}&fp_data=default&_d=d&showGoogleOneTapLogin=true&showAppleLogin=true&showMicrosoftLogin=true&controlId=d_checkpoint_lg_consumerLogin-login_submit_button&session_password=Ghosh%4039039820"
#     headers = {
#         'Host': 'www.linkedin.com',
#         'Content-Length': '488',
#         'Cache-Control': 'max-age=0',
#         'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
#         'Sec-Ch-Ua-Mobile': '?0',
#         'Sec-Ch-Ua-Platform': '"Linux"',
#         'Accept-Language': 'en-GB,en;q=0.9',
#         'Upgrade-Insecure-Requests': '1',
#         'Origin': 'https://www.linkedin.com',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-User': '?1',
#         'Sec-Fetch-Dest': 'document',
#         'Referer': 'https://www.linkedin.com/checkpoint/lg/sign-in-another-account',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Priority': 'u=0, i'
#     }

#     response = session.post(url, headers=headers, data=payload)
#     linkedin_cookies = session.cookies

#     chrome_cookie_value = ""
#     csrf_val = ""
#     print("LI_COO", linkedin_cookies)
#     for cookie in linkedin_cookies:
#         chrome_cookie_value += f"{cookie['name']}={cookie['value']}; "
        
#         if cookie['name'] == "JSESSIONID":
#             csrf_val = cookie['value']
#     session = requests.Session()
#     for cookie in linkedin_cookies:
#         session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
#     session_cookies = [{"name": cookie.name, "value": cookie.value, "domain": cookie.domain, "path": cookie.path}
#                 for cookie in session.cookies]
    
#     collection = DB_INSTANCE["source_cookies"]
#     db_data = {
#         "session_cookies": session_cookies,
#         "csrf_val": csrf_val
#     }
#     collection.insert_one(db_data)


# # Run the script
# def automated_login_driver():
#     creds_collection = DB_INSTANCE["source_creds"]
#     creds_list = list(creds_collection.find({}))
#     for cred_data in creds_list[1:2]:
#         username = cred_data["email"]
#         password = cred_data["password"]
#         logger.info(f"{SERVICE_NAME} ")
#         linkedin_cookies = asyncio.run(run_login_automation(email_id = username))
#         # time.sleep(15)
#     # return session, csrf_val






