# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import re
import string
import internal_interaction_bot


# MAKE NORMAL REPLY START
def make_reply(msg, pers):

    reply = None

    if msg is not None:

      print("A PROMPT HAS BEEN SENT BY :")
      print(pers)
      print("\nTHE PROMPT IS : ")
      print(str(msg))

      if (sum(word.strip(string.punctuation).isalpha() for word in msg.split()) < 25):
        internal_interaction_bot.interact_model(length = int(2*len(msg.split())) ,tanmay_outside_prompt = msg)
        reply = str(internal_interaction_bot.get_data())
      else:
        internal_interaction_bot.interact_model(length = int(1.5*len(msg.split())), temperature=0.67 ,tanmay_outside_prompt = msg)
        reply = str(internal_interaction_bot.get_data())

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
# MAKE NORMAL REPLY END




# MAKE QA REPLY
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

# MAKE QA REPLY END


# B2B DRIVER
# def b2b(init_message, n_replies, message, pers):
  
#   # person = 'GPT-2'
#   print("Reply number " + str(1))
#   fin_q = "Q: " + init_message + "\n" + "A: "
#   reply2 = make_reply_b2b(fin_q, pers)
#   reply2 = reply2.strip()
#   # reply2 = make_reply_b2b(init_message, pers)
#   reply3 = "AI - 1" + " :-\n" + reply2
#   await message.channel.send(reply3)

#   if (str(pers) == 'TangentTanmay#1223'):
#     pass
#   else:
#     tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe number of replies to be sent are\n\n"+str(n_replies) + "\n\n___________________"
#     await message.channel.send(tellgod)
#     tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
#     await message.channel.send(tellgod)

#   for i in range(1, n_replies):
#       print("Reply number " + str(i+1))
#       fin_q = fin_q + reply2 + "\nQ: " + reply2 + "\n" + "A: "
#       reply2 = make_reply_b2b(fin_q, pers)
#       reply2 = reply2.strip()
#       # reply2 = make_reply_b2b(reply2, pers)

#       reply3 = "AI - " + str((i%2)+1) + " :-\n" + reply2
#       await message.channel.send(reply3)
#       if (str(pers) == 'TangentTanmay#1223'):
#         pass
#       else:
#         tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
#         await message.channel.send(tellgod)
            
#   final_message = "Chat between AIs completed!"
#   await message.channel.send(final_message)
#   if (str(pers) == 'TangentTanmay#1223'):
#     pass
#   else:
#     tellgod = "___________________\n\n" + str(pers) + " used the BOT_TO_BOT mode\n\nChat between AIs completed!" + "\n\n___________________"
#     await message.channel.send(tellgod)
# B2B DRIVER END



# B2B MAKE REPLY
def make_reply_b2b(msg, per):
    reply = None
    reply2 = None
    if msg is not None:

      print("A PROMPT HAS BEEN SENT BY :")
      print(str(per))
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

# B2B MAKE REPLY END





# BORING STUFF
DISCORD_TOKEN = "Enter_Token_Here"
prefix = '>'
client = commands.Bot(command_prefix = prefix)
exceptions = ["TangentTanmay#1223"]
restricted = [""]
nottalking = 0
botlogs = 0

@client.event
async def on_ready():
  global botlogs
  print("bot is ready")
  guild_count = 0
  for guild in client.guilds:
    # PRINT THE SERVER'S ID AND NAME.
    print("guild id - " + str(guild.id) + " Name - " + str(guild.name))
    # INCREMENTS THE GUILD COUNTER.
    guild_count = guild_count + 1

  # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
  print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
  
  for i in range(guild_count):
    if(str(client.guilds[i].id) == "772183715463692298"):
      print("The index of Bot logs is : " + str(i))
      botlogs = i
  
  print("The value of global botlogs is now " + str(botlogs))
  

# BORING STUFF END


# COMMANDS
@client.command()
async def ping(ctx):
  await ctx.send("Pong! " + str(int(client.latency)*1000) + "ms")

@client.command()

# COMMANDS END


