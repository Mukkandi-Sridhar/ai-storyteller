from app.openai_client import get_client

client = get_client()

def generate_story(topic: str) -> str:
    prompt = f"""
Write an engaging educational story about {topic}.
Target beginners.
Use simple language.
Length: 200–300 words.
End with a short summary.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a calm and friendly teacher."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=600
    )

    return response.choices[0].message.content.strip()
