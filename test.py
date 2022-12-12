import urllib.request
import re

search_keyword = ["commerce", "chemistry"]


for keyword in search_keyword:
    videos = []
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + 
keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    video_ids = sorted(set(video_ids))

    
    i = 0
    for id in video_ids:
        i+=1
        if i < 6:
            x ="https://www.youtube.com/watch?v=" + id
            videos.append(x)
        else:
            break

    print(f"{keyword}:{videos}")

