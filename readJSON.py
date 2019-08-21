# Ch 9: Files (Aug 21)
# 11. Reading a JSON file 
# JSON = stands for JavaScript Object Notation 
#	note: is not restricted to only JavaScript 
import json 
with open('message.json') as message_json: 
  message = json.load(message_json)
  print(message['text'])