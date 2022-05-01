import requests
from moviepy.editor import *
import PySimpleGUI as sg


def download_file(film_id, url, seg):
    url = url.format(seg=seg)
    local_filename = f"{seg}.ts"
    r = requests.get(url, stream=True)
    with open(f"ts_files/{film_id}/{local_filename}", 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def download_full_video(film_id, url, parts, codec=None):
    os.mkdir(f"ts_files/{film_id}")
    for seg in range(parts + 1):
        download_file(film_id, url, seg)
        sg.one_line_progress_meter(film_id, seg, parts, 'Скачивание видеофайлов...')

    cwd = os.getcwd()
    TS_DIR = f"ts_files/{film_id}"
    tss = []
    for ts_file in [f"{i}.ts" for i in range(1, parts + 1)]:
        sg.one_line_progress_meter(film_id, int(ts_file.split(".")[0]), parts, 'Обработка видеофайлов...')
        clip = VideoFileClip(f'{cwd}/{TS_DIR}/{ts_file}')
        tss.append(clip)
    final_clip = concatenate_videoclips(tss)
    final_clip.write_videofile(f"res/{film_id}.mp4",
                               codec=codec)
