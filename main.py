import webbrowser
import pyttsx3
import sys
import random
import time
import json
import os

# 🎤 Whisper + audio
import whisper
import sounddevice as sd
import numpy as np

# =========================
# 🧠 AI MODE (STEP 5)
# =========================
AI_ENABLED = False   # keep False = NO billing

# =========================
# 🧠 LONG-TERM MEMORY (JSON)
# =========================
MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "name": None,
        "last_site": None,
        "last_topic": None
    }

def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

memory = load_memory()

# =========================
# 🔊 TEXT TO SPEECH
# =========================
def speak(text):
    try:
        print("Jarvis:", text)

        engine = pyttsx3.init(driverName="sapi5")
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
        time.sleep(0.3)
    except Exception as e:
        print("TTS ERROR:", e)

# =========================
# 🎤 WHISPER
# =========================
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper model loaded.")

def listen(duration=5, samplerate=16000):
    print("🎤 Listening...")
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    sd.stop()

    audio = np.squeeze(recording)
    result = model.transcribe(audio, language="en")
    text = result["text"].strip().lower()

    if len(text) < 2:
        return ""

    print("Heard:", text)
    return text

# =========================
# 🧠 OFFLINE AI FALLBACK
# =========================
def offline_ai_answer(command):
    if "why" in command:
        return "That's a good question. Nature works in fascinating ways."
    if "how" in command:
        return "That depends on many factors, but I can explain the basics."
    if "what is" in command or "who is" in command:
        return "I have a basic idea, but a deeper answer would need internet intelligence."
    return "I don't have a perfect answer yet, but I'm learning every day."

def ai_brain(command):
    return offline_ai_answer(command)

# =========================
# 🧠 RESPONSES
# =========================
greeting_responses = [
    "Hey! I'm here.",
    "Hello! How can I help you?",
    "Hi there. I'm listening."
]

tired_responses = [
    "Sounds like you’re tired. You should rest a bit.",
    "Take a break. I’ll stay here."
]

happy_responses = [
    "That’s great to hear!",
    "Nice! That makes me happy too."
]

angry_responses = [
    "Hey, calm down. I’m here.",
    "Let’s slow things down."
]

joke_responses = [
    "Why don’t programmers like nature? Too many bugs.",
    "I would tell you a Python joke, but it’s still loading."
]

confused_responses = [
    "I didn’t fully understand, but I’m listening."
]

# =========================
# 🧠 COMMAND HANDLER
# =========================
def process_command(command):
    print("You said:", command)

    # 🔐 RECALL NAME (HIGHEST PRIORITY)
    if "what is my name" in command:
        if memory["name"]:
            speak(f"Your name is {memory['name']}.")
        else:
            speak("You haven't told me your name yet.")
        return "continue"

    # 🧠 REMEMBER NAME
    if "my name is" in command:
        name = command.replace("my name is", "").strip().title()
        if name:
            memory["name"] = name
            save_memory()
            speak(f"Got it. I'll remember your name is {name}.")
        return "continue"

    # 🔴 EXIT
    if any(x in command for x in ["exit", "quit", "shutdown"]):
        speak("Shutting down. Goodbye.")
        sys.exit()

    # 💤 SLEEP
    if "sleep" in command:
        speak("Okay. Going to sleep.")
        return "sleep"

    # 🌐 OPEN WEBSITES
    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://google.com")
        memory["last_site"] = "google"
        save_memory()
        return "continue"

    if "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
        memory["last_site"] = "youtube"
        save_memory()
        return "continue"

    if "open it again" in command:
        if memory["last_site"] == "google":
            speak("Opening Google again.")
            webbrowser.open("https://google.com")
        elif memory["last_site"] == "youtube":
            speak("Opening YouTube again.")
            webbrowser.open("https://youtube.com")
        else:
            speak("I don't remember what you opened.")
        return "continue"

    # 😊 EMOTIONS
    if "tired" in command:
        speak(random.choice(tired_responses))
        return "continue"

    if "happy" in command:
        speak(random.choice(happy_responses))
        return "continue"

    if "angry" in command:
        speak(random.choice(angry_responses))
        return "continue"

    if "joke" in command:
        speak(random.choice(joke_responses))
        return "continue"

    # 🤖 AI FALLBACK (OFFLINE)
    speak(ai_brain(command))
    return "continue"

# =========================
# 🚀 MAIN LOOP
# =========================
if __name__ == "__main__":
    speak("Jarvis initialized")

    if memory["name"]:
        speak(f"Welcome back, {memory['name']}.")

    wake_words = ["jarvis", "hey jarvis", "hello jarvis"]

    while True:
        try:
            print("Waiting for wake word...")
            text = listen(duration=4)

            if any(wake in text for wake in wake_words):
                speak("Yes, I'm listening")

                while True:
                    command = listen(duration=6)
                    if not command:
                        continue

                    if process_command(command) == "sleep":
                        break

        except KeyboardInterrupt:
            speak("Shutting down.")
            sys.exit()
