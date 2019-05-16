import speech_recognition as sr

r = sr.Recognizer()
mc=sr.Microphone()
with mc as source:
    print('Say Something!')
    audio = r.listen(source)


text = r.recognize_google(audio,language="bn-BD")
print(text)