# NORMAL MESSAGES
@client.event
async def on_message(message):

  global botlogs
  global nottalking
  global restricted

  await client.process_commands(message)

  if(message.content.startswith(prefix)):
    return
  else:
    if message.author == client.user:
      return
    elif ((str(message.author) in restricted) and ((message.content.startswith('/n '))or(message.content.startswith('/q '))or(message.content.startswith('/b2b0 '))or(message.content.startswith('/b2b1 '))or(message.content.startswith('/b2b2 '))or(message.content.startswith('/b2b3 '))or(message.content.startswith('/b2b4 '))or(message.content.startswith('/b2b5 '))or(message.content.startswith('/b2b6 '))or(message.content.startswith('/b2b7 '))or(message.content.startswith('/b2b8 '))or(message.content.startswith('/b2b9 ')))):
      await message.channel.send("ACCESS DENIED! Lol XD! Master asked me not to talk to you lol XD")
      print(str(message.author) + " tried to access me!")
      return

    # FUN PART STARTS 

    # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n_______________________________")

    # QUESTION MODE HELP START
    if (message.content == '\question' or message.content.startswith('/question') or message.content.startswith('/Question') or message.content == '/Question mode'):
      print("\nQuestion help message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")

      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the /question command" + "\n\n___________________"
        # await message.channel.send(tellgod)
        # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")


      reply2 = "To use QUESTION mode:\n\n\n1. Start your message with /q \n\n2. After /q, leave a space and type your question\n\n\nThat's it. \nHave fun!"
      await message.channel.send(reply2)
      print("Question help message block has finished working!\n")
    # QUESTION MODE HELP END


    # QUESTION BLOCK
    elif (message.content.startswith('/q') or message.content.startswith('/Q') or message.content.startswith('\q') or message.content.startswith('\Q')):
      person = message.author
      syntax_error = 0

      print("\nQA block activated")
      nottalking = 1
      print(str(person) + " tried to use it")
      list_mess = re.findall('/q (.+)', str(message.content))
      strings = [str(sen) for sen in list_mess]
              
      if (len(strings) > 0): #There is a question 
        act_q = str("".join(strings))
        if (act_q.startswith('\\') or act_q.startswith('/')): #Two commands error
          syntax_error = 1
          error_message = "Please don't use two commands at the same time!"
          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used two commands at once" + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")
            # await message.channel.send(tellgod)
          await message.channel.send(error_message)

        else: #Two commands error handled
          fin_q = "Q: " + act_q + " \n" + "A:"
          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used the question block correctly\n\nThe message was\n\n"+str(fin_q) + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await message.channel.send(tellgod)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

          reply2 = make_reply_qa(str(fin_q), str(person))
          await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
          await message.channel.send(reply2)
          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used the question block correctly\n\nThe reply sent is\n\n"+str(reply2) + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await message.channel.send(tellgod)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

                  
      else: #There was no question
        syntax_error = 1
        error_message = "SYNTAX ERROR - Format should be:-\n /q\nand then a space, and then your question.\n\nIn /q, the \'q\' should not be capital."
        await message.channel.send(error_message)

                
        if (str(person) in exceptions):
          pass
        else:
          tellgod = "___________________\n\n" + str(person) + " is making a syntax error in Question block" + "\n\n___________________"
          # bot.send_message(tellgod, 967745126)
          # await message.channel.send(tellgod)
          # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
          await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

              
      if (syntax_error == 1):
        print("User is making a syntax error!")
      print("QA block has finished working!\n")
    # QUESTION BLOCK END



    # HELP BLOCK START
    elif (message.content == '\help' or message.content.startswith('/help') or message.content == '/Help'):
      print("\nHelp message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")

      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the /help command" + "\n\n___________________"
        # await message.channel.send(tellgod)
        # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      reply2 = "What can this bot do?\n\nThis bot tries to complete your sentences and paragraphs\n\nThere are three types of prompts :-\n\n1. NORMAL PROMPT - AI tries to complete your sentences. Simply enter a paragraph or a sentence or a phrase. Start your message with a \'/n\' and a space. Then type your prompt. I ignore all messages that don't start with a /.\n\n2. BOT_TO_BOT PROMPT - Two AIs chat with each other. Just give them a topic (preferably in the form of a question) to talk about.\n(Type /bot_to_bot to see the syntax.)\n\n3. QUESTION PROMPT - Use this when you have a question. AI tries to reply to that question instead of just completing your sentences.\n(Type /question to see the syntax.)\n\nSOME TIPS:\n1. The longer your prompt, the better\n2. Please add all important punctuation marks. That'll help me a lot. End your sentences with a full-stop or a \'?\'\n3. You can also access some additional commands by using \'>\'\n4. Unfortunately, I cannot reply properly to imperative sentences :(. Try not giving me orders :)\n\nPRIVACY POLICY -\nYOUR MESSAGES CAN BE READ BY MY CREATOR\n(@TangentTanmay#1223)\n\n\nThat's it. \nHave fun!"
      await message.channel.send(reply2)
      print("Help message block has finished working!\n")
    # HELP BLOCK END



    # BOT TO BOT HELP START
    elif (message.content == '\bot_to_bot' or message.content.startswith('/bot_to_bot') or message.content == '/b2b' or message.content == '/Bot to bot'):
      print("\nB2B help message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")

      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the /bot_to_bot command" + "\n\n___________________"
        # await message.channel.send(tellgod)
        # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")


      reply2 = "To use BOT_TO_BOT mode:\n\n\n1. Start your message with\n/b2b3 or /b2b5 or /b2b with any number\n\n2. The number decides how long the AIs will talk to each other\n\n3. After /b2b(a natural number), leave a space and type a few sentences in the form of a question\n\n4. The AIs will start by replying to it\n\n\nThat's it. \nHave fun!"
      await message.channel.send(reply2)
      print("B2B help message block has finished working!\n")
    # BOT TO BOT HELP END




    # HELLO BLOCK START
    elif ((message.content.startswith('/n Hello') or message.content.startswith('/n hello') or message.content.startswith('/n Heelo') or message.content.startswith('/n Hi') or message.content.startswith('/n hey') or message.content.startswith('/n hi') or message.content.startswith('/n Hey') ) and (sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) < 5)):
      print("\nHello message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")

      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the hello block" + "\n\n___________________"
        # await message.channel.send(tellgod)
        # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      reply2 = "Hello there!"
      await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
      await message.channel.send(reply2)
      print("Hello message block has finished working!\n")
    # HELLO BLOCK END




    





    
    # B2B
    elif (message.content.startswith('\b2b') or message.content.startswith('/b2b')):
      print("\nb2b block activated")
      nottalking = 1
      syntax_error = 0
      person = message.author
      print(str(person) + " tried to use it")
      list_number = re.findall('2b([0-9]+) ', str(message.content))
      strings = [str(integer) for integer in list_number]
      if (len(strings) == 0):
        syntax_error = 1
        strings.append('1')
      T_n_replies = int("".join(strings))
              
      print("\nThe user chose the number of replies to be " + str(T_n_replies) + "\n")

      if (T_n_replies > 5):
        T_n_replies = 3
        warning_message = "Please choose a number less than 9.\nOtherwise it'll take a lot of time.\nWe have chosen 3 for you this time.\nYou'll start receiving replies now!"
        await message.channel.send(warning_message)
        print("It has been changed to 3")
                
      if (syntax_error == 0):
        list_mess = re.findall('2b[0-9]+ (.+)', str(message.content))
        strings = [str(sen) for sen in list_mess]
        act_mess = "".join(strings)
        if (len(strings) > 0):
          if (act_mess.startswith('\\') or act_mess.startswith('/')):
            error_message = "Please don't use two commands at the same time!"
            await message.channel.send(error_message)
                    
            if (str(person) in exceptions):
              pass
            else:
              tellgod = "___________________\n\n" + str(person) + " is using two commands at once" + "\n\n___________________"
              # await message.channel.send(tellgod)
              # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")
              await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

          else:
            if (str(person) in exceptions):
              pass
            else:
              tellgod = "___________________\n\n" + str(person) + " used the b2b block correctly\n\nThe message was\n\n"+str(message.content) + "\n\n___________________"
              # await message.channel.send(tellgod)
              # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
              await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

            # b2b(act_mess, T_n_replies, message, person)

            print("Reply number " + str(1))
            fin_q = "Q: " + act_mess + "\n" + "A: "
            reply2 = make_reply_b2b(fin_q, person)
            reply2 = reply2.strip()
            # reply2 = make_reply_b2b(init_message, pers)
            reply3 = "AI - 1" + " :-\n" + reply2
            await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
            await message.channel.send(reply3)

            if (str(person) in exceptions):
              pass
            else:
              tellgod = "___________________\n\n" + str(person) + " used the BOT_TO_BOT mode\n\nThe number of replies to be sent are\n\n"+str(T_n_replies) + "\n\n___________________"
              # await message.channel.send(tellgod)
              # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
              await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")
              tellgod = "___________________\n\n" + str(person) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
              # await message.channel.send(tellgod)
              # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
              await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

            for i in range(1, T_n_replies):
              print("Reply number " + str(i+1))
              fin_q = fin_q + reply2 + "\nQ: " + reply2 + "\n" + "A: "
              reply2 = make_reply_b2b(fin_q, person)
              reply2 = reply2.strip()
              # reply2 = make_reply_b2b(reply2, pers)

              reply3 = "AI - " + str((i%2)+1) + " :-\n" + reply2
              await message.channel.send(reply3)
              if (str(person) in exceptions):
                pass
              else:
                tellgod = "___________________\n\n" + str(person) + " used the BOT_TO_BOT mode\n\nThe reply sent is\n\n"+str(reply3) + "\n\n___________________"
                # await message.channel.send(tellgod)
                # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
                await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")
            
            final_message = "Chat between AIs completed!"
            await message.channel.send(final_message)
            if (str(person) in exceptions):
              pass
            else:
              tellgod = "___________________\n\n" + str(person) + " used the BOT_TO_BOT mode\n\nChat between AIs completed!" + "\n\n___________________"
              # await message.channel.send(tellgod)
              # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
              await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

        else:
          syntax_error = 1
          error_message = "SYNTAX ERROR - Format should be:-\n /b2b(a natural number)\nand then a space, and then your message"
          await message.channel.send(error_message)
      else:
        error_message = "SYNTAX ERROR - Format should be:-\n /b2b(a natural number)\nand then a space, and then your message"
        await message.channel.send(error_message)
      if (syntax_error == 1):
        print("User is making a syntax error!")
                
        if (str(person) in exceptions):
          pass
        else:
          tellgod = "___________________\n\n" + str(person) + " is making a syntax error in Bot_to_Bot" + "\n\n___________________"
          # await message.channel.send(tellgod)
          # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
          await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      print("b2b block has finished working!\n")
    # B2B END



    # OKAY BLOCK START
    elif(((message.content.startswith('/n Okay')) or (message.content.startswith('/n okay'))) and (sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) < 5)):
              
      print("Okay message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")
      print("Message was " + str(message.content))
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " sent this message\n"+str(message.content) + "\nand the reply sent is\n\nOkay!  :)"+"\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      reply2 = "Okay!  :)"
      # bot.send_message(reply2, from_)
      await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
      await message.channel.send(reply2)
      print("Okay block has finished working!")
    # OKAY BLOCK END


    # ALMOST EMPTY BLOCK START
    elif((sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) == 1) and ((message.content.startswith('/n '))or(message.content.startswith('/q '))or(message.content.startswith('/b2b0 '))or(message.content.startswith('/b2b1 '))or(message.content.startswith('/b2b2 '))or(message.content.startswith('/b2b3 '))or(message.content.startswith('/b2b4 '))or(message.content.startswith('/b2b5 '))or(message.content.startswith('/b2b6 '))or(message.content.startswith('/b2b7 '))or(message.content.startswith('/b2b8 '))or(message.content.startswith('/b2b9 ')))):
              
      print("Almost empty message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " sent a message with no alphabets" + "\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      reply2 = "  :)  "
      # bot.send_message(reply2, from_)
      await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
      await message.channel.send(reply2)
      print("Almost empty message block has finished working!")
    # ALMOST EMPTY END


    # ONE WORD BLOCK START
    # elif((sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) == 2)):
    elif((sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) == 2) and ((message.content.startswith('/n '))or(message.content.startswith('/q '))or(message.content.startswith('/b2b0 '))or(message.content.startswith('/b2b1 '))or(message.content.startswith('/b2b2 '))or(message.content.startswith('/b2b3 '))or(message.content.startswith('/b2b4 '))or(message.content.startswith('/b2b5 '))or(message.content.startswith('/b2b6 '))or(message.content.startswith('/b2b7 '))or(message.content.startswith('/b2b8 '))or(message.content.startswith('/b2b9 ')))):
    
              
      print("One word message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")
      print("Message was " + str(message.content))
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " sent a message with only one word\n\nIt was "+str(message.content) + "\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      line = message.content.split(' ', 1)[1]
      reply2 = str(line) + "!"
      # bot.send_message(reply2, from_)
      await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
      await message.channel.send(reply2)
      print("One word message block has finished working!")
    # ONE WORD BLOCK END


    # YOU ARE BLOCK START
    elif(((message.content.startswith('/n you are')) or (message.content.startswith('/n You are'))) and (sum(word.strip(string.punctuation).isalpha() for word in message.content.split()) < 7)):
              
      print("You are message block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")
      print("Message was " + str(message.content))
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " sent this message\n"+str(message.content) + "\nand the reply sent is\n\nHaha! You bet! :)"+"\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      reply2 = "Haha! You bet!  :)"
      # bot.send_message(reply2, from_)
      await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
      await message.channel.send(reply2)
      print("You are message block has finished working!")
    # YOU ARE BLOCK END


    # NORMAL BLOCK
    elif (message.content.startswith('/n') or message.content.startswith('/N') or message.content.startswith('\\n') or message.content.startswith('\\N')):
      print("\nNormal block activated")
      nottalking = 1
      person = message.author
      print(str(person) + " tried to use it")

      syntax_error = 0

      act_q = ''
      fin_q = ''
      reply2 = ''

      list_mess = re.findall('/n (.+)', str(message.content))
      strings = [str(sen) for sen in list_mess]
              
      if (len(strings) > 0): #There is a sentence 
        act_q = str("".join(strings))
        if (act_q.startswith('\\') or act_q.startswith('/')): #Two commands error
          syntax_error = 1
          error_message = "Please don't use two commands at the same time!"
          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used two commands at once" + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")
            # await message.channel.send(tellgod)
          await message.channel.send(error_message)

        else: #Two commands error handled
          fin_q = act_q 
          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used the normal block correctly\n\nThe message was\n\n"+str(fin_q) + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await message.channel.send(tellgod)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

          # await message.channel.send(make_reply_qa(str(fin_q), str(person)))
          if (fin_q.startswith('What') or fin_q.startswith('what') or fin_q.startswith('Who') or fin_q.startswith('who') or fin_q.startswith('Why') or fin_q.startswith('why') or fin_q.startswith('When') or fin_q.startswith('when') or fin_q.startswith('How') or fin_q.startswith('how') or fin_q.endswith('?') or fin_q.endswith(' m') or fin_q.startswith(' M') or fin_q.startswith('Do you ') or fin_q.startswith('do you')):
            error_message = "You might want to enter QUESTION mode for this.\nType /help or /question to know more.\nCurrently, this message is being processed in NORMAL mode."
            # bot.send_message(error_message, from_)
            await message.channel.send(error_message)

          reply2 = make_reply(fin_q, str(person))
          # bot.send_message(reply2, from_)
          await message.channel.send("REPLYING TO:\n\"" + str(message.content)+"\"\n__ __ __ __ __ __ __ __ __\n")
          await message.channel.send(reply2)

          if (str(person) in exceptions):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used the normal block correctly\n\nThe reply sent is\n\n"+str(reply2) + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            # await message.channel.send(tellgod)
            # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
            await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")


      else: #There was no sentence
        syntax_error = 1
        error_message = "SYNTAX ERROR - Format should be:-\n /n\nand then a space, and then your question.\n\nIn /n, the \'n\' should not be capital."
        await message.channel.send(error_message)

                
        if (str(person) in exceptions):
          pass
        else:
          tellgod = "___________________\n\n" + str(person) + " is making a syntax error in normal block" + "\n\n___________________"
          # bot.send_message(tellgod, 967745126)
          # await message.channel.send(tellgod)
          # await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+ "\nChannel : "+str(message.channel)+"\n"+tellgod+"\n_______________________________")
          await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

              
      if (syntax_error == 1):
        print("User is making a syntax error!")

             
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the normal block\n\nThe message was\n\n"+str(message.content) + "\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")


      
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " used the normal block\n\nThe reply sent is\n\n"+str(reply2) + "\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")

      print("Normal block has finished working!")
    # NORMAL BLOCK END


    # WEIRD COMMAND START
    elif(message.content.startswith('\\') or message.content.startswith('/')):
      print("Command error block activated\n")
      person = message.author
      print(str(person) + " tried to use it")
              
      if (str(person) in exceptions):
        pass
      else:
        tellgod = "___________________\n\n" + str(person) + " is using an invalid command" + "\n\n___________________"
        # bot.send_message(tellgod, 967745126)
        await client.guilds[botlogs].text_channels[0].send('_______________________________\nReceived a message from '+ str(message.author)+"\nGuild : "+str(message.guild) +"\nChannel : "+str(message.channel)+"\n"+str(tellgod)+"\n_______________________________")


      error_message = "This is not a valid command. Please type /help for help"
      # bot.send_message(error_message, from_)
      await message.channel.send(error_message)
      print("User is making a command error!")
      print("Command error block has finished working!\n")
    # WEIRD COMMAND END



    # NOT TALKING START
    else:
      print("Not talking!")
      # global nottalking
      nottalking = (nottalking) + 1

      if((nottalking)%50 == 0):
        warning_message = "Hey include me in the conversation! Please type /help for help on how to talk to me :)"
        # bot.send_message(error_message, from_)
        await message.channel.send(warning_message)
    # NOT TALKING END


# NORMAL MESSAGES END 
    
client.run(DISCORD_TOKEN)