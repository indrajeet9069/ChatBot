import time, pafy, vlc, youtube_dl

url = "https://www.youtube.com/watch?v=qcCH6JpcK5w"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance('--no-video ')
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
duration = player.get_length() / 1000
player.play()
time.sleep(duration)