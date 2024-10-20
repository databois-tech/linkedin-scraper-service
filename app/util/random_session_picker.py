from ..config.mongo_config import connect_db
import requests

MONGO_CLIENT = connect_db()

def fetch_random_session():
    db_instance = MONGO_CLIENT["scraper_service"]
    collection = db_instance["source_cookies"]
    random_doc = collection.aggregate([{'$sample': {'size': 1}}])

    # Convert the cursor into a list and get the first (and only) document
    db_data = list(random_doc)[0] if random_doc else None

    if not db_data:
        raise Exception("No cookie data found in the database")

    # Extract the cookies from the randomly chosen document
    session_cookies = db_data["session_cookies"]
    csrf = db_data["csrf_val"]
    # Create a new requests.Session
    session = requests.Session()

    # Set each cookie in the session
    for cookie in session_cookies:
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])

    return session, csrf