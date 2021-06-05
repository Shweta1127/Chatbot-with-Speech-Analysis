import speech_recognition as sr


r1 = sr.Rcognizer()
r2 = sr.Rcognizer()

with sr.Microphone() as source:
	audio = r1.listen(source)

text = r2.recognize_google(audio)
 
