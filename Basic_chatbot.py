'''

TASK 1: Basic Chatbot

Goal: Build a simple rule-based chatbot.
Scope:
. Input from user like: "hello", "how are you", "bye".
. Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
Key Concepts Used: if-elif, functions, loops, input/output.

'''
import datetime

def chatbot():

    print("========================================")
    print("     Welcome Python ChatBot      ")
    print("     Type 'bye' or 'tata' to exit the chatBot      ")
    print("========================================")

    while True:
        message = input("\n You : ").lower().strip()

        if message == "hello" or message == "hi":
            print("Bot : Hi! Nice to meet you.")

        elif message == "how are you" or message == "how are you?":
            print("Bot : I'm fine, Thanks! How are you?")
        
        elif message == "i am also fine" or message == "i am also fine, Thanks For asking":
            print("Bot : Nice! Buddy, Always Be Happy 😊.")

        elif message == "what is your name" or message == "what is your name?":
            print("Bot : I am a Python ChatBot.")

        elif message == "date and time please":
            print(datetime.datetime.now())
        
        elif message == "bye" or message == 'tata':
            print("Bot : GoodBye! Have a nice day.")
            break

        else:
            print("Bot : Sorry, I can't understand that.")

chatbot()     