import pyttsx3                                   # python text to speech library
# import threading
import json
import random


engine = pyttsx3.init()                          # initialize the engine as pyttsx3
delay = 1                                        # delay for tts
engine.setProperty('rate', 150)                  # speed delay for next tts

engine.say("Hello I am your asssistant")            # test case tts
print("Hello I am your assistant")                 # print case tts

engine.runAndWait()                               # run and wait for next tts

greet = ["What can I do for you?", "How are you?", "Do you need any help?", "How can I assist you today?"]
response = random.choice(greet)
engine.say(response)
print(response)
engine.runAndWait()

# engine.say("I am waiting for your command")
# print("I am waiting for your command")

# define json_file with their path(file location) which contain responses.
json_file= "C:\\Users\\DELL\\OneDrive\\Desktop\\Project\\responses.json"
# def responses from .json file to load responses
def load_responses():                  # also here we define default responses in case .json not work or unable to fetch file patch

    with open(json_file,"r") as file:            # open file_json in "r" read mood 
        return json.load(file)


def time():                                 # define time function
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def date():                                 # define date function
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d") 

def day():                                  # define day function
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%A")


def arithmatic_operation(operation, num1, num2):          # define arithmatic operation
    
    if operation in ["addition", "+", "sum"]:
        return num1 + num2
    elif operation in ["subtraction", "-", "minus"]: 
        return num1 - num2
    elif operation in ["multiplication", "*", "multiply"]:
        return num1 * num2
    elif operation in ["division", "/", "divide"]:
        return num1 / num2
    elif operation in ["modulus", "%", "mod"]:
        return num1 % num2
    else:
        return "I'm not sure how to respond."


def chatbot():
    responses=load_responses()

    while True:
        user_input=input("You: ").lower()
        if user_input in ["bye", "exit"]:
            print("Chatbot: Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break
        
        elif user_input=="time":
            print(f"chatbot: The current time is {time()}")
            engine.say(f"The current time is {time()}")
            engine.runAndWait()

        elif user_input=="date":
            print(f"chatbot: The current date is {date()}")
            engine.say(f"The current date is {date()}")
            engine.runAndWait()
            
        elif user_input=="day":
            print(f"chatbot: The current day is {day()}")
            engine.say(f"The current day is {day()}")
            engine.runAndWait()        



        elif user_input in ["addition", "+", "subtraction", "-", "multiplication", "*", "division", "/", "modulus", "%"]:
            if user_input in ["addition", "+", "add"]:
                print("chatbot: Ok you want to do addition.")
                engine.say("Ok you want to do addition.")
                engine.runAndWait()
            elif user_input in ["subtraction", "-", " minus"]:
                print("chatbot: Ok you want to do subtraction.")
                engine.say("Ok you want to do subtraction.")
                engine.runAndWait()
            elif user_input in ["multiplication", "*", "multiply"]:
                print("chatbot: Ok you want to do multiplication.")
                engine.say("Ok you want to do multiplication.")
                engine.runAndWait()
            elif user_input in ["division", "/", "divide"]:
                print("chatbot: Ok you want to do division.")
                engine.say("Ok you want to do division.")
                engine.runAndWait()
            elif user_input in ["modulus", "%","mod"]:
                print("chatbot: Ok you want to do modulus.")
                engine.say("Ok you want to do modulus.")
                engine.runAndWait()
                
             
            engine.say("enter first number: ")
            engine.runAndWait()
            num1=float(input("enter first number: "))
            engine.say("enter second number: ")
            engine.runAndWait()
            num2=float(input("enter second number: "))
            engine.runAndWait() 
            
            result=arithmatic_operation(user_input, num1, num2)
            print(f"chatbot: {result}") 
            engine.say(result)
            engine.runAndWait()

            print("anything else?")
            engine.say("anything else?")
            engine.runAndWait()

        else:
            response=random.choice(responses.get(user_input,["I'm not sure how to respond."]))  
            print(f"chatbot: {response}")
            engine.say(response)
            engine.runAndWait()

       

delay = 1                                        # delay for next tts
engine.setProperty('rate', 150)                  # speed delay for next tts

chatbot()



# engine.say("I am waiting for your command")
# def speak_and_print(text):
#     engine.say(text)
#     print(text)

# texts = [
#     "Hello I am your assistant",
#     "What can I do for you?",
#     "I am waiting for your command"
# ]

# threads = []
# for text in texts:
#     thread = threading.Thread(target=speak_and_print, args=(text,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

