from gtts import gTTS

def text_to_speech(text: str, output_file="story.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
