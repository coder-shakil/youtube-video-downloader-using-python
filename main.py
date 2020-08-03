import pytube
#Take video URL from user
video_url = input("Enter Your Link Here :\n")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
#select your path where you want to download this video file
video.download('D:\Demo')

