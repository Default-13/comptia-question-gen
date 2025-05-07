import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_question():
    prompt = """
Generate one CompTIA Security+ SY0-701 level multiple-choice question.
Use this exact format:

Question: <question>
A) <option A>
B) <option B>
C) <option C>
D) <option D>
Answer: <correct letter>
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity exam generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300
    )
    return response.choices[0].message.content

def run_quiz():
    while True:
        question_block = generate_question()
        print("\n" + "-" * 60)
        print(question_block.split("Answer:")[0])
        print("-" * 60)

        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        correct_line = [line for line in question_block.splitlines() if line.startswith("Answer:")]
        correct_answer = correct_line[0].split(":")[1].strip() if correct_line else "?"

        print("\n" + "-" * 60)
        if user_answer == correct_answer:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. The correct answer was {correct_answer}.")
        print("-" * 60 + "\n")

try:
    run_quiz()
except KeyboardInterrupt:
    print("\n\n👋 Session ended. Good luck with your studies!\n")

