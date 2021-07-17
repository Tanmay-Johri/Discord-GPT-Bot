from Tbot import telegram_chatbot
import re
import string

import internal_interaction_bot

bot = telegram_chatbot("/content/drive/My Drive/gpt-2/src/config.cfg")


def make_reply_b2b(msg, per):
    reply = None
    reply2 = None
    if msg is not None:

      print("A PROMPT HAS BEEN SENT BY :")
      print(per)
      print("\nTHE PROMPT IS : ")
      print(str(msg))

      basic_msg = msg.replace('\n', '')

      internal_interaction_bot.interact_model(length = 33, temperature=0.9 ,tanmay_outside_prompt = msg)
      reply = str(internal_interaction_bot.get_data())
      
      reply = reply.replace('\n', '')

      reply2_1 = re.findall('(.+?)[A-Z 0-9]:', reply)

      if (len(reply2_1) == 0):
        reply2 = reply
      else:
        reply2 = reply2_1[0]
      
      reply2_2 = re.findall('(.+?)<|endoftext|>', reply2)

      if (len(reply2_2) == 0):
        pass
      else:
        reply2 = reply2_2[0]


      
    if (((sum(word.strip(string.punctuation).isalpha() for word in reply2.split()) == 0)) and ((not reply2.startswith('Yes')) and (not reply2.startswith('No')) and (not reply2.startswith('yes')) and (not reply2.startswith('no')) ) ):
      reply2 = "Well, maybe you're right. Tell me more!"
    
    print("\nTHE REPLY TO BE SENT IS : ")
    print("AI - 1" + " :-\n" + reply2)
    print("__________________________________________________________")   
    return reply2

update_id = None
person = ''

def b2b(init_message, n_replies, fro, pers):
  
  # person = 'GPT-2'
  print("Reply number " + str(1))
  fin_q = "Q: " + init_message + "\n" + "A: "
  reply2 = make_reply_b2b(fin_q, pers)
  reply2 = reply2.strip()
  # reply2 = make_reply_b2b(init_message, pers)
  reply3 = "AI - 1" + " :-\n" + reply2
  bot.send_message(reply3, fro)

  if (pers == 'Tanmay'):
    pass
  else:
    tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe number of replies to be sent are\n\n"+str(n_replies) + "\n\n___________________"
    bot.send_message(tellgod, 967745126)
    tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
    bot.send_message(tellgod, 967745126)

  for i in range(1, n_replies):
      print("Reply number " + str(i+1))
      fin_q = fin_q + reply2 + "\nQ: " + reply2 + "\n" + "A: "
      reply2 = make_reply_b2b(fin_q, pers)
      reply2 = reply2.strip()
      # reply2 = make_reply_b2b(reply2, pers)

      reply3 = "AI - " + str((i%2)+1) + " :-\n" + reply2
      bot.send_message(reply3, fro)
      if (pers == 'Tanmay'):
        pass
      else:
        tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
        bot.send_message(tellgod, 967745126)
            
  final_message = "Chat between AIs completed!"
  bot.send_message(final_message, fro)
  if (pers == 'Tanmay'):
    pass
  else:
    tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nChat between AIs completed!" + "\n\n___________________"
    bot.send_message(tellgod, 967745126)


# while True:
#     updates = bot.get_updates(offset=update_id)
#     updates = updates["result"]
#     if updates:
#         for item in updates:
#             update_id = item["update_id"]
#             try:
#                 message = item["message"]["text"]
#             except:
#                 message = None
#             from_ = item["message"]["from"]["id"]
#             person = item["message"]["from"]["first_name"]
#             print("Reply number " + str(1))
#             reply2 = make_reply_b2b(message, person)
#             reply3 = "AI - 1" + " :-\n" + reply2
#             bot.send_message(reply3, from_)

#             for i in range(1, 3):
#               print("Reply number " + str(i+1))
#               reply2 = make_reply_b2b(reply2, person)

#               reply3 = "AI - " + str((i%2)+1) + " :-\n" + reply2
#               bot.send_message(reply3, from_)
            
#             final_message = "Chat between AIs completed!"
#             bot.send_message(final_message, from_)

            


