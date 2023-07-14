import telepot

token = '5024533416:AAEwgEVZpjeglNWkQMTVbjmXXi9N_M2Afgw'
id = -794824552
telegrammBot = telepot.Bot(token)

def send_message(text):
    telegrammBot.sendMessage(id,text,parse_mode='Markdown')