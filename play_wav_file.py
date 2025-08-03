import subprocess

def play_audio(audio):
    print("File opening", audio)
    subprocess.run(["ffplay", "-nodisp", "-autoexit", audio], 
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    