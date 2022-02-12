from pytube import YouTube

yt = YouTube(url='https://www.youtube.com/watch?v=V4ScM3uU1Gg&list=PLVVvqw65v_JaSwErTsH4Q03Rqo-PZv1P6&index=26')#,proxies={'http':'192.168.0.109:10809'})
#yt.title
#yt.thumbnail_url
#yt.streams.all()
stream = yt.streams.first()
#stream
stream.download('/root/down')