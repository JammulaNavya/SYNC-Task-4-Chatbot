import datetime
import random

# Define the rule-based chatbot function
def rule_based_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help!"
    elif "goodbye" in user_input:
        return "Goodbye! Feel free to return if you have more questions."
    elif "name" in user_input:
        return "I'm a chatbot, and you can call me ChatBot."
    elif "age" in user_input:
        return "I don't have an age; I'm just a computer program."
    elif "help" in user_input:
        return "Sure, I can help with various questions. Just ask!"
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    elif "time" in user_input:
        # Access the real-time time using the datetime module
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is {current_time}."
    elif "weather" in user_input:
        return "I'm sorry, I don't have access to weather information."
    elif "joke" in user_input:
        jokes = [
            "Why was the math book sad? Because it had too many problems!",
            "Why can't a bike stand on its own? Because it's two tired!",
            "Why are the cricket stadiums so cool? Because every seat has a fan in it!",
            "Why do fish live in salt water? Because pepper water makes them sneeze.",
            "Why was 6 afraid of 7? Because 7 ate 9!"
        ]
        return random.choice(jokes)
    else:
        return "I'm sorry, I don't understand that. Please ask another question."

# Main chat loop
while True:
    user_input = input("You: ")
    response = rule_based_chatbot(user_input)
    print("Chatbot:", response)

    # Add an exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
