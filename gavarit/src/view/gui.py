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
from src.controll.tts import Pyttsx3, Festival, Audio
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
		self.ids.voice.bind(text=self.selected_value)
		self.engine='system'
		self.text=""

	def play_audio(self):
		if self.engine == 'pyttsx3(Linux and Windows)':
			self.start_trhead = threading.Thread(target=Pyttsx3().play, args=(self.text,))
			self.start_trhead.start()
		elif self.engine == 'festival(Linux)':
			self.start_trhead = threading.Thread(target=Festival().play, args=(self.text,))
			self.start_trhead.start()

	def play_user_audio(self):
			self.start_trhead = threading.Thread(target=Audio().play())
			self.start_trhead.start()

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

	def selected_value(self, spinner, text, *args):
	    self.engine = text

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
			elif touch.spos[0] > 0.60:
				self.status=False
				self.microphone.set_status(False)
				self.microphone.save()

			else:
				self.status=False
				self.microphone.set_status(False)
				self.microphone.save()
		self.microphone.set_status(True)

class TextInput_:
	def __init__(self, *args):
		self.user_text=""

	def set_user_text(self, text):
		self.user_text = str(text)

	def get_user_text(self):
		return Sphinx().recognize()

text_input_class = TextInput_()

class Gui(App):
	def build(self):
		return Home()

if __name__ == '__main__':
	Gui().run()