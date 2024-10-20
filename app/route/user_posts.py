from fastapi import APIRouter, Query
from pydantic import BaseModel
from ..service import user_posts, login_module, popular_posts

class Profile_url_data(BaseModel):
    linkedin_url: str
    # csrf: str

class Search_query(BaseModel):
    query_string: str

class Linkedin_profile_creds(BaseModel):
    email_id: str
    password: str

router = APIRouter(
    prefix= "/scraper-api/v1",
    tags = ["LinkedinDataFetch"],
    responses= {404 : {"description" : "Path Not found"}},
)


@router.post("/fetch-posts")
def fetch_top_activities(data: Profile_url_data):
    result = user_posts.driver_function(data)
    return result

@router.post("/fetch-popular-posts")
def fetch_popular_posts(data: Search_query):
    result = popular_posts.driver_function(data)
    return result


@router.post("/login-automate-internal")
def perform_automated_login(data: Linkedin_profile_creds):
    result = login_module.automated_login_driver(data)
    return result