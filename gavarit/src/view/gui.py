from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.event import EventDispatcher

import threading

from src.controll.microphone import Microphone
from src.controll.tts import GoogleTranslate, Pyttsx3, Festival, Audio
from src.controll.stt import Sphinx
from src.controll.chatbot import Bot

chatbot = Bot()
chatbot.first_train()

class Home(Screen):
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)
		self.chatbot=chatbot

		self.sphinx = Sphinx()
		self.text_input_class=text_input_class
		self.ids.voice.bind(text=self.show_selected_value)
		self.engine='system'
		self.text=""

	def play_audio(self):
		print(self.text)
		if self.engine == 'gtts':
			try:
				print(11)
				GoogleTranslate().execute(self.text)
				print(22)
				print(33)
			except:
				print("\n\n\nArquivo criado, porem nao executa o audio\n\n\n")

			Audio().play(file='./temp/file.mp3')

		elif self.engine == 'pyttsx3':
			Pyttsx3().play(self.text)
		elif self.engine == 'festival':
			Festival().play(self.text)

	def play_user_audio(self):
		Audio().play()

	def add_message_box_bot(self, *args):
		self.text=args[0]
		self.ids.message_box_bot.text=str(self.text)

	def add_message_box_user(self, text):
		self.text=str(self.chatbot.get_response(str(text)))
		self.ids.message_box_user.text=self.text

	def set_user_input(self, text):
		self.ids.user_input.text=text

	def get_user_text(self):
		get_reponse = threading.Thread(target=self.sphinx.recognize)
		return get_reponse

	def show_selected_value(self, spinner, text, *args):
	    print('The spinner', spinner, 'have text', text, '\n', text)
	    self.engine = text


""" TO-DO
		Obter resposta do bot
"""

class TouchWidget(Widget):
	def __init__(self, **kwargs):
		super(TouchWidget, self).__init__(**kwargs)
		self.microphone = Microphone()

	def on_touch_down(self, touch):
		self.status=True
		self.start_trhead = threading.Thread(target=self.microphone.start, args=(self,))
		self.start_trhead.start()

	
		if self.collide_point(*touch.pos):
			touch.grab(self)
		"""
			Implementar - Quando o botão for largado, retornar a posição inicial
		"""

	def on_touch_up(self, touch):
		if touch.grab_current is self:
			touch.ungrab(self)
			if touch.spos[0] < 0.45:
				try:
					self.status=False
					self.microphone.set_status(False)
					self.microphone.save()
				except:
					pass
				print("\nCANCEL...\n")

			elif touch.spos[0] > 0.60:
				self.status=False
				self.microphone.set_status(False)
				self.microphone.save()

				print("\nSEND...\n")
			else:
				self.status=False
				self.microphone.set_status(False)
				self.microphone.save()
				print("\nSEND...\n")

		self.microphone.set_status(True)

class TextInput_:
	def __init__(self, *args):
		self.user_text=""

	def set_user_text(self, text):
		self.user_text = str(text)

	def get_user_text(self):
		return Sphinx().recognize()

# Objeto global
text_input_class = TextInput_()

class Gui(App):
	def build(self):
		return Home()

class ScreenSettings:#Implementar Screen de Configuração 
	def __init__(self):
		pass

if __name__ == '__main__':
	Gui().run()