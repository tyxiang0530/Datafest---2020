api_key = 'AIzaSyDEs_5Yl6XjKUUkwPffA8sbKDQUlg4Jguk'
from apiclient.discovery import build
import urllib.request
from urllib.request import Request, urlopen
import json

# build our youtube object
youtube = build('youtube', 'v3', developerKey = api_key)

# Get the number of views for a given video ID
def get_num_views(video_id):
    video_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+ video_id + '&key='+ api_key
    response = urllib.request.urlopen(video_url)
    videos = json.load(response)
    for video in videos['items']:
        return video['statistics']['viewCount']
				
print(get_num_views('cGazy4z3eFo'))

# Get the title of a video given its video ID
def get_vid_title(video_id):
    video_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+ video_id + '&key='+ api_key
    response = urllib.request.urlopen(video_url)
    videos = json.load(response)
    for video in videos['items']:
        return video['snippet']['title']
				
print(get_vid_title('cGazy4z3eFo'))

# Gather the most popular videos in the United States uploaded in a certain date range
def gather_vids_US(category, pub_after, pub_before, language):
    '''
    Since YouTube API limits to georeferencing by a 1000km radius, 
    we must gather videos from three regions of the US and aggregate later
    '''
    # region 1: west
    search_response_left = youtube.search().list(
        type = 'video',
        part = 'snippet',
        location = '41.4381, -113.5477',
        locationRadius = '1000km',
        videoCategoryId = category,
        videoCaption = 'closedCaption', 
        order = 'viewCount', 
        publishedAfter = pub_after + 'T00:00:00Z',
        publishedBefore = pub_before + 'T00:00:00Z',
        relevanceLanguage = language,
        regionCode = 'us',
        maxResults = '15',
        ).execute()
    # region 2: central
    search_response_middle = youtube.search().list(
        type = 'video',
        part = 'snippet',
        location = '41.4381, -97.5837',
        locationRadius = '1000km',
        videoCategoryId = category,
        videoCaption = 'closedCaption', 
        order = 'viewCount', 
        publishedAfter = pub_after + 'T00:00:00Z',
        publishedBefore = pub_before + 'T00:00:00Z',
        relevanceLanguage = language,
        regionCode = 'us',
        maxResults = '15',
        ).execute()
    # region 3: east
    search_response_right = youtube.search().list(
        type = 'video',
        part = 'snippet',
        location = '36.7508, -85.5837',
        locationRadius = '1000km',
        videoCategoryId = category,
        videoCaption = 'closedCaption', 
        order = 'viewCount', 
        publishedAfter = pub_after + 'T00:00:00Z',
        publishedBefore = pub_before + 'T00:00:00Z',
        relevanceLanguage = language,
        regionCode = 'us',
        maxResults = '15',
        ).execute()
    search_response_left = search_response_left['items']
    search_response_middle = search_response_middle['items']
    search_response_right = search_response_right['items']
    arr_left_link = []
    arr_middle_link = []
    arr_right_link = []
    # append the video ids for our videos to separate arrays
    for i in search_response_left:
        print(i['id'].get('videoId'), i['snippet'].get('title'))
        arr_left_link.append(i['id'].get('videoId'))
    for i in search_response_middle:
        print(i['id'].get('videoId'), i['snippet'].get('title'))
        arr_middle_link.append(i['id'].get('videoId'))
    for i in search_response_right:
        print(i['id'].get('videoId'), i['snippet'].get('title'))
        arr_right_link.append(i['id'].get('videoId'))
    # combine the arrays and remove the duplicates
    arr_all_link = arr_left_link + arr_middle_link + arr_right_link
    arr_all_link = list(dict.fromkeys(arr_all_link))
    # sort the array from least viewed to most viewed
    sorted_arr_all_link = []
    while arr_all_link:
        minimum = arr_all_link[0]
        for i in arr_all_link:
            if get_num_views(i) < get_num_views(minimum):
                minimum = i
        sorted_arr_all_link.append(minimum)
        arr_all_link.remove(minimum)
    print(sorted_arr_all_link)
    # retrieve top 15 most viewed videos from the list
    sorted_arr_all_link = sorted_arr_all_link[-15:]
    # add the videos to a csv
    for items in sorted_arr_all_link:
        with open('/home/txaa2019/free_gourds/Youtube Grab/Categories/' + category + '.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['https://www.youtube.com/watch?v=' + items, get_vid_title(item)])
						
gather_vids_US('1','2020-01-01','2020-05-09','en')
