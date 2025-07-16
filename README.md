# Voice-to-Gemini

**Voice-to-Gemini** is a robust FastAPI-powered backend that enables seamless voice interaction with Google Gemini 2.0 Flash (Generative AI). The system captures spoken input, transcribes it, queries Gemini for intelligent responses, and delivers synthesized speech output—all in real time.

## Overview
Voice-to-Gemini bridges human speech and advanced AI, providing a natural conversational interface. Designed for extensibility, it can serve as the backend for desktop, web, or mobile applications requiring voice-driven AI interaction.

## Key Features
- **Real-Time Speech Recognition:** High-accuracy transcription using `sounddevice`, `soundfile`, and `speech_recognition`.
- **AI-Powered Responses:** Integrates with Google Gemini 2.0 Flash via `google-generativeai` for state-of-the-art conversational intelligence.
- **Text-to-Speech Output:** Converts AI responses to natural-sounding speech using `gTTS` and plays them with `pygame`.
- **RESTful API:** Exposes a `/api/ask` endpoint for easy integration with any client.
- **Configurable & Secure:** API keys and configuration managed via environment variables and Pydantic settings.

## API Endpoint

### `POST /api/ask`
- **Description:** Captures audio from the microphone, transcribes speech, queries Gemini, and returns both the transcript and AI response. The response is also spoken aloud.
- **Response:**
  - `transcript`: The recognized text from the user's speech.
  - `answer`: The AI-generated response from Gemini.

## Technology Stack
- **FastAPI** — High-performance Python web framework
- **sounddevice & soundfile** — Cross-platform audio recording and file handling
- **speech_recognition** — Speech-to-text processing
- **google-generativeai** — Gemini 2.0 Flash integration
- **gTTS** — Text-to-speech synthesis
- **pygame** — Audio playback
- **pydantic-settings, python-dotenv** — Configuration management

## Architecture
```
User Speech → [sounddevice] → Audio File → [speech_recognition] → Transcript → [Gemini AI] → Response → [gTTS/pygame] → Spoken Output
```

## Professional Applications
- Voice-enabled assistants
- Conversational AI interfaces
- Accessibility tools
- Smart device integration

---
For integration, customization, or deployment inquiries, please contact the project maintainer.
