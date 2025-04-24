[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# CompTIA Security+ Question Generator
A simple Python script that generates multiple-choice questions at CompTIA Security+ level (SY0-701).
I felt like rapid fire questions were a good way to prepare.
They are AI-generated, so be aware it's not official and may contain errors.
## ** Features
- Generates exam-style Security+ questions
- Lets you choose an answer and tells you if it was correct
- Keeps the question and options visible after answering
- One question per run, clean and simple
## ** How to use
1. Clone this repository:
git clone https://github.com/Martinsecc/comptia-question-gen.git
cd comptia-question-gen
2. Create a `.env` file in the root folder:
OPENAI_API_KEY=sk-...
3. Set up a virtual environment:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
4. Run the quiz:
python main.py
---
Made for personal study use. Contributions welcome.
If you fail the test because of this generator, you're not eligible for compensation.
