from typing import List

from fastapi import FastAPI, Query
from src import HASHTAGS
from src.tweet import Tweets
from starlette_exporter import PrometheusMiddleware, handle_metrics

api = FastAPI()
api.add_middleware(PrometheusMiddleware, app_name="twitter-api")
api.add_route("/metrics", handle_metrics)
tweets = Tweets()


@api.get("/")
async def insert_tweets(htag: List[str] = Query(HASHTAGS)):
    return tweets.insert_tweets(htag)


@api.get("/most-followed-users")
async def most_followed_users():
    return tweets.get_most_followed_users()


@api.get("/total-hashtag-lang")
async def total_hashtag_lang():
    return tweets.get_total_tweets_by_hashtag_lang()