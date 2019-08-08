from os import rename
import youtube_dl

def download(youtube_url):
    # 定义某些下载参数
    ydl_opts = {
        # outtmpl 格式化下载后的文件名，避免默认文件名太长无法保存
        'outtmpl': 'E:\\视频\youtube\\temp\\%(title)s.%(ext)s',
        # 'outtmpl': 'E:\\视频\youtube\\學生Why\\學習力 - 提升學習成效\\%(title)s.%(ext)s',
        # 'outtmpl': 'E:\\视频\youtube\\肯德拉语言学校\\常用英语口语训练\\%(title)s.%(ext)s',
        'proxy': '127.0.0.1:1080',
        # 'format' : '137+140',
        'format' : 'best',
        # 'playliststart' : 14,
        # 'playlistend' : 20

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     # extract_info 提取信息
    #     result = ydl.extract_info(youtube_url, download=False)
    #     print(result)

if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=PiGY8qyXf5Q')