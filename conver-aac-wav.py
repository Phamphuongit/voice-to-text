from pydub import AudioSegment

aac_file_path = "./voice-data/mot-con-vit.aac"
wac_output_path = "./wav-data/mot-con-vit.wav"
# Load AAC file
audio = AudioSegment.from_file(aac_file_path, format="aac")

# Export to WAV
audio.export(wac_output_path, format="wav")

print("✅ Chuyển đổi hoàn tất!")
