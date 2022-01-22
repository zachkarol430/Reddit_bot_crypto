# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import praw
# See
reddit = praw.Reddit(
    client_id="RGk2fXW6iRH_BRmjrtfk5w",
    client_secret="Sk39BuXFpcetaIOwltN4MMgIwN4jSw",
    user_agent="crpyto by u/ballislifefifa"
)


subreddit= "CryptoMoonshots"
for submission in reddit.subreddit(subreddit).hot(limit=5):
    print(submission.title.lower())
    try:
        print(submission.comments[1].body) #ignore automod
    except:
        print("no comments")


