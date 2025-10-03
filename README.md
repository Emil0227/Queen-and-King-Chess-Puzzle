# Queen and King Chess Puzzle
A Python-based chess variant where only the **Queen** and **King** are in play.  
This project was developed as part of my MSc Computer Science coursework at the University of London.  

## Project Overview
- Implements a simplified chess game with **customizable board sizes** (3×3 up to 26×26).  
- Supports **multiple queens per side** while enforcing traditional chess rules for movement, check, checkmate, and stalemate.  
- Features an **interactive console interface**: player plays as White, and the computer generates Black’s moves.  

## Key Features
- **Game Engine**
  - Validates board configurations from file input.
  - Handles moves according to chess rules with real-time feedback.
  - Detects check, checkmate, and stalemate conditions.
- **AI Opponent**
  - Automatically generates valid moves for Black.
  - Introduces randomness to avoid predictability.
- **Board Visualization**
  - Displays game state using Unicode chess symbols ♔♕♚♛.
  - Saves/loads game states in a simple text format.
- **Testing**
  - Comprehensive **pytest** unit tests with >5 test cases per function.
  - Verified correctness of move validation, board state management, and game termination logic.

## Skills Demonstrated
- Object-Oriented Programming in Python (class design for `King`, `Queen`, `Board`).  
- Algorithmic problem solving (path checking, rule validation, AI move generation).  
- Software engineering practices:
  - Modular code design
  - Unit testing with **pytest**
  - Git-based version control with frequent, descriptive commits  

## Project Structure
```text
├── chess_puzzle.py # Core implementation
├── test_chess_puzzle.py # Unit tests
├── board_examp.txt # Example board configuration
└── README.md # Project documentation
```

## How to Run
```bash
# Run the game
python chess_puzzle.py

# Run all tests
pytest test_chess_puzzle.py
```

## Example Gameplay
```
File name for initial configuration: board_examp.txt
The initial configuration is:

  ♔  
   ♕ 
 ♚  ♛
     
  ♕

Next move of White: c3c4
The configuration after White's move is:

   ♔ 
   ♕ 
 ♚  ♛
     
  ♕  
