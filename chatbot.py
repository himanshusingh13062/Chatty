import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
HEADERS = {"Content-Type": "application/json"}

def get_chatty_response(prompt, history):
    system_prompt = (
        "You are Chatty, a helpful, friendly AI assistant created by Himanshu Singh. "
        "You answer politely, give helpful information, and when asked 'who are you?', reply: "
        "'I am Chatty, your personal AI assistant, created by Himanshu Singh.'"
    )

    contents = [{"role": "user", "parts": [{"text": system_prompt}]}]

    for i, msg in enumerate(history):
        role = "user" if i % 2 == 0 else "model"
        contents.append({"role": role, "parts": [{"text": msg}]})

    contents.append({"role": "user", "parts": [{"text": prompt}]})

    data = {"contents": contents}
    
    for _ in range(2):
        try:
            response = requests.post(API_URL, headers=HEADERS, data=json.dumps(data))
            
            if response.status_code == 200:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            elif response.status_code == 503:
                time.sleep(2)  # Wait a bit and try again
                continue
            else:
                return f"Error: {response.status_code} - {response.text}"
        except:
            time.sleep(1)
    
    return "Sorry, I'm having trouble connecting right now. Please try again."
