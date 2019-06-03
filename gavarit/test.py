def speak(text, lang='en'):
	from gtts import gTTS
	from pygame import mixer

	tts = gTTS(text=text, lang='en-us')
	tts.save('./file.mp3')
	
	mixer.init()
	mixer.music.load('./file.mp3')
	mixer.music.play()
	while True:
		pass
speak('Hello, how are you?')