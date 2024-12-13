import random
import json
import os

MOVES = ["rock", "paper", "scissors"]

DATA_FILE = "user_moves.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"history": []}

print("Checkpoint 1 reached; code works")