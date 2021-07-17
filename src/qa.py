from Tbot import telegram_chatbot
import re
import string

import internal_interaction_bot

bot = telegram_chatbot("/content/drive/My Drive/gpt-2/src/config.cfg")


def make_reply_qa(msg, per):
    reply = None
    reply2 = None
    if msg is not None:

      print("A PROMPT HAS BEEN SENT BY :")
      print(per)
      print("\nTHE PROMPT IS : ")
      print(str(msg))

      basic_msg = msg.replace('\n', ' ')

      internal_interaction_bot.interact_model(length = int((3)*(sum(word.strip(string.punctuation).isalpha() for word in basic_msg.split()))), temperature=0.67 ,tanmay_outside_prompt = msg)
      reply = str(internal_interaction_bot.get_data())
      
      reply = reply.replace('\n', ' ')

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



    if (sum(word.strip(string.punctuation).isalpha() for word in reply2.split()) == 0):
      reply2 = "I am Groot!"
      
    print("\nTHE REPLY TO BE SENT IS : ")
    print(reply2)
    print("__________________________________________________________")   
    return reply2

update_id = None
person = ''

def qa_main(init_message, fro, pers):
  
  reply3 = make_reply_qa(init_message, pers)
  bot.send_message(reply3, fro)

  if (pers == 'Tanmay'):
    pass
  else:
    tellgod = "___________________\n\n" + str(pers) + " used the QUESTION mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
    bot.send_message(tellgod, 967745126)

            
  # final_message = "Chat between AIs completed!"
  # bot.send_message(final_message, fro)


