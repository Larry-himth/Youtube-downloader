import pytubefix

try:
    url = input("Enter the YT URL: ")
    yt_object = pytubefix.YouTube(url)
    print("Title: ",yt_object.title)

    format = input("Download the video or audio:\n").lower()
    if format == "video":
        stream = yt_object.streams.filter(progressive=True,file_extension="mp4").all()
        if not stream:
            print("No available streams")
        
        print("Available video qualities:\n")
        for i, streams in enumerate(stream):
            print(f"{i+1}.{streams.resolution}")
        choice = int(input("Enter the quality of your choice:\n"))
        if choice < 1 or choice > len(stream):
            print("Invalid quality, Defaulting to the highest quality")
            selected_stream = stream[-1]
        else:
            selected_stream = stream[choice-1]
            
    elif format == "audio":
        stream = yt_object.streams.filter(only_audio=True).first()
    else:
        print("Invalid format")
        exit()

    file_path = input("Choose file location:\n").strip().strip('"')
    if file_path == "":
        stream.download()
    else:
        stream.download(file_path)

    print("Download Complete!")

except ValueError:
    print("Invalid input!")
except Exception as e:
    print("An error occured: ",e)