import random, requests
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
from urllib.parse import quote
from .user_posts import driver_function
from ..config.mongo_config import connect_db


async def random_delay(min_time=1, max_time=3):
    await asyncio.sleep(random.uniform(min_time, max_time))

async def move_mouse_randomly(page):
    for _ in range(random.randint(2, 5)):
        x = random.randint(0, 1280)
        y = random.randint(0, 800)
        await page.mouse.move(x, y)
        await random_delay(0.1, 0.5)

async def login_and_get_cookies():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Non-headless mode
        context = await browser.new_context(
            locale='en-US',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            geolocation={'latitude': 40.7128, 'longitude': -74.0060},
            permissions=['geolocation']
        )
        page = await context.new_page()
        
        # Apply stealth
        await stealth_async(page)
        
        # Set viewport and other browser-like behavior
        await page.set_viewport_size({"width": 1280, "height": 800})

        # Go to LinkedIn login
        await page.goto('https://www.linkedin.com/login')

        # Fill username and password
        await page.fill('input#username', 'official.prithidevghosh@gmail.com')
        await random_delay()
        await page.fill('input#password', 'Ghosh@39039820')
        await random_delay()

        # Move mouse randomly before submitting
        await move_mouse_randomly(page)

        # Submit form
        await page.click('button[type="submit"]')
        
        # Wait for navigation and cookies
        await page.wait_for_load_state('networkidle')
        cookies = await page.context.cookies()

        await browser.close()

        return cookies


# Run the script
def automated_login_driver(data):
    linkedin_cookies = asyncio.run(login_and_get_cookies())
    chrome_cookie_value = ""
    csrf_val = ""

    for cookie in linkedin_cookies:
        chrome_cookie_value += f"{cookie['name']}={cookie['value']}; "
        
        if cookie['name'] == "JSESSIONID":
            csrf_val = cookie['value']
    session = requests.Session()
    for cookie in linkedin_cookies:
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
    session_cookies = [{"name": cookie.name, "value": cookie.value, "domain": cookie.domain, "path": cookie.path}
                   for cookie in session.cookies]
    mongo_client = connect_db()
    db_instance = mongo_client["scraper_service"]
    collection = db_instance["source_cookies"]
    db_data = {
        "session_cookies": session_cookies,
        "csrf_val": csrf_val
    }
    collection.insert_one(db_data)
    # return session, csrf_val

# automated_login_driver()
def test_login():
    cookies = [
        {'name': 'li_rm', 'value': 'AQEnWrhgFJGQfQAAAZH-cGhzcroqBXwayymPyNtIGEZQo93W7r1HIJB8O55xlvdjAVtcF87ANBYz-aFs5N2yv5BrRFnkIH8fQpGfJNau_-J5Sz4oM0DzuXwD', 'domain': '.www.linkedin.com', 'path': '/', 'expires': 1758086669.867428, 'httpOnly': True, 'secure': True, 'sameSite': 'None'},
        {'name': 'lang', 'value': 'v=2&lang=en-us', 'domain': '.linkedin.com', 'path': '/', 'expires': -1, 'httpOnly': False, 'secure': True, 'sameSite': 'None'},
        {'name': 'JSESSIONID', 'value': '"ajax:5969587573258662047"', 'domain': '.www.linkedin.com', 'path': '/', 'expires': 1734326669.867881, 'httpOnly': False, 'secure': True, 'sameSite': 'None'},
        {'name': 'bcookie', 'value': '"v=2&4b9dc2b7-9d05-436c-8fe1-2ff37ba8ab5e"', 'domain': '.linkedin.com', 'path': '/', 'expires': 1758086670.867945, 'httpOnly': False, 'secure': True, 'sameSite': 'None'},
        {'name': 'bscookie', 'value': '"v=1&2024091705242564bf525a-aaac-4135-8498-3ab0076f5197AQHvcJSh7t_KIVcs9jProcwKeOqdZUsJ"', 'domain': '.www.linkedin.com', 'path': '/', 'expires': 1758086670.868025, 'httpOnly': True, 'secure': True, 'sameSite': 'None'},
        {'name': 'liap', 'value': 'true', 'domain': '.linkedin.com', 'path': '/', 'expires': 1734326669.867755, 'httpOnly': False, 'secure': True, 'sameSite': 'None'},
        {'name': 'li_at', 'value': 'AQEDAVJmCCcD-euYAAABkf5weS4AAAGSInz9Lk4Ax_upx2ahVF7ovM_BxPRYndwnsZlHswTRQ3V_6E8AQRXlSVOuZoIBm7iDqDJG410F1SdTB0FUMawe70bDSkktT8nKnBLh1AYtRxQN2Ks9E_64tcvb', 'domain': '.www.linkedin.com', 'path': '/', 'expires': 1758086669.867827, 'httpOnly': True, 'secure': True, 'sameSite': 'None'},
        {'name': 'lidc', 'value': '"b=VB71:s=V:r=V:a=V:p=V:g=3640:u=4:x=1:i=1726550670:t=1726635911:v=2:sig=AQFyvZ3cFvixE3JxN1mVz-Lk6uaXpvVG"', 'domain': '.linkedin.com', 'path': '/', 'expires': 1726635912.379133, 'httpOnly': False, 'secure': True, 'sameSite': 'None'}
    ]
    chrome_cookie_value = ""
    csrf_val = ""

    for cookie in cookies:
        chrome_cookie_value += f"{cookie['name']}={cookie['value']}; "
        
        if cookie['name'] == "JSESSIONID":
            csrf_val = cookie['value']
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])

    return session, csrf_val


def test_automated_login(data):
    session, csrf_val = test_login()
    # return driver_function("deepigoyal", session, csrf_val)




