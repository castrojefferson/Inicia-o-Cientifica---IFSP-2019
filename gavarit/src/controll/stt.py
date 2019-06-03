from threading import Thread

import speech_recognition

class Sphinx:
	def __init__(self):
		self.sphinx = speech_recognition.Recognizer()
		self.text = ""

	def get_text(self, text):
		return self.text

	def recognize(self, path="./temp/file.wav"):
		with speech_recognition.AudioFile(path) as source:
			self.audio = self.sphinx.record(source)
		try:
			self.text = self.sphinx.recognize_sphinx(self.audio)
			return str(self.text)
		except speech_recognition.UnknownValueError:
			self.text = "Sphinx could not understand audio"
		except speech_recognition.RequestError as e:
			pass