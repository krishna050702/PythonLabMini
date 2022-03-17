
from flask import Flask,render_template,request
from chatterbot.chatterbot import ChatBot
from chatterbot import trainers

english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = trainers.ChatterBotCorpusTrainer(english_bot)

trainer.train("/content/english")

user = input()
english_bot.get_response(user)

for i in range(5):
  user = input()
  print(english_bot.get_response(user))

!pip install tk

import tkinter as tk

import tkinter as tk
window = tk.Tk()

