import pyaudio
import wave
import time
import sys
import os
import configparser
from threading import Thread

import gtts
try:
	import pyttsx3
except:
	pass

AUDIO_FILE='./temp/file.wav'
AUDIO_FILE_MP3='./temp/file.mp3'
class GoogleTranslate:
	def __init__(self):#, *args):
		pass

	def execute(self, text):
		print(str(text))
		try:
			gtts.gTTS(str(text), lang='en-us').save(AUDIO_FILE_MP3)
		except:
			print(None)

class Pyttsx3:
	def __init__(self):
		self.engine = pyttsx3.init()
		self.engine.setProperty('voices', 'english')
		self.engine.setProperty('gender', 'female')

	def play(self, text):
		print('\n\nverificar se nao vai congelar o kivy\n\n')
		print(text)
		self.engine.say(text)
		runAndWait = Thread(target=self.engine.runAndWait)
		runAndWait.start()

class Festival:
	def __init__(self):
		pass

	def play(self, text):
		pass

class Audio():
	def __init__(self):
		pass
		
	def play(self, file=AUDIO_FILE):
		print(1)
		wf = wave.open(file, 'rb')
		p = pyaudio.PyAudio()

		def callback(in_data, frame_count, time_info, status):
		    data = wf.readframes(frame_count)
		    return (data, pyaudio.paContinue)

		stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		                channels=wf.getnchannels(),
		                rate=wf.getframerate(),
		                output=True,
		                stream_callback=callback)

		stream.start_stream()

		while stream.is_active():
		    time.sleep(0.1)

		stream.stop_stream()
		stream.close()
		wf.close()

		p.terminate()