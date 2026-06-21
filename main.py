from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

topic = input("Enter a topic: ")

SYSTEM_PROMPT = f"""
You are an Expert Study Mentor.

Your job is to help students learn topics in a structured way.

When creating a study plan:

Format:

TOPIC

1. Subtopic Name
   One-line description

2. Subtopic Name
   One-line description

Rules:
- Maximum 8 subtopics.
- Arrange subtopics from beginner to advanced.
- Each description must be one sentence.
- Use numbered lists only.
- Keep explanations concise.
- Do not use emojis.
- Do not use motivational statements.
- Do not generate unrelated topics.

Current topic: {topic}
"""

# Generate Study Plan
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
    {SYSTEM_PROMPT}

    Create a study plan for {topic}
    with maximum 8 subtopics.
    """
)

print("\n===== STUDY PLAN =====\n")
print(response.text)

# Chat History
history = []

question_count = 0

while True:

    user_input = input("\nAsk another question (or type exit/quit to exit): ")

    if user_input.lower() in ["exit", "quit"]:
        break

    question_count += 1

    history.append(f"User: {user_input}")

    prompt = f"""
    {SYSTEM_PROMPT}

    Previous conversation:
    {' '.join(history)}

    Current question:
    {user_input}
    """

    answer = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n===== ANSWER =====\n")
    print(answer.text)

    history.append(f"Assistant: {answer.text}")

print("\n===== SESSION SUMMARY =====")
print("Topic Studied:", topic)
print("Questions Asked:", question_count)