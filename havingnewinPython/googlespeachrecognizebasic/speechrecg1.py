import speech_recognition as sr
harvard = sr.AudioFile('F:\havingnewinPython\googlespeachrecognizebasic\harvard.wav')
r = sr.Recognizer()
with harvard as source:
  audio = r.record(source)
print(r.recognize_google(audio))


jackhammer = sr.AudioFile('F:\havingnewinPython\googlespeachrecognizebasic\jackhammer.wav')
with jackhammer as source:
   r.adjust_for_ambient_noise(source)
   audio = r.record(source)

print(r.recognize_google(audio))

#here we are connecting with micro phone

mic=sr.Microphone()
#print(sr.Microphone.list_microphone_names())

with mic as source:
    print('say some thing ')
    audi=r.listen(source)

print(r.recognize_google(audi,language="bn-BD"))