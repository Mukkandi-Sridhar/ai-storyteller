from dotenv import load_dotenv
from app.story_generator import generate_story
from app.tts import text_to_speech

load_dotenv()

if __name__ == "__main__":
    topic = "Bhishma in Mahabharata"

    story = generate_story(topic)
    print("\nGenerated Story:\n")
    print(story)

    text_to_speech(story)
    print("\nAudio saved as story.mp3")
