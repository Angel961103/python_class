import instaloader

# ok hashtags
# headshot
# selfie
loader = instaloader.Instaloader(
    download_videos=False,
    save_metadata=False,
    download_comments=False,
    post_metadata_txt_pattern='')
loader.interactive_login("CharlesInstaResearch")
loader.download_profile('josie_prendergast', fast_update=True)
# loader.download_hashtag('', max_count=100)
