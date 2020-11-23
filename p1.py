
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS




def speak(text):
	tts = gTTS(text = text, lang = 'en')
	filename = "sample.mp3"
	tts.save(filename)
	playsound.playsound(filename)	

def get_audio():
	print('Speak..')
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
			
		except Exception as e:
			print("Exception : ", str(e))

	return said

def insert_words():
	
	speak('New word')
	new_key = get_audio()
	
	speak('Add response')
	new_val = get_audio()
	
	known_words[new_key] = new_val
	confirmation = f'Your word {new_key} with value {new_val} has been saved in known_words.'

	return confirmation

def delete_word():
	
	speak('Delete the word')
	delete_key = get_audio()

	if delete_key in known_words_keys:
		known_words.pop(delete_key)
		confirmation = f'Your word {delete_key} has been deleted.'

	else:
		confirmation = 'Word not found in current dictionary'
	return confirmation


known_words = {'happy':'Because today we got 50 dollars. yahooo!','coolest':'Aseeb bhaiya is the coolest brother of them all.','fattest':'Shazia is the fattest.','check':'reply check','name' : "Don't have a name.", 'birthday' :'may 20th 2020', 'version':'Prototype 1', 'job':'I am a robot sir.'}
known_words_keys = known_words.keys()

while True:

	reply = get_audio()
	print('Inside Home')

	match_word = [word for word in known_words_keys if word in reply]

	# empty string from user
	if len(reply) == 0:
		speak('Please. Speak again')	

	# to stop the pro
	elif "stop" in reply:
		speak('yes sir! stopping now')
		print('Program Ended!')
		break

	# inserting word option
	elif "insert word" in reply:
		switch = True
		while switch == True:
			speak('Say proceed to Insert word else say pass')
			print('Inside insert word')
			add_word_response = get_audio()

			if 'proceed' in add_word_response:
				confirmation_msg = insert_words()
				speak(confirmation_msg)
				print(known_words)
				switch = False	

			elif 'pass' in add_word_response:
				speak('Passing')
				switch = False
				
			else:
				pass

	# responding 
	elif len(match_word) != 0:
		response = known_words[f"{match_word[0]}"]
		speak(response)

	# delete word
	elif 'delete word' in reply:
		switch = True
		while switch == True:
			speak('Say proceed to delete word or say pass')
			print('Inside delete word')
			delete_word_response = get_audio()

			if 'proceed' in delete_word_response:
				confirmation_msg = delete_word()
				speak(confirmation_msg)
				print(known_words)
				switch = False	

			elif 'pass' in delete_word_response:
				speak('Passing')
				switch = False
			else:
				speak("What's it? Please say that again.")
				
	