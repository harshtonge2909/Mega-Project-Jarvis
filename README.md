# Mega Project Jarvis

A Python-based personal voice assistant inspired by JARVIS. It listens for voice commands, recognizes wake words, responds using text-to-speech, remembers a user's name, and can open common websites like Google and YouTube.

## Features

- Voice activation using a wake word such as "Jarvis"
- Speech-to-text transcription with OpenAI Whisper
- Text-to-speech output using `pyttsx3`
- Simple offline AI-style responses for basic commands
- Memory saving for user name and last opened website
- Basic emotional and conversational responses
- Browser integration for opening websites

## Tech Stack

- Python 3
- `pyttsx3` for TTS
- `whisper` for speech recognition
- `sounddevice` for microphone input
- `numpy` for audio processing
- `webbrowser` for website launching

## Project Structure

```text
Mega Project Jarvis/
├── main.py
├── test_tts.py
├── memory.json
├── README.md
└── .git/
```

## Requirements

Install the required Python packages:

```bash
pip install pyttsx3 whisper sounddevice numpy
```

On Windows, this project is designed to use the system SAPI5 voice engine, which is supported by `pyttsx3`.

## Setup

1. Clone the repository:

```bash
git clone <your-repository-url>
cd Mega Project Jarvis
```

2. Install dependencies:

```bash
pip install pyttsx3 whisper sounddevice numpy
```

3. Run the assistant:

```bash
python main.py
```

## How to Use

- Say one of the wake words:
  - "Jarvis"
  - "Hey Jarvis"
  - "Hello Jarvis"
- After activation, speak commands like:
  - "My name is Alex"
  - "What is my name"
  - "Open Google"
  - "Open YouTube"
  - "Open it again"
  - "Tell me a joke"
  - "I am tired"
  - "Exit"

## Notes

- The assistant currently uses an offline fallback for general questions.
- The project is intended as a learning and personal assistant prototype.
- `memory.json` stores simple session data locally.

## License

This project is currently unlicensed. If you plan to publish it on GitHub, you may want to add a license file such as MIT later.

## Future Ideas

- Add a web-based AI API integration
- Support more commands and smart automation
- Add GUI support
- Improve wake-word detection and command handling
- Add more memory features and personalization
