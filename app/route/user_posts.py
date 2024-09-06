from fastapi import APIRouter, Query
from pydantic import BaseModel
from ..service import user_posts

class Profile_url_data(BaseModel):
    linkedinUrl: str
    csrf: str



router = APIRouter(
    prefix= "/scraper-api/v1",
    tags = ["LinkedinDataFetch"],
    responses= {404 : {"description" : "Path Not found"}},
)


@router.post("/fetch-posts")
def fetch_top_activities(data: Profile_url_data, cookie: str = Query(..., description= "cookie")):
    result = user_posts.driver_function(data, cookie)
    return result