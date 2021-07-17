from Tbot import telegram_chatbot
from bot_to_bot import b2b
from qa import qa_main
import re
import string

import internal_interaction_bot

bot = telegram_chatbot("/content/drive/My Drive/gpt-2/src/config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:

      print("A PROMPT HAS BEEN SENT BY :")
      print(person)
      print("\nTHE PROMPT IS : ")
      print(str(msg))

      if (sum(word.strip(string.punctuation).isalpha() for word in msg.split()) < 25):
        internal_interaction_bot.interact_model(length = int(2*len(msg.split())) ,tanmay_outside_prompt = msg)
        reply = str(internal_interaction_bot.get_data())
      else:
        internal_interaction_bot.interact_model(length = int(1.5*len(msg.split())), temperature=0.67 ,tanmay_outside_prompt = msg)
        reply = str(internal_interaction_bot.get_data())
      # print("Received the computed text (This sentence is from Tserver)")
      # reply = "We are Groot!"
    # print("\nReturning the reply now")
    # print("By the way, this is the reply I received")

      reply2_2 = re.findall('(.+?)<|endoftext|>', reply)

      if (len(reply2_2) == 0):
        pass
      else:
        reply = reply2_2[0]

    if ((sum(word.strip(string.punctuation).isalpha() for word in reply.split()) == 1) or (sum(word.strip(string.punctuation).isalpha() for word in reply.split()) == 0)):
      reply = "I am Groot!"
    
    print("\nTHE REPLY TO BE SENT IS : ")
    print(reply)
    print("__________________________________________________________")   
    return reply

update_id = None
person = ''
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = "/media"
            from_ = item["message"]["from"]["id"]
            person = item["message"]["from"]["first_name"]

            syntax_error = 0

            # if (person != 'Tanmay'):
            #   print(str(person) + " tried to use it")
            #   reply2 = "Sorry, the server is busy right now. \n\nContact Tanmay Johri!"
            #   bot.send_message(reply2, from_)
            #   continue

            if (message == '\start' or message == '/start'):
              print("\nStart message block activated")
              print(str(person) + " tried to use it")
              reply2 = "The server is ready! Enter the prompt for GPT-2"
              bot.send_message(reply2, from_)

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the /start command" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)

              print("Start message block has finished working!\n")

            
            elif (message == '/media'):
              print("\nMedia error block activated")
              print(str(person) + " tried to use it")

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " sent an media or typed /media" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)

              reply2 = "This bot doesn't support media!"
              bot.send_message(reply2, from_)
              print("Media error block has finished working!\n")

            elif(message == '/new'):
              
              print("What's new block activated")
              print(str(person) + " tried to use it")
              
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the /new command\n"+str(message) + "\nand the reply sent is\n\nOkay!  :)"+"\n\n___________________"
                bot.send_message(tellgod, 967745126)
              reply2 = "What\'s new:-\n\n\n1. The BOT_TO_BOT mode doesn't complete the sentences now. It replies to them.\n\n2. Changed the word limits and randomness of the replies.\n\n3. Added context in the BOT_TO_BOT feature. The AIs now remember what they were talking about a few messages ago.\n\n4. Handeled the <|EOT|> error\n\n5. Handled a few other difficulties for the AI.\n\n\nThat's it for now.\nHave fun!"
              bot.send_message(reply2, from_)
              print("What's new block has finished working!")

            elif (message == '\help' or message.startswith('/help') or message == 'Help' or message == 'help'):
              print("\nHelp message block activated")
              print(str(person) + " tried to use it")

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the /help command" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)

              reply2 = "What can this bot do?\n\nThis bot tries to complete your sentences and paragraphs\n\nThere are three types of prompts :-\n\n1. NORMAL PROMPT - AI tries to complete your sentences. Simply enter a paragraph or a sentence or a phrase. No syntax is required.\n\n2. BOT_TO_BOT PROMPT - Two AIs chat with each other. Just give them a topic (preferably in the form of a question) to talk about.\n(Type /bot_to_bot to see the syntax.)\n\n3. QUESTION PROMPT - Use this when you have a question. AI tries to reply to that question instead of just completing your sentences.\n(Type /question to see the syntax.)\n\nPRIVACY POLICY -\n\nYOUR MESSAGES CAN BE READ BY MY CREATOR\n(TANMAY - @TangentTanmay)\n\n\nThat's it. \nHave fun!"
              bot.send_message(reply2, from_)
              print("Help message block has finished working!\n")
            
            elif (message == '\bot_to_bot' or message.startswith('/bot_to_bot') or message == 'b2b' or message == 'Bot to bot'):
              print("\nB2B help message block activated")
              print(str(person) + " tried to use it")

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the /bot_to_bot command" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)


              reply2 = "To use BOT_TO_BOT mode:\n\n\n1. Start your message with\n/b2b3 or /b2b5 or /b2b with any number\n\n2. The number decides how long the AIs will talk to each other\n\n3. After /b2b(a natural number), leave a space and type a few sentences in the form of a question\n\n4. The AIs will start by replying to it\n\n\nThat's it. \nHave fun!"
              bot.send_message(reply2, from_)
              print("B2B help message block has finished working!\n")
            
            elif ((message.startswith('Hello') or message.startswith('hello') or message.startswith('Heelo') or message.startswith('Hi') or message.startswith('Hey') ) and (sum(word.strip(string.punctuation).isalpha() for word in message.split()) < 3)):
              print("\nHello message block activated")
              print(str(person) + " tried to use it")

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the hello block" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)


              reply2 = "Hello there!"
              bot.send_message(reply2, from_)
              print("Hello message block has finished working!\n")

            elif (message == '\question' or message.startswith('/question') or message.startswith('Question') or message == 'Question mode'):
              print("\nQuestion help message block activated")
              print(str(person) + " tried to use it")

              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the /question command" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)


              reply2 = "To use QUESTION mode:\n\n\n1. Start your message with /q \n\n2. After /q, leave a space and type your question\n\n\nThat's it. \nHave fun!"
              bot.send_message(reply2, from_)
              print("Question help message block has finished working!\n")
            
            # elif (message.startswith('\1') or message.startswith('/1') or message.startswith('\one') or message.startswith('/one')):
            #   print("\nOne word block activated")
            #   print(str(person) + " tried to use it")

            #   list_mess = re.findall('/1 (.+)', message)
            #   strings = [str(sen) for sen in list_mess]
              
            #   if (len(strings) > 0):
            #     act_q = str("".join(strings))
            #     if (act_q.startswith('\\') or act_q.startswith('/')):
            #       syntax_error = 1
            #       error_message = "Please don't use two commands at the same time!"
            #       if (person == 'Tanmay'):
            #         pass
            #       else:
                    
            #         tellgod = "___________________\n\n" + str(person) + " used two commands at once" + "\n\n___________________"
            #         bot.send_message(tellgod, 967745126)

            #       bot.send_message(error_message, from_)
            #     else:
                  
            #       if (person == 'Tanmay'):
            #         pass
            #       else:
            #         tellgod = "___________________\n\n" + str(person) + " used the one word block correctly" + "\n\n___________________"
            #         bot.send_message(tellgod, 967745126)
                  
            #       internal_interaction_bot.interact_model(length = 1 ,tanmay_outside_prompt = message)
            #       reply = str(internal_interaction_bot.get_data())
            #       print("\nTHE REPLY TO BE SENT IS :")
            #       print(reply)
            #       bot.send_message(reply, from_)

            #   else:
            #     syntax_error = 1
            #     error_message = "SYNTAX ERROR - Format should be:-\n /1\nand then a space, and then your sentence."
            #     bot.send_message(error_message, from_)
                
            #     if (person == 'Tanmay'):
            #       pass
            #     else:
            #       tellgod = "___________________\n\n" + str(person) + " is making a syntax error in one word block" + "\n\n___________________"
            #       bot.send_message(tellgod, 967745126)

              
            #   if (syntax_error == 1):
            #     print("User is making a syntax error!")
            #   print("One word block has finished working!\n")
  
                             
            elif (message.startswith('\q') or message.startswith('/q') or message.startswith('\Q') or message.startswith('/Q')):
              print("\nQA block activated")
              print(str(person) + " tried to use it")
              list_mess = re.findall('/q (.+)', message)
              strings = [str(sen) for sen in list_mess]
              
              if (len(strings) > 0):
                act_q = str("".join(strings))
                if (act_q.startswith('\\') or act_q.startswith('/')):
                  syntax_error = 1
                  error_message = "Please don't use two commands at the same time!"
                  if (person == 'Tanmay'):
                    pass
                  else:
                    tellgod = "___________________\n\n" + str(person) + " used two commands at once" + "\n\n___________________"
                    bot.send_message(tellgod, 967745126)

                  bot.send_message(error_message, from_)
                else:
                  fin_q = "Q: " + act_q + " \n " + "A:"
                  if (person == 'Tanmay'):
                    pass
                  else:
                    tellgod = "___________________\n\n" + str(person) + " used the question block correctly\n\nThe message was\n\n"+str(message) + "\n\n___________________"
                    bot.send_message(tellgod, 967745126)

                  qa_main(fin_q, from_, person)
                  
              else:
                syntax_error = 1
                error_message = "SYNTAX ERROR - Format should be:-\n /q\nand then a space, and then your question.\n\nIn /q, the \'q\' should not be capital."
                bot.send_message(error_message, from_)
                
                if (person == 'Tanmay'):
                  pass
                else:
                  tellgod = "___________________\n\n" + str(person) + " is making a syntax error in Question block" + "\n\n___________________"
                  bot.send_message(tellgod, 967745126)

              
              if (syntax_error == 1):
                print("User is making a syntax error!")
              print("QA block has finished working!\n")
  
            elif (message.startswith('\b2b') or message.startswith('/b2b')):
              print("\nb2b block activated")
              print(str(person) + " tried to use it")
              list_number = re.findall('2b([0-9]+) ', message)
              strings = [str(integer) for integer in list_number]
              if (len(strings) == 0):
                syntax_error = 1
                strings.append('1')
              T_n_replies = int("".join(strings))
              
              print("\nThe user chose the number of replies to be " + str(T_n_replies) + "\n")

              if (T_n_replies > 5):
                T_n_replies = 3
                warning_message = "Please choose a number less than 9.\nOtherwise it'll take a lot of time.\nWe have chosen 4 for you this time.\nYou'll start receiving replies now!"
                bot.send_message(warning_message, from_)
                print("It has been changed to 3")
                
              if (syntax_error == 0):
                list_mess = re.findall('2b[0-9]+ (.+)', message)
                strings = [str(sen) for sen in list_mess]
                act_mess = "".join(strings)
                if (len(strings) > 0):
                  if (act_mess.startswith('\\') or act_mess.startswith('/')):
                    error_message = "Please don't use two commands at the same time!"
                    bot.send_message(error_message, from_)
                    
                    if (person == 'Tanmay'):
                      pass
                    else:
                      tellgod = "___________________\n\n" + str(person) + " is using two commands at once" + "\n\n___________________"
                      bot.send_message(tellgod, 967745126)

                  else:
                    if (person == 'Tanmay'):
                      pass
                    else:
                      tellgod = "___________________\n\n" + str(person) + " used the b2b block correctly\n\nThe message was\n\n"+str(message) + "\n\n___________________"
                      bot.send_message(tellgod, 967745126)

                    b2b(act_mess, T_n_replies, from_, person)
                    
                    
                else:
                  syntax_error = 1
                  error_message = "SYNTAX ERROR - Format should be:-\n /b2b(a natural number)\nand then a space, and then your message"
                  bot.send_message(error_message, from_)
              else:
                error_message = "SYNTAX ERROR - Format should be:-\n /b2b(a natural number)\nand then a space, and then your message"
                bot.send_message(error_message, from_)
              if (syntax_error == 1):
                print("User is making a syntax error!")
                
                if (person == 'Tanmay'):
                  pass
                else:
                  tellgod = "___________________\n\n" + str(person) + " is making a syntax error in Bot_to_Bot" + "\n\n___________________"
                  bot.send_message(tellgod, 967745126)

              print("b2b block has finished working!\n")

            elif(message.startswith('\\') or message.startswith('/')):
              print("Command error block activated\n")
              print(str(person) + " tried to use it")
              
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " is using an invalid command" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)

              error_message = "This is not a valid command. Please type /help for help"
              bot.send_message(error_message, from_)
              print("User is making a command error!")
              print("Command error block has finished working!\n")

            elif((message.startswith('Okay')) and (sum(word.strip(string.punctuation).isalpha() for word in message.split()) < 4)):
              
              print("Okay message block activated")
              print(str(person) + " tried to use it")
              print("Message was " + str(message))
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " sent this message\n"+str(message) + "\nand the reply sent is\n\nOkay!  :)"+"\n\n___________________"
                bot.send_message(tellgod, 967745126)
              reply2 = "Okay!  :)"
              bot.send_message(reply2, from_)
              print("Okay block has finished working!")

            elif((sum(word.strip(string.punctuation).isalpha() for word in message.split()) == 0)):
              
              print("Almost empty message block activated")
              print(str(person) + " tried to use it")
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " sent a message with no alphabets" + "\n\n___________________"
                bot.send_message(tellgod, 967745126)
              reply2 = "  :)  "
              bot.send_message(reply2, from_)
              print("Almost empty message block has finished working!")

            elif((sum(word.strip(string.punctuation).isalpha() for word in message.split()) == 1)):
              
              print("One word message block activated")
              print(str(person) + " tried to use it")
              print("Message was " + str(message))
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " sent a message with only one word\n\nIt was "+str(message) + "\n\n___________________"
                bot.send_message(tellgod, 967745126)
              reply2 = message + "!"
              bot.send_message(reply2, from_)
              print("One word message block has finished working!")

            elif((message.startswith('You are')) and (sum(word.strip(string.punctuation).isalpha() for word in message.split()) < 6)):
              
              print("You are message block activated")
              print(str(person) + " tried to use it")
              print("Message was " + str(message))
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " sent this message\n"+str(message) + "\nand the reply sent is\n\nHaha! You bet! :)"+"\n\n___________________"
                bot.send_message(tellgod, 967745126)
              reply2 = "Haha! You bet!  :)"
              bot.send_message(reply2, from_)
              print("You are message block has finished working!")

            

            else:
              print("\nNormal block activated")
              print(str(person) + " tried to use it")
              
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the normal block\n\nThe message was\n\n"+str(message) + "\n\n___________________"
                bot.send_message(tellgod, 967745126)

              if (message.startswith('What') or message.startswith('Who') or message.startswith('Why') or message.startswith('When') or message.startswith('How') or message.endswith('?') or message.endswith(' m') or message.startswith('Do you ')):
                error_message = "You might want to enter QUESTION mode for this.\nType /help or /question to know more.\nCurrently, this message is being processed in NORMAL mode."
                bot.send_message(error_message, from_)
              reply2 = make_reply(message)
              bot.send_message(reply2, from_)
              if (person == 'Tanmay'):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the normal block\n\nThe reply sent is\n\n"+str(reply2) + "\n\n___________________"
                bot.send_message(tellgod, 967745126)
              print("Normal block has finished working!")


