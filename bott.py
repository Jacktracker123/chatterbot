from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

bot = ChatBot('Talkie',tagger_language=ENGSM)
trainer = ListTrainer(bot)
for i in os.listdir('files'):
    con=open('files/' + i, 'r').read().splitlines()
    trainer.train(con)

while True:
    request = input("You: ")
    if request=='exit':
        break
    else:
        print(f"Bot: {bot.get_response(request)}")
