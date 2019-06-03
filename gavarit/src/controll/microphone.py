import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import os
class Microphone:
	def __init__(self, *args):
		self.FORMAT = pyaudio.paInt16 # data type formate
		self.CHANNELS = 2 # Adjust to your number of channels
		self.RATE = 44100 # Sample Rate
		self.CHUNK = 1024 # Block Size
		self.RECORD_SECONDS = 5 # Record time
		self.WAVE_OUTPUT_FILENAME = "./temp/file.wav"

		self.status = False

	def set_status(self, status=True):
		if status is bool:
			self.status=status

	def start(self, home):
		try:
			os.remove('./temp/file.wav')
		except:
			pass

		self.audio  = pyaudio.PyAudio()
		self.status = True
		self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                rate=self.RATE, input=True,
                frames_per_buffer=self.CHUNK)

		self.frames = []
		contador=0
		while home.status == True:#self.status == True:
			data = self.stream.read(self.CHUNK)
			self.frames.append(data)
			contador+=1
			print(str(contador)+"\t\t"+str(self.status))

	def save(self):
		try:
			self.stream.stop_stream()
			self.stream.close()
			self.audio.terminate()
			try:
				os.system("echo '' > /temp/file.wav")
				self.waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
			except:
				self.waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')

			self.waveFile.setnchannels(self.CHANNELS)
			self.waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
			self.waveFile.setframerate(self.RATE)
			self.waveFile.writeframes(b''.join(self.frames))
			self.waveFile.close()
		except:
			pass

	def get_status(self):
		return self.status