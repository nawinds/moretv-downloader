from download_video import download_full_video

FILM_NAME = "Кухня"
SEASONS = {
    1:  # Season 1
        {
            1:  # Episode 1
                {
                    "url": "https://ts-video.url/h"
                           "ls-seg-{seg}-f1-v1-a1.ts",  # <-- change with your URL. Remember to replace
                                                        # segment number with {seg}
                    "hours": 0,  # <-- set the duration of the episode
                    "minutes": 0,
                    "seconds": 0
                }
        }
}

BLACK_LIST = [(1, 2)]  # Episode 2 of season 1 shouldn't be downloaded

for season_n, season in SEASONS.items():
    for episode_n, episode in season.items():
        if (season_n, episode_n) not in BLACK_LIST:
            print(f"{season_n} сезон, {episode_n} серия")
            h, m, s = episode["hours"], episode["minutes"], episode["seconds"]
            parts = (h * 3600 + m * 60 + s)
            parts = parts // 10 if parts % 10 == 0 else parts // 10 + 1
            download_full_video(f"{FILM_NAME}. {season_n} сезон, {episode_n} серия",
                                episode["url"], parts, "h264_nvenc")
