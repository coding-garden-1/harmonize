
import os
from pydub import AudioSegment

def list_audio_files():
    files = os.listdir()
    audio_files = [f for f in files if f.endswith(".mp3") or f.endswith(".wav")]
    for i, file in enumerate(audio_files):
        print(f"{i+1}. {file}")
    return audio_files

def extract_audio_segment(audio_file, start_min, middle_min, end_min, middle):
    audio = AudioSegment.from_file(audio_file)

    start_ms = start_min * 60 * 1000
    middle_ms = middle_min * 60 * 1000
    end_ms = end_min * 60 * 1000

    start = audio[:start_ms]
    middle = audio[start_ms:start_ms+middle_ms] if middle else None
    end = audio[-end_ms:]

    return start, middle, end

def main():
    print("List of audio files in the directory:")
    audio_files = list_audio_files()

    file1_idx = int(input("Enter the number corresponding to the first audio file: ")) - 1
    file2_idx = int(input("Enter the number corresponding to the second audio file: ")) - 1

    start1_min = int(input("How many minutes at the start of the first file do you want? "))
    middle1_min = int(input("How many minutes in the middle of the first file do you want? "))
    end1_min = int(input("How many minutes at the end of the first file do you want? "))

    start2_min = int(input("How many minutes at the start of the second file do you want? "))
    middle2_min = int(input("How many minutes in the middle of the second file do you want? "))
    end2_min = int(input("How many minutes at the end of the second file do you want? "))

    extract_middle1 = input("Do you want to extract a segment from the middle of the first file? (yes/no) ").lower().startswith('y')
    extract_middle2 = input("Do you want to extract a segment from the middle of the second file? (yes/no) ").lower().startswith('y')

    file1 = audio_files[file1_idx]
    file2 = audio_files[file2_idx]

    start1, middle1, end1 = extract_audio_segment(file1, start1_min, middle1_min, end1_min, extract_middle1)
    start2, middle2, end2 = extract_audio_segment(file2, start2_min, middle2_min, end2_min, extract_middle2)

    output1 = start1 + (middle1 if middle1 is not None else AudioSegment.empty()) + end1
    output2 = start2 + (middle2 if middle2 is not None else AudioSegment.empty()) + end2

    output1.export("output1.mp3", format="mp3")
    output2.export("output2.mp3", format="mp3")

    combined_output = output1 + output2
    combined_output.export("combined_output.mp3", format="mp3")

    print("Extraction and combination completed. Output files saved as output1.mp3, output2.mp3, and combined_output.mp3")

if __name__ == "__main__":
    main()
