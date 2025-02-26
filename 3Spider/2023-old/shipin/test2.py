import tkinter as tk
from tkinter import ttk
import yt_dlp
import os

# 以下4行代码用来支持ffmpeg的库文件来自于本目录
# 获取当前脚本所在的文件夹路径
# script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = f'E:\\tools\\ffmpeg-7.0-essentials_build'
print(script_dir)

# 构建ffmpeg库文件夹的完整路径
ffmpeg_path = os.path.join(script_dir, "bin")
print(ffmpeg_path)
# 获取当前的环境变量PATH值
path_env = os.environ.get("PATH", "")
print(path_env)
# 将本文件夹的路径添加到PATH环境变量中
os.environ["PATH"] = f"{ffmpeg_path};{path_env}"


def progress_hook(progress):
    """
    下载进度回调函数，用于更新下载进度条
    """
    if progress['status'] == 'downloading':
        total_bytes = progress.get('total_bytes')
        downloaded_bytes = progress.get('downloaded_bytes')
        if total_bytes and downloaded_bytes:
            percent = downloaded_bytes / total_bytes * 100
            # 更新进度条的值
            progress_bar['value'] = percent
            # 更新界面
            window.update()


def download_video():
    """
    视频下载函数，处理视频下载的逻辑
    """
    video_url = url_entry.get()
    download_path = path_entry.get()

    ydl_opts = {
        'default_search': 'ytsearch',
        'outtmpl': download_path + '/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'progress_hooks': [progress_hook],
        'verbose': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        author_name = info_dict.get('uploader', "未知作者")
        video_name = info_dict.get('title', "未知视频")
        ydl.download([video_url])

    url_entry.delete(0, tk.END)
    path_entry.delete(0, tk.END)
    status_label.config(text=f"下载完成！作者：{author_name} 视频名称：{video_name}")


# 创建GUI界面
window = tk.Tk()
window.title("YouTube视频下载工具")

# URL输入框
url_label = tk.Label(window, text="视频URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# 下载路径输入框
path_label = tk.Label(window, text="下载路径:")
path_label.pack()
path_entry = tk.Entry(window, width=50)
path_entry.pack()

# 下载按钮
download_button = tk.Button(window, text="下载视频", command=download_video)
download_button.pack()

# 下载进度条
progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack()

# 状态标签
status_label = tk.Label(window, text="")
status_label.pack()

# 运行GUI
window.mainloop()