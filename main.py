import os
import io
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import pygame
import time
from dotenv import load_dotenv
import sounddevice as sd
import soundfile as sf
import tempfile

load_dotenv()

app = FastAPI()

class Settings(BaseSettings):
    gemini_api_key: str = os.getenv("GEMINI_API_KEY")

def get_settings():
    return Settings()

def speech_to_text():
    fs = 16000  # Sample rate
    seconds = 5  # Duration of recording
    print("Listening with sounddevice...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmpfile:
        sf.write(tmpfile.name, recording, fs)
        tmpfile.flush()
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmpfile.name) as source:
            audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcribed: {text}")
            return text
        except Exception as e:
            print(f"Transcription error: {e}")
            return None

def ask_gemini(prompt, settings: Settings):
    try:
        genai.configure(api_key=settings.gemini_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        answer = response.text.strip()
        print(f"Gemini: {answer}")
        return answer
    except Exception as e:
        print(f"Gemini error: {e}")
        return None

def speak_response(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    # Play audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

@app.post("/api/ask")
def api_ask(settings: Settings = Depends(get_settings)):
    transcript = speech_to_text()
    if not transcript:
        raise HTTPException(status_code=400, detail="Speech transcription failed.")
    answer = ask_gemini(transcript, settings)
    if not answer:
        raise HTTPException(status_code=400, detail="Gemini API call failed.")
    speak_response(answer)
    return JSONResponse({"transcript": transcript, "answer": answer}) 