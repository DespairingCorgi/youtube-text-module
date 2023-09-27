import requests
import os
import json

API_KEY = '<YOURAPIKEY HERE>'
API_COMMENTTHREAD_REQ = 'https://www.googleapis.com/youtube/v3/commentThreads'
VIDEOID = '_XTGPe0Ui_g'

comment_params = {
    'key':API_KEY,
    'videoId' : VIDEOID,
    'part' : 'snippet,replies',
    'maxResults' : '100', 
}

def get_video_data(vid):
    
    comment_params['key'] = API_KEY
    comment_params['videoId'] = vid
    
    while True:
        res = requests.get(API_COMMENTTHREAD_REQ, params=comment_params)
        if res.status_code != 200:
            del comment_params["pageToken"]
            break
        data = json.loads(res.text)
        print(data.keys())
        if "nextPageToken" in data.keys():
            comment_params["pageToken"] = data["nextPageToken"]
        else:
            del comment_params["pageToken"]
            break
        
        texts = []
        
        comment_id = 0
        for i in data['items']:
            comment = {
                "vid": vid,
                "id": f"{comment_id}",
                "is_reply":0,
                "text": i['snippet']["topLevelComment"]["snippet"]["textOriginal"]
            }
            texts.append(comment)
            if i["snippet"]["totalReplyCount"]:
                reply_id = 0
                if 'replies' in i.keys():
                    for j in i['replies']["comments"]:
                        reply = {
                            "vid": vid,
                            "id":f"{comment_id}_{reply_id}",
                            "is_reply":1,
                            "text": j['snippet']['textOriginal']
                        }
                        texts.append(reply)
                    


# url = 'https://www.youtube.com/watch?v=AXSBlElPUpQ'
# vid = url.split('=')[-1]

# with open('textfile.txt') as f:
#     lst = f.read().split("\n")
    
# for url in lst:
#     vid = url.split('=')[-1]
#     get_video_data(vid)
