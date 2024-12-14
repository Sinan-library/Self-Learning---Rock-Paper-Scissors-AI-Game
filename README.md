
# **Self Learning - Rock-Paper-Scissors AI Game**

## **Overview**
This project implements a self-learning Rock-Paper-Scissors game using two AI strategies:

1. **Markov Chain-Based Prediction** (Basic AI)
2. **Machine Learning Model (Random Forest Classifier)** (Advanced AI)

The AI learns from user gameplay patterns and improves its predictions, aiming to beat the user by anticipating future moves.

---

## **Features**
- Tracks user moves across game sessions.
- Implements two AI models:
  - Markov Chain-based prediction.
  - Random Forest Classifier-based prediction using scikit-learn.
- Persistent data storage with `user_moves.json`.
- Adaptive gameplay with improving AI performance.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors-ai.git
   ```

2. Navigate to the project folder:
   ```bash
   cd rock-paper-scissors-ai
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:
   ```bash
   python rock_paper_scissors_ai.py
   ```

---

## **Game Instructions**
- Enter your move: `rock`, `paper`, or `scissors`.
- The AI will choose its move based on the implemented prediction model.
- The winner is announced after each round.
- The game continues until you choose to quit.

---

## **Technical Details**

### **1. Markov Chain-Based Model (Basic AI)**
- Analyzes past user moves to create a transition matrix.
- Predicts the next user move based on historical probabilities.
- Chooses a move that beats the predicted move.

### **2. Machine Learning Model (Advanced AI)**
- Uses the `RandomForestClassifier` from scikit-learn.
- Encodes moves as integers (`rock: 0, paper: 1, scissors: 2`).
- Trains on historical data (`user_moves.json`).
- Predicts the next user move and selects a counter-move.

---

## **Dependencies**
- Python 3.x
- scikit-learn
- NumPy
- JSON (standard library)

---

## **How to Contribute**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.

---

## **License**
This project is licensed under the MIT License.

---

<p align="center"><strong>Developed with ❤️ by Sinan Bandi</strong></p> 
