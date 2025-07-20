def chatbot():
    print("Hi! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing fine!")
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
