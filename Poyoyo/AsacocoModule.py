#ASACOCOMODULE by KaitodotWav
#StealStuffHere and you'll be dead

import praw, random
from datetime import datetime

#Auth
getToken = requests.get("https://public.sn.files.1drv.com/y4mUp_D7Mmsn-5tOf45TSsQIlmp0p31_GRBmwlvVdyax48a2zewBu9S3JEB-WSSZS3uUjrN3sMLcdrYHk6YeIji4bgNyc8D8XrEHuwskxJGtxtm4VR6G8MRatNMfa8_ySMKCfklssv9Lq9Qo1aWNa9SwJdyY8b_0nsUxdcASrU8lAVnTp2-K9OP5ujpTSnibpY6pzvDnxiKeOz574aDrm-_dplTWMvvaIJrPe1atGp-VD8?access_token=EwAIA61DBAAUmcDj0azQ5tf1lkBfAvHLBzXl5ugAAR6r/Os2txq5vkU%2bJKj3OqkTc8V7JHvxmrroIljJBfYLJ5noVE4bYGrSegV1U3kKmgRvndNlMHXx%2btVGU52fyCJOfcmZf5ar0yiqzSxkAMjW2weB6zX46Hklc5M9oUy0uKaGZFXZjwfkzqk5tD4Jj9tri%2bFIPyyNCDl0ZGXMiaL8OTU1zbBc5jQc9N/czsRRQczyPCbNAuQU4dBMRcAUBKpE5k5JEp%2bJjjPz8d0FAcGAHNocMzDVq6hDPxFnJejXPp7sdEGNLUr/XUNy4iNQgA3CZula6qESljly7VrmHVCRk%2bJabvB4T0kt4VnuF4X8dvswyDoz8FWlvYKzdHdn3QcDZgAACFqviq7BVShW2AEkYAiDmwz4DFm2z50TPsUC7uH9gjbT2yRNN9NQ/uQlyOd8jwehinOigxpZtFchnmunV71jt2znukrit7pJataT/ABtni2ZwgTtKicn8Mf8M14YCevHnoP7hTBsnwEiH9GAETZPDRZWoEJKdcSfDTeEpAELdYMalnqIEcb5hZx7N8Lg6qclss/IKQm1%2b0STiSFBr5PAp8Pg1tXlu3iLog%2bOJi6kiOsIfv0KNTi0iD98VLiWduV%2bEWffvIuBoTj3w2bVQPFnhj/rIjIEDHktyOHUDQnVl86issHxvhcpa7NVE4ODpnPdk5JLsbYc0J3goyEQHM1CvToqrbmGVYJfqAFlsPRtC3abho7d56hn77dVyFcQWPW4beyVM4DleBqhp4YNSFpO5nXPFP7ThnyUaNR7hiWuuqfWhRgWVnkj/mT0PXhgE/5Bdw%2bVPSOY0OpPzrzQ702kOfAaofQn58BPvUxSHo9N3WgSCjtq0zIWWCz5gqKwBoNE7Y9YV4dsteb2muWjgT5Vy2tUJntOzFyirWEfvTO5x3lUE4tUHovkfWDpJD4ZUlMbVckG6w7qnzX3uZPt25muLw4QK0KNMx3i%2bMsyiEIozRmDIVVyiHj/4BrOveLSObF9G%2b7gDgI%3d")
Otoken = json.loads(getToken.text)
AsaToken = Otoken["Asacoco"]

reddit = praw.Reddit(client_id = AsaToken["Client_ID"], 
                     client_secret = AsaToken["Client_Secret"], 
                     user_agent = AsaToken["User_Agent"]
                     )

def getContents(posts):
    image_urls = []
    image_titles = []
    image_timestamps = []
    for post in posts:
        image_urls.append(post.url.encode('utf-8'))
        image_titles.append(post.title.encode('utf-8'))
        #image_scores.append(post.score)
        image_timestamps.append(datetime.fromtimestamp(post.created))
        #print(datetime.fromtimestamp(subreddit.created))
        #image_ids.append(post.id)
    return image_urls, image_titles, image_timestamps

