# Task 4: Basic Rule-Based Chatbot

def get_response(user_input):
    """Returns a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! 👋 How can I help you?"

    elif user_input in ["how are you", "how are you?", "how r you"]:
        return "I'm fine, thanks! 😊 How about you?"

    elif user_input in ["good", "i am fine", "i'm fine", "fine", "great"]:
        return "That's great to hear! 😄"

    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I'm ChatBot 🤖, your simple Python assistant!"

    elif user_input in ["what can you do", "help", "help me"]:
        return "I can chat with you! Try saying hello, asking how I am, or say bye 😊"

    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Hmm, I didn't understand that. Try saying 'hello', 'how are you', or 'bye'."


def run_chatbot():
    """Main loop to run the chatbot."""
    print("=" * 40)
    print("       Welcome to ChatBot 🤖")
    print("  Type 'bye' or 'quit' to exit")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("ChatBot: Please say something! 😊")
            continue

        response = get_response(user_input)
        print(f"ChatBot: {response}")

        # Exit condition
        if user_input.lower() in ["bye", "goodbye", "see you", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()
