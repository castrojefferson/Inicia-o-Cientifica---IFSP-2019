from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

class Bot:
	def __init__(self, *args):
		self.chatbot = ChatBot('antony', read_only=True)
		self.trainer_corpus = ChatterBotCorpusTrainer(self.chatbot)
		self.trainer_list = ListTrainer(self.chatbot)

	def learn(self, lista_treinamento):
		self.trainer_list.train(list(lista_treinamento))

	def first_train(self):
		if(open('./configs/train.txt').read() == '0'	):
			open('./configs/train.txt', 'w').write('1')
			self.trainer_corpus.train("chatterbot.corpus.english")
		else:
			pass

	def get_response(self, text):
		return self.chatbot.get_response(text)

if __name__ == '__main__':
	Bot().first_train()
	while True:
		print(Bot().get_response(input("EU >>> ")))