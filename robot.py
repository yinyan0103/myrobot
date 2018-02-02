from wxpy import *

bot = Bot()

@bot.register(msg_types=FRIENDS)
def auto_accept_friedns(msg):
    new_friend = msg.card.accept()
    new_friend.send('You have already being my friednds,we can start chat!')
    

