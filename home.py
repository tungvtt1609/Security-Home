import telepot
import RPi.GPIO as GPIO
import time
import datetime
from telepot.loop import MessageLoop

PIR    = 17

GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)

motion = 0
motionNew = 0
 
def handle(msg):
    global telegramText
    global chat_id
  
    chat_id = msg['chat']['id']
    telegramText = msg['text']
  
    print('Message received from ' + str(chat_id))
  
    if telegramText == '/start':
        bot.sendMessage(chat_id, 'Welcome to House Notification')

    while True:
        main()
    
           

bot = telepot.Bot('Your Token Here')
bot.message_loop(handle)		

def main():
	    
    global chat_id
    global motion 
    global motionNew
    
    if GPIO.input(PIR) == 1:
        print("Motion detected")
        motion = 1
        if motionNew != motion:
            motionNew = motion
            sendNotification(motion)
            
            
    elif GPIO.input(PIR) == 0:
        print("No motion detected")
        motion = 0
        if motionNew != motion:
            sendNotification(motion)
            motionNew = motion


def sendNotification(motion):   

    global chat_id
    
    if motion == 1:
        bot.sendMessage(chat_id, 'Someone is at your front door')
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

    elif motion == 0:
        bot.sendMessage(chat_id, 'Nobody is at your front door')

while 1:
    time.sleep(10)  