import instaloader
ig = instaloader.Instaloader()
dp = input("Enter Instagram name of the user: ")
ig.download_profile(dp, profile_pic_only=True)
