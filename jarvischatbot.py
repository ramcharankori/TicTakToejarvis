import re
import tkinter as tk
import random

class JarvisChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS Chatbot")

        self.chat_log = tk.Text(root)
        self.chat_log.pack(padx=10, pady=10)

        self.user_input = tk.Entry(root)
        self.user_input.pack(padx=10, pady=5)
        self.user_input.bind("<Key>", self.user_typing)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.clear_button = tk.Button(root, text="Clear Chat", command=self.clear_chat)
        self.clear_button.pack()

        self.rules = [
            (r"(hello|hi).*", "Hello! How can I assist you?"),
            (r"how are you.*", "I'm just a chatbot, but I'm here to help!"),
            (r"what is your name.*", "I'm a chatbot. You can call me JARVIS."),
            (r"bye|goodbye", "Goodbye! Have a great day!"),
            (r"tell me a joke", random.choice(["Why don't scientists trust atoms? Because they make up everything!", "I'm reading a book on anti-gravity. It's impossible to put down!"])),
            (r"call me (.*)", "Sure thing! I'll call you {} from now on."),
            (r".*", "I'm sorry, I didn't understand that."),
            (r"how old are you.*", "I'm a computer program, so I don't have an age."),
        ]

        self.user_name = "user"
        self.add_initial_greeting()

    def add_initial_greeting(self):
        initial_greeting = f"JARVIS: Hello! How can I assist you, {self.user_name}? Type 'bye' to exit.\n"
        self.chat_log.insert(tk.END, initial_greeting)

    def user_typing(self, event):
        self.chat_log.insert(tk.END, "User is typing...\n")

    def clear_chat(self):
        self.chat_log.delete(1.0, tk.END)

    def send_message(self):
        user_input = self.user_input.get()
        self.chat_log.insert(tk.END, f"You: {user_input}\n")

        if user_input.lower() == 'bye':
            self.chat_log.insert(tk.END, "JARVIS: Goodbye!\n")
            self.root.after(1000, self.root.destroy)
        else:
            response = self.chatbot_response(user_input)
            self.chat_log.insert(tk.END, f"JARVIS: {response}\n")

        self.user_input.delete(0, tk.END)

    def chatbot_response(self, user_input):
        for pattern, response in self.rules:
            if re.match(pattern, user_input, re.IGNORECASE):
                if callable(response):
                    return response()
                elif isinstance(response, list):
                    return random.choice(response)
                elif "{}" in response:
                    self.user_name = re.match(pattern, user_input, re.IGNORECASE).group(1)
                    return response.format(self.user_name)
                return response
        return self.rules[-1][1]

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisChatbotGUI(root)
    root.mainloop()
