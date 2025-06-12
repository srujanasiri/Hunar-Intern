print("Hi !I'm chatbot. Type'bye' to exit.\n")
while True:
    user_input=input("You:").lower()
    if user_input=="bye":
        print("chatbot: Goodbye! Have a nice day")
        break
    elif user_input in["hi","hello","hey"]:
        print("chatbot: Hello! How can I help you?")
    elif "time" in user_input:
        print("chatbot:sorry, I can't check the time right now.")
    elif "your name" in user_input:
        print("chatbot: I'm a simple chatbot created by python.")
    elif "how are you" in user_input:
        print("chatbot: I'm just a program, but I'm doing great!")
    elif "weather" in user_input:
        print("chatbot: I can't check the weather,but I hope it's sunny!")
    elif "thank" in user_input:
        print("chatbot: IYou're welcome! I'm glad its helps you!")
    elif "help" in user_input:
        print("chatbot: you ask me about my name,time,weather,or just hi!")
    elif "sad" in user_input or "not good" in user_input:
        print("chatbot: I'm sorry to hear that. Ihope things are better soon.")
    elif "happy" in user_input or "good" in user_input:
        print("chatbot: That's great to hear!")
    elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
        try:
            result = eval(user_input)
            print(f"chatbot: The answer is {result}")
        except:
            print("chatbot: sorry, I couldn't calculate that.")
    else:
        print("chatbot: I'm not sure how to respond to that.")

