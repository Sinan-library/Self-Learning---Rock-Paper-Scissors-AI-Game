import random
import json
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

MOVES = ["rock", "paper", "scissors"]
MOVE_TO_INT = {"rock": 0, "paper": 1, "scissors": 2}
INT_TO_MOVE = {0: "rock", 1: "paper", 2: "scissors"}

DATA_FILE = "user_moves.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"history": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_user_move():
    while True:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        if move in MOVES:
            return move
        print("Invalid move. Try again.")

def determine_winner(user_move, ai_move):
    if user_move == ai_move:
        return "tie"
    if (user_move == "rock" and ai_move == "scissors") or \
       (user_move == "scissors" and ai_move == "paper") or \
       (user_move == "paper" and ai_move == "rock"):
        return "user"
    return "ai"

def train_model(history):
    if len(history) < 5:
        return None
    X, y = [], []
    for i in range(len(history) - 1):
        X.append([MOVE_TO_INT[history[i]]])
        y.append(MOVE_TO_INT[history[i + 1]])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def predict_ai_move_ml(model, last_move):
    if model is None or last_move not in MOVE_TO_INT:
        return random.choice(MOVES)
    predicted_move_int = model.predict([[MOVE_TO_INT[last_move]]])[0]
    predicted_move = INT_TO_MOVE[predicted_move_int]
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[predicted_move]

def play_game():
    data = load_data()
    model = train_model(data["history"])
    while True:
        user_move = get_user_move()
        data["history"].append(user_move)
        model = train_model(data["history"])
        ai_move = predict_ai_move_ml(model, user_move)
        print(f"AI chose: {ai_move}")
        winner = determine_winner(user_move, ai_move)
        print(f"Result: {winner.capitalize()} wins!\n")
        save_data(data)
        if input("Play again? (yes/no): ").lower() != "yes":
            break

play_game()
