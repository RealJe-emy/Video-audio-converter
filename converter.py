from pytube import YouTube
import pytube
import os


def main():
    video_url = input('Enter YouTube video URL: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    try:
        name = pytube.extract.video_id(video_url)
        audio_stream = YouTube(video_url).streams.filter(only_audio=True).first()

        if not audio_stream:
            print("No audio stream available for this video.")
            return

        audio_stream.download(filename=name)
        location = path + name + '.mp4'
        renametomp3 = path + name + '.mp3'

        if os.name == 'nt':
            os.system(f'ren {location} {renametomp3}')
        else:
            os.system(f'mv {location} {renametomp3}')

        print(f"Audio downloaded and saved as {renametomp3}")

    except pytube.exceptions.VideoUnavailable:
        print("The video is unavailable. Please check the URL.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()
