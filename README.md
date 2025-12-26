# Voice-First Government Scheme Assistant (Marathi)
[▶️ Demo Video]([https://your-video-link-here](https://iitgnacin-my.sharepoint.com/:v:/g/personal/22110113_iitgn_ac_in/IQBnwGSYSXvQT7SG-sRf4kVsAalOADLLSZwmKsTlOMn4yFg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=astloN))
A **voice-first, agentic AI system** that helps users discover **eligible Indian government schemes** using **speech-only interaction** in **Marathi**.

This project is designed to satisfy all hard requirements of the assignment, including native language support, explicit agent workflow, tool usage, memory, and failure handling.

---

## 🚀 Key Highlights

- 🎤 **Voice-first interaction** (No text input required)
- 🗣️ **Native Marathi support** across the entire pipeline
- 🧠 **Explicit Agent State Machine** (not a chatbot)
- 🛠️ **Multiple tools** (Eligibility Engine + Scheme Retrieval)
- 🧾 **Conversation memory across turns**
- ⚠️ **Robust failure handling** with retries and safe exits

---

## 🧠 Agent Architecture

The system follows an **explicit state-machine based agent lifecycle**:

START
↓
COLLECT_INFO
↓
VALIDATE_INFO
↓
CHECK_ELIGIBILITY
↓
RECOMMEND_SCHEME
↓
END


### Agent Responsibilities
- **Planner**: Decides next state based on missing information
- **Executor**: Collects user data via voice prompts
- **Evaluator**: Confirms user information and eligibility results

---

## 🔊 Voice Pipeline (End-to-End)

| Stage | Technology |
|-----|-----------|
| Speech-to-Text | OpenAI Whisper |
| Normalization | Offline LLM-style Normalizer |
| Reasoning | Agent State Machine |
| Tool Calls | Eligibility Engine + Scheme DB |
| Text-to-Speech | gTTS (Marathi output) |

> Entire pipeline works in **Marathi** (non-English).

---

## 🛠️ Tools Used (Requirement Satisfied)

1. **Eligibility Engine**
   - Applies age, income, caste, gender, BPL, and student rules
2. **Scheme Retrieval System**
   - Loads scheme metadata from `schemes_db.json`

---

## 🧾 Conversation Memory

The agent maintains memory for:
- Age
- Income
- Category (SC/ST/OBC/GEN)
- State
- Gender
- Student status
- BPL status

### Contradiction Handling
- If user changes an answer → re-confirmation is triggered
- Invalid or unclear responses → retries with polite prompts

---

## ⚠️ Failure Handling

- Max retries per question
- Graceful session termination on repeated failures
- Explicit confirmation before eligibility evaluation


---

## Project Structure

.
├── app.py  
├── README.md  
├── requirements.txt  
├── agent/  
│   ├── state_machine.py  
│   ├── memory.py  
│   ├── llm_normalizer.py  
│   └── __init__.py  
├── stt/  
│   ├── whisper_stt.py  
│   └── __init__.py  
├── tts/  
│   ├── gtts_tts.py  
│   └── __init__.py  
├── tools/  
│   ├── eligibility.py  
│   ├── schemes_db.json  
│   └── __init__.py  

---

## How to Run

pip install -r requirements.txt  
python app.py  

---

## Assignment Requirement Coverage

Voice-first interaction: YES  
Native non-English pipeline: YES  
Agentic workflow: YES  
Multiple tools: YES  
Conversation memory: YES  
Failure handling: YES  

This repository contains original code with an explicit agent design and a fully voice-driven Marathi interaction pipeline that satisfies all hard requirements.


