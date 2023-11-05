import argparse
from pathlib import Path
from llama_hub.file.audio import AudioTranscriber

def transcribe_audio_file(mp3_audio_file):
    # Create an instance of AudioTranscriber
    loader = AudioTranscriber(model_version="medium")

    # Load the audio file
    documents = loader.load_data(file=mp3_audio_file)
    
    # Generate the output file path with a .txt extension
    output_file = mp3_audio_file.with_suffix('.txt')

    # Write the transcription to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(documents[0].text)

    print(f"Transcription saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", type=Path, help="Path to the audio file to transcribe")
    args = parser.parse_args()

    # Call the transcribe_audio_file function with the provided audio file path
    transcribe_audio_file(args.audio_file)
