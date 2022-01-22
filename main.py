

import praw
reddit = praw.Reddit(
    client_id="RGk2fXW6iRH_BRmjrtfk5w",
    client_secret="Sk39BuXFpcetaIOwltN4MMgIwN4jSw",
    user_agent="crpyto by u/ballislifefifa"
)


subreddit= "CryptoMoonshots"
post_number= 10
#i will make dataframe later
titles= []
comments=[]
for submission in reddit.subreddit(subreddit).hot(limit=post_number):
    posts_title= ("title: " + submission.title.lower())
    try:
        comment= (submission.comments[1].body) #ignore automod, just first comment for now. Most comments are troll
    except:
        comment= ("no comments")
    titles.append(posts_title)
    comments.append(comment)

print(titles)
print(comments)






