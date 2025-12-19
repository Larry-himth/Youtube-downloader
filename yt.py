import pytubefix, webbrowser

running = True
while(running):
    
    try:
        
        url = input("Enter the YT URL: ")
        yt_object = pytubefix.YouTube(url)
        print("Title: ",yt_object.title)
            
        format = input("Download the video or audio:\n").lower()
        if format == "video":
            stream = yt_object.streams.filter(progressive=True,file_extension="mp4")
            if not stream:
                print("No available streams")
            
            print("Available video qualities:\n")
            for i, streams in enumerate(stream):
                print(f"{i+1}. {streams.resolution}")
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
            continue

        file_path = input("Choose file location:\n").strip().strip('"')
        if file_path == "":
            selected_stream.download()
        else:
            selected_stream.download(file_path)

        print("Download Complete!\n")
        
        again = input("Do you want to download another video?\n").lower()
        
        if again == "yes" or again == "y":
            running = True
        else:
            running = False

    except ValueError:
        print("Invalid input!")
        running = True
    except Exception as e:
        print("An error occured: ",e)
        running = True
        
print("Thank you for using our Youtube Downloader!")
git_link = webbrowser.open("https://github.com/Larry-himth/Youtube-downloader")
exit()