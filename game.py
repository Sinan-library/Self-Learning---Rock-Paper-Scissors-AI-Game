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

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Get user input
def get_user_move():
    while True:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        if move in MOVES:
            return move
        print("Invalid move. Try again.")

# Determine winner
def determine_winner(user_move, ai_move):
    if user_move == ai_move:
        return "tie"
    if (user_move == "rock" and ai_move == "scissors") or \
       (user_move == "scissors" and ai_move == "paper") or \
       (user_move == "paper" and ai_move == "rock"):
        return "user"
    return "ai"

# Predict AI move using Markov Chain
def predict_ai_move(history):
    if len(history) < 2:
        return random.choice(MOVES)
    transitions = {move: {next_move: 0 for next_move in MOVES} for move in MOVES}
    for i in range(len(history) - 1):
        current_move = history[i]
        next_move = history[i + 1]
        transitions[current_move][next_move] += 1
    last_move = history[-1]
    predicted_move = max(transitions[last_move], key=transitions[last_move].get)
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[predicted_move]

# Game loop
def play_game():
    data = load_data()
    while True:
        user_move = get_user_move()
        data["history"].append(user_move)
        ai_move = predict_ai_move(data["history"])
        print(f"AI chose: {ai_move}")
        winner = determine_winner(user_move, ai_move)
        print(f"Result: {winner.capitalize()} wins!\n")
        save_data(data)
        if input("Play again? (yes/no): ").lower() != "yes":
            break

play_game()
