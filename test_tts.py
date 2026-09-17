import pyttsx3

engine = pyttsx3.init(driverName="sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

engine.say("Hello. If you hear this, text to speech is working.")
engine.runAndWait()
