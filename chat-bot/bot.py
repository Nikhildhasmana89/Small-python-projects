print("Hello, I am your chatbot!")

#chatbot memory 
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm functioning as expected!",
    "what is your name": "I am a simple chatbot created to assist you.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "bye": "Goodbye! Have a great day!"
}

#functions

def getResponse(userInput):
    userInput = userInput.lower()
    for eachkey in responses:
        if eachkey in userInput:
            return responses[eachkey]
        
    return "I'm sorry, I don't understand that."

#user input
while True:
    userInput = input("please ask me a question: ")
    reply = getResponse(userInput)

    print("Chatbot: " + reply)

    if "bye" in userInput.lower():
        break