import whisper
import re
import yt_dlp
import os

def receive_url():
    #if we check receive url or not 

    url = input("Enter the valut: ").strip()

    if url == "":
        return None

    return url

def validate_url(url_pattern):
    # check the youtube pattern it is correct in input url it will move to next process and validate the value

    pattern =  r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/"

    if re.search(pattern, url_pattern):
        print("Validate the url is correct")
        return True

    print("Invalid pattern found...")
    return False

def extract_video(url):
    #Again get the short form to understand the url pattern and search the pattern if group match create the video id store the data in file

    pattern = r"(?:v=|youtu\.be/|shorts/)([a-zA-Z0-9_-]{11})"

    match = re.search(pattern, url)

    if match:
        video_id = match.group(1)
        print("Video ID: ",video_id)

        return video_id

    print("Unable video cannot be process")
    return None

def video_exists(url):
    #Check if the video file exists or not

    video_id = extract_video(url)

    if video_id is None:
        return False

    print("Video Id is found and created....")
    return True

def download_audio(youtube_url):
    # if download audio file convert into save in os file path and extract video id convert into audio mp3 and if exists it is download else not download

    if not video_exists(youtube_url):
        print("The video cannot found..")
        return None

    output_download = 'downloads'

    os.makedirs(output_download, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_download, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading the youtube url converting.... into mp3")
            ydl.download([youtube_url])
            video_id = video_exists(youtube_url)
            audio_path = os.path.join(output_download, f"{video_id}.mp3")

            if os.path.exists(audio_path):
                print("Audio downloaded successfully....")
                return audio_path

            print("Audio file not yet download..")
            return None

    except Exception as e:
        print(f"An Error occur in the youtube url {e}")
        return None

def transcribe_video_text(audio_path):

    # before transcribe
    if audio_path is None:
        print("No audio file received.")
        return None

    if not os.path.exists(audio_path):
        print("No audio path does not exists")
        return None

    if os.path.getsize(audio_path) == 0:
        print("Audio file is empty")
        return None

    try:
        model = whisper.load_model("base")
    except Exception as e:
        print(f"Unable to load the whisper mode; {e}")
        return None

    # during transcribe

    try:
        print("Transcribing the model")

        res = model.transcribe(audio_path)

    except Exception as e:
        print(f"Unable to transcribing the data {e}")
        return None

# after transcribe

    transcript = res["text"].strip()

    if transcript == " ":
        print("No transcript data can be found in process")
        return None

    print("Transcript data found in Successfully")

    return transcript

def clean_model(transcript):
    # before clean the process

    if transcript is None:
        print("Transcripting not found")
        return None

    if transcript.strip() == " ":
        print("Transcript data is empty")
        return None

    # during clean the process

    # Remove [Music], [Applause], etc.
    transcript = re.sub(r"\[.*?\]", "", transcript)

    # Remove (Music), (Applause), etc.
    transcript = re.sub(r"\(.*?\)", "", transcript)

    # Remove multiple spaces
    transcript = re.sub(r"\s+", " ", transcript)

    # Remove repeated blank lines
    transcript = re.sub(r"\n+", "\n", transcript)

    # Remove leading/trailing spaces
    transcript = transcript.strip()

    # after clean the process

    if transcript == " ":
        print("Transcript became empty after cleaning.")
        return None

    print("Transcript cleaned successfully.")

    return transcript

def save_transcript(transcript, video_id):

    # before save the model
    if transcript is None:
        print("Transcript file is not found")
        return None

    if transcript == " ":
        print("Transcript data is Empty")
        return None

    folder = "transcripts"

    os.makedirs(folder, exist_ok = True)

    file_path = os.path.join(folder, f"{video_id}.txt")

# save the model
    try:
        with open(file_path, "w", encoding = "utf-8") as file:

            file.write(transcript)

    except Exception as e:
        print(f"Saving failed {e}")

        return None

    # verify the model
    
    if not os.path.exists(file_path):
        print("File path is not exists")
        return None

    if os.path.getsize(file_path) == 0:
        print("File size is Zero")
        return None

    print("Transcript file saved successfully")

    return file_path