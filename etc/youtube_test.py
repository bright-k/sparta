from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
DEVELOPER_KEY = "AIzaSyAmmHbqw6Dz1JH_qNs5IzTLy4gt7O7HAEo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
# build(googleapiclient.discovery) 객체 생성
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
# 검색결과 크롤링
search_response = youtube.search().list(
    q = "bts",
    order = "date",
    part = "snippet",
    maxResults = 50
    ).execute()
videos = []
channels = []
playlists = []
for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        videos.append("%s (%s)" % (search_result["snippet"]["title"],search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
        channels.append("%s (%s)" %(search_result["snippet"]["title"], search_result["id"]["channelID"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
        playlists.append("%s (%s)" %(search_result["snippet"]["title"], search_result["id"]["playlistID"]))

print(videos)