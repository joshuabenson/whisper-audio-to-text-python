import speech_recognition as sr
from pydub import AudioSegment

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
mp3_audio_file = "S01E01 - We Planned This.mp3"  # Change this to your MP3 file's path
wav_audio_file = mp3_audio_file.removesuffix('.mp3')
audio = AudioSegment.from_mp3(mp3_audio_file)
audio.export(wav_audio_file, format="wav")

# Load the audio file and transcribe it
with sr.AudioFile(wav_audio_file) as source:
    audio_data = recognizer.record(source)

try:
    # Use Google Web Speech API to transcribe the audio
    text = recognizer.recognize_google(audio_data)

    # Write the transcribed text to a text file
    with open("transcription.txt", "w") as text_file:
        text_file.write(text)

    print("Transcription saved to transcription.txt")
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
