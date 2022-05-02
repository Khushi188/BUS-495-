import instaloader
from instaloader import Profile, Post
instance = instaloader.Instaloader()
instance.download_hashtag(hashtag="nflgame", max_count=10)