def getAll(posts):
    image_urls = []
    image_titles = []
    image_timestamps = []
    image_scores = []
    image_ids = []
    for post in posts:
        image_urls.append(post.url.encode('utf-8'))
        image_titles.append(post.title.encode('utf-8'))
        image_scores.append(post.score)
        image_timestamps.append(datetime.fromtimestamp(post.created))
        image_ids.append(post.id)
    return image_urls, image_titles, image_timestamps, image_scores, image_ids
    

def getMemes(post_range=10):
    image_urls = []
    image_titles = []
    image_timestamps = []
    for subreddit in reddit.subreddit('Hololive').search("memes", syntax="meme", sort="top", time_filter="year"):
        image_urls.append(subreddit.url.encode('utf-8'))
        image_titles.append(subreddit.title.encode('utf-8'))
        #image_scores.append(post.score)
        image_timestamps.append(datetime.fromtimestamp(subreddit.created))
        #print(datetime.fromtimestamp(subreddit.created))
        #image_ids.append(post.id)
    return image_urls, image_titles, image_timestamps

def getLewds(Type="hot"):
    subreddit = reddit.subreddit('Hololewd')
    hot_post = subreddit.hot()
    new_post = subreddit.new()
    if Type == "hot":
        a, b, c = getContents(hot_post)
    elif Type == "new":
        a, b, c = getContents(new_post)
    else:
        a, b, c = getContents(subreddit)
    return a, b ,c

class Asacoco():
    def __init__(self, Subreddit, Sort="top", Time_Filter="week"):
        self.subreddit = Subreddit
        self.sort = Sort
        self.time_filter = Time_Filter
        self.search = None
        self.url = []
        self.title = []
        self.timestamps = []
        self.scores = []
        self.id = []
        self.filter_image = []
        self.cache = ""
        self.old = []
        self.new = []

    def fetch(self, Type="top"):
        if Type == "hot":
            for subreddit in reddit.subreddit(self.subreddit).hot():
                self.url.append(subreddit.url)
                self.title.append(subreddit.title)
                self.scores.append(subreddit.score)
                self.timestamps.append(datetime.fromtimestamp(subreddit.created))
                self.id.append(subreddit.id)
        elif Type == "top":
            for subreddit in reddit.subreddit(self.subreddit).top():
                self.url.append(subreddit.url)
                self.title.append(subreddit.title)
                self.scores.append(subreddit.score)
                self.timestamps.append(datetime.fromtimestamp(subreddit.created))
                self.id.append(subreddit.id)

    def Search(self, syntax, Sort="top"):
        for subreddit in reddit.subreddit('Hololive').search(syntax, sort=Sort, time_filter=self.time_filter):
            self.url.append(subreddit.url)
            self.title.append(subreddit.title)
            self.scores.append(subreddit.score)
            self.timestamps.append(datetime.fromtimestamp(subreddit.created))
            self.id.append(subreddit.id)

    def ImageLink(self):
        images = []
        img_format = [".jpg", ".png"]
        for u in self.url:
            for i in img_format:
                if i in u:
                    images.append(u)
        self.filter_image = images
        return images

    def SetCache(self, directory):
        self.cache = directory
        try:
            open(self.cache)
        except:
            with open(str(self.cache), "w") as F:
                F.write("")
        else:
            self.old = [line.strip() for line in open(self.cache)]

    def SetTimeFilter(self, time_filter):
        self.time_filter = time_filter

    def GetNew(self, List):
        new = []
        old = [line.strip() for line in open(self.cache)]
        self.old = old
        for u in List:
            if u in self.old:
                pass
            else:
                new.append(u)
        self.new = new
        return new

    def WriteCache(self, target):
        try:
            open(self.cache)
        except:
            WF = open(self.cache, "w")
            WF.write(target)
            WF.close()
        else:
            AF = open(self.cache, "a")
            print(target, file=AF)
            AF.close()
    
    def Debug(self):
        print(self.filter_image)
    
if __name__ == "__main__":
    Holo = Asacoco("Hololive")
    Holo.Search("Meme")
    Holo.SetCache(r"Kawaii.txt")
    new = Holo.GetNew(Holo.ImageLink())
    print(new)
    for i in new:
        Holo.WriteCache(i)
    
