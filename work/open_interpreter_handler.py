import os
import pickle

import interpreter


class OpenInterpreterHandler:
    def __init__(self, model: str = "gpt-4"):
        interpreter.api_key = os.environ["OPENAI_API_KEY"]
        interpreter.auto_run = True
        interpreter.model = model
        self.messages = None
        
    def chat(self, prompt: str):
        self.messages = interpreter.chat(prompt, return_messages=True)

    def save_messages_history(self, filename: str="messages_history"):
        with open(f"temp/{filename}.pkl", "wb") as f:
            pickle.dump(self.messages, f)

    def load_messages_history(self, filename: str="messages_history"):
        with open(f"temp/{filename}.pkl", "rb") as f:
            self.messages = pickle.load(f)
        interpreter.load(self.messages)

    def clear_messages_history(self):
        interpreter.reset()