import os
import gtts
import pygame
import configparser
from threading import Thread

class GoogleTranslate:
	def __init__(self):#, *args):
		pass

	def create(self, text):
		print(str(text))
		gtts.gTTS(str(text), lang='en').save('temp/speak.wav')

class Espeak:
	def __init__(self):
		from espeak import espeak
		espeak.set_voice("en")

	def play(self, text):
		espeak.synth(text)

class Pyttsx3:
	def __init__(self):
		import pyttsx3
		self.engine = pyttsx3.init()
		self.engine.setProperty('voices', 'english')
		self.engine.setProperty('gender', 'female')

	def play(self, text):
		print('\n\nverificar se nao vai congelar o kivy\n\n')
		self.engine.say(text)
		runAndWait = Thread(target=self.engine.runAndWait)
		runAndWait.start()

class Audio():
	def __init__(self):
		pygame.init()
		
		self.config = configparser.ConfigParser()
		self.config.read('../../config.ini')

	def play(self):
		'''try:
									pygame.mixer.music.stop()
								except:
									pass
		'''
		self.pygame_start()
		#start_audio = Thread(target=self.pygame_start)
		#start_audio.start()

	def stop(self):
		pygame.mixer.music.stop()
		try:
			print('_')
			os.remove('./temp/file.wav')
			print('_|')
		except:
			pass

	def pygame_start(self):
		try:
			pygame.mixer.music.load('./temp/file.wav')
			pygame.mixer.music.play()
			pygame.mixer.music.set_volume(1)
			pygame.mixer.music.terminate()

		except:
			print('pass')

if __name__ == '__main__':
	GoogleTranslate().create(input("TEXT: "))
	audio = Audio()
	audio.play()

	text=input("TEXT: ")
	"""
	text = text.replace("\"", "'")
	print("\""+text+"\"")
	start_audio = Thread(target=os.system, args=["espeak \""+text+"\"",])
	start_audio.start()
	"""
	#Pyttsx3().play(text)