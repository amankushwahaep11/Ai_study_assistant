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
Enter a topic: cybersecurity

===== STUDY PLAN =====

CYBERSECURITY

1.  **Introduction to Cybersecurity Fundamentals**
    Learn the core concepts, importance, and basic terminology of cybersecurity, including the CIA triad.

2.  **Common Cyber Threats and Vulnerabilities**
    Understand prevalent attack vectors such as malware, phishing, social engineering, and common system weaknesses.

3.  **Network Security Principles**
    Explore fundamental network security concepts including firewalls, VPNs, intrusion detection, and secure network protocols.

4.  **Operating System and Application Security**
    Gain knowledge in securing operating systems, managing patches, configuring user access, and understanding secure software development practices.

5.  **Cryptography Basics**
    Study the foundational principles of encryption, hashing, digital signatures, and their application in securing data.

6.  **Identity and Access Management (IAM)**
    Learn about authentication, authorization, multi-factor authentication, and implementing the principle of least privilege.

7.  **Incident Response and Disaster Recovery**
    Understand the phases of responding to security incidents, forensic basics, and planning for business continuity and data recovery.

8.  **Cybersecurity Governance, Risk, and Compliance (GRC)**
    Examine the regulatory landscape, legal frameworks, ethical considerations, and risk management strategies in cybersecurity.

Ask another question (or type exit/quit to exit): How much time will it take to learn it properly?

===== ANSWER =====

Learning cybersecurity properly is an ongoing process rather than a destination with a fixed endpoint, as the field constantly evolves. However, to gain a foundational understanding and become proficient enough for an entry-level professional role, you can generally expect the following:

*   **For foundational knowledge and entry-level competency:** Expect to dedicate at least **6 months to 2 years** of focused study and practical application. This timeframe can vary significantly based on your prior technical background (e.g., existing IT or networking experience), the intensity of your study (hours per week), and the specific learning path you pursue (e.g., certifications, degree programs, self-study).
*   **For specialized roles and advanced proficiency:** This will require continuous learning beyond the initial foundational period, potentially spanning **several years** of dedicated effort, practical experience, and advanced certifications or education.

The concept of "properly" implies not just theoretical knowledge but also practical skills, which take time to develop through labs, projects, and real-world experience.

Ask another question (or type exit/quit to exit): exit

===== SESSION SUMMARY =====
Topic Studied: cybersecurity
Questions Asked: 1
```




