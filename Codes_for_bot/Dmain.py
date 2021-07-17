# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import re
import string
import internal_interaction_bot


# MAKE NORMAL REPLY START
def make_reply(msg, person):

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
def make_reply_qa(msg, person):
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








# BORING STUFF
DISCORD_TOKEN = "NzcxMzEzNTQ2Nzc5OTUxMTI0.X5qTtw.RjNeCD6RfpCM41HcRwI1N2OoDfI"
prefix = '/'
client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("bot is ready")
# BORING STUFF END


# COMMANDS
@client.command()
async def hello(ctx):
  await ctx.send('Command mode!')
# COMMANDS END


# NORMAL MESSAGES
@client.event
async def on_message(message):

  await client.process_commands(message)

  if(message.content.startswith(prefix)):
    return
  else:
    if message.author == client.user:
      return

    # FUN PART STARTS 
    if (message.content.startswith('/q') or message.content.startswith('/Q') or message.content.startswith('\q') or message.content.startswith('\Q')):
      person = message.author

      print("\nQA block activated")
      print(str(person) + " tried to use it")
      list_mess = re.findall('/q (.+)', message)
      strings = [str(sen) for sen in list_mess]
              
      if (len(strings) > 0): #There is a question 
        act_q = str("".join(strings))
        if (act_q.startswith('\\') or act_q.startswith('/')): #Two commands error
          syntax_error = 1
          error_message = "Please don't use two commands at the same time!"
          if (person == 'TangentTanmay#1223'):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used two commands at once" + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            await message.channel.send(tellgod)
            await message.channel.send(error_message)

        else: #Two commands error handled
          fin_q = "Q: " + act_q + " \n " + "A:"
          if (person == 'TangentTanmay#1223'):
            pass
          else:
            tellgod = "___________________\n\n" + str(person) + " used the question block correctly\n\nThe message was\n\n"+str(message) + "\n\n___________________"
            # bot.send_message(tellgod, 967745126)
            await message.channel.send(tellgod)

          await message.channel.send(make_reply_qa(message, person))
                  
      else: #There was no question
        syntax_error = 1
        error_message = "SYNTAX ERROR - Format should be:-\n /q\nand then a space, and then your question.\n\nIn /q, the \'q\' should not be capital."
        await message.channel.send(error_message)

                
        if (person == 'TangentTanmay#1223'):
          pass
        else:
          tellgod = "___________________\n\n" + str(person) + " is making a syntax error in Question block" + "\n\n___________________"
          # bot.send_message(tellgod, 967745126)
          await message.channel.send(tellgod)

              
      if (syntax_error == 1):
        print("User is making a syntax error!")
      print("QA block has finished working!\n")
      
# NORMAL MESSAGES END 
    
client.run(DISCORD_TOKEN)