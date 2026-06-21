# AI Study Assistant CLI

## Overview

AI Study Assistant CLI is a command-line application built using the Gemini API. The user enters any topic, and the assistant generates a structured study plan with subtopics arranged from beginner to advanced level. After generating the study plan, the assistant supports follow-up questions in a conversational format while maintaining context throughout the session. The application also tracks the number of questions asked and provides a session summary when the user exits.

## Features

* Generate structured study plans for any topic
* Follow-up question support
* Context-aware conversation
* Session memory
* Question counter
* Exit command with session summary
* Gemini API integration
* Prompt-engineered responses

---

## Prompt Engineering Write-Up

### 1. What role did you assign in your system prompt, and why did you choose that framing?

I assigned the role of **Expert Study Mentor**. I chose this role because the goal of the application is to help users learn topics in a structured and educational manner. By defining a specific role, the model consistently generates responses that focus on teaching, explanation, and logical progression rather than giving random or overly broad information.

### 2. What format did you specify for the study plan output, and how did you enforce it in the prompt?

I specified a numbered study-plan format containing subtopics and one-line descriptions. The prompt explicitly instructed the model to arrange topics from beginner to advanced level, limit the number of subtopics, and provide concise descriptions. I also included formatting requirements such as using numbered lists only and keeping explanations short to ensure consistency across different topics.

### 3. What happens if you remove the system prompt entirely?

When the system prompt is removed, the responses become less structured and less consistent. The model may generate different formats for different topics and may include unnecessary explanations, making the study plans harder to follow. The system prompt helps enforce a predictable structure and improves the overall quality of the output.

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

4. Run the application

```bash
python main.py
```

---

## Example Usage

```text
Enter a topic: Python

===== STUDY PLAN =====

1. Networking Fundamentals
2. Operating Systems
3. Cryptography
4. Web Security
5. Incident Response
```

---

## Technologies Used

* Python
* Gemini API
* google-genai SDK
* python-dotenv
* Command Line Interface (CLI)
