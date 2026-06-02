import requests

class OllamaBrain:
    def __init__(self, model="gemma3:4b"):
        self.model = model

    def think(self, user_input):
        return "ollama brain online"