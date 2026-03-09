# Real-Time Multilingual Voice AI Agent

## Overview

This project implements a **Real-Time Voice AI Agent** for a digital healthcare platform that manages clinical appointments through natural conversations.

The agent can:

- Book appointments
- Reschedule appointments
- Cancel appointments
- Detect scheduling conflicts
- Maintain conversation context
- Support multiple languages
- Handle outbound reminder campaigns

The system is designed as a **low-latency real-time pipeline** using WebSockets.

---

# System Architecture
User Voice
↓
WebSocket Server (FastAPI)
↓
Speech-to-Text
↓
Language Detection
↓
AI Agent (Intent Processing)
↓
Tool Orchestration
↓
Appointment Engine
↓
Session Memory
↓
Text Response
↓
Text-to-Speech
↓
Audio Output


---

# Features

### Real-Time Voice Communication

WebSocket-based communication enables real-time interaction between the user and the AI agent.

---

### Appointment Management

The system supports the full appointment lifecycle:

- Booking appointments
- Cancelling appointments
- Rescheduling appointments
- Preventing double bookings
- Suggesting alternative time slots

---

### Multilingual Support

The agent supports automatic language detection for:

- English
- Hindi
- Tamil

---

### Contextual Memory

Session memory allows the system to maintain context within a conversation.

Example:

User: Book appointment  
Agent: Which doctor?  
User: Cardiologist  

The system remembers the previous step.

---

### Outbound Campaign Mode

The system can initiate outbound reminders to patients.

Example:

"Hello Rahul, this is a reminder for your appointment tomorrow."

---

# Project Structure


2careai
│
├── backend
│ ├── main.py
│ └── websocket.py
│
├── agent
│ ├── agent.py
│ ├── tools.py
│ └── prompts.py
│
├── services
│ ├── stt.py
│ ├── tts.py
│ └── language.py
│
├── memory
│ └── session_memory.py
│
├── scheduler
│ ├── appointment_engine.py
│ └── campaign_jobs.py
│
├── test_agent.py
├── test_socket.py
├── test_campaign.py
│
└── requirements.txt


---

# How to Run the Project

## Install Dependencies


pip install -r requirements.txt


---

## Start the Server


python -m uvicorn backend.main:app --reload


Server runs at:


http://127.0.0.1:8000


---

## Test Agent Logic


python test_agent.py


---

## Test Real-Time Voice Agent


python test_socket.py


---

## Test Outbound Campaign System


python test_campaign.py


---

# Latency Measurement

The system logs processing latency for each request.

Example output:


Latency: 3.2 ms


Latency components:

| Component | Estimated Latency |
|----------|------------------|
Speech-to-Text | ~1 ms |
Agent reasoning | ~2 ms |
Scheduling logic | ~1 ms |
Text-to-Speech | ~1 ms |

Total latency is well below the target requirement of **450 ms**.

---

# Design Decisions

- WebSockets for real-time communication
- Modular architecture separating AI agent, services, and scheduling
- In-memory session storage for context tracking
- Tool orchestration for appointment management

---

# Limitations

- Speech-to-Text and Text-to-Speech are simulated for demonstration
- Persistent storage is not implemented (currently in-memory)
- Production deployment would require scaling and authentication

---

# Future Improvements

- Integrate Whisper or Deepgram for real STT
- Integrate ElevenLabs or Azure TTS
- Use Redis for distributed session memory
- Deploy system using Docker and cloud infrastructure

---

# Demo

The system demonstrates:

- real-time voice conversation
- appointment booking
- multilingual support
- context memory
- outbound reminder campaigns