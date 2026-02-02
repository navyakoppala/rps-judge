import random
from pathlib import Path

# ----------------------------
# Load prompts (for evaluation)
# ----------------------------
BASE_DIR = Path(__file__).parent
SYSTEM_PROMPT = (BASE_DIR / "Prompts" / "system_prompt.txt").read_text()
INSTRUCTION_PROMPT = (BASE_DIR / "Prompts" / "instruction_prompt.txt").read_text()

# ----------------------------
# Minimal state
# ----------------------------
state = {
    "round": 1,
    "user_bomb_used": False
}

BOT_MOVES = ["rock", "paper", "scissors", "bomb"]

# ----------------------------
# AI Judge placeholder
# ----------------------------
def call_ai_judge(user_input, bot_move, state):
    """
    Placeholder for AI Judge.
    The real AI (LLM) would populate these fields.
    """
    return f"""
Round: {state['round']}
User Move: {user_input}
Bot Move: {bot_move}
Move Status: (AI decides)   # VALID / INVALID / UNCLEAR
Winner: (AI decides)        # User / Bot / Draw / None
Explanation: The AI Judge evaluates the move using the provided rules and returns a structured decision.
"""

# ----------------------------
# Game loop (glue only)
# ----------------------------
print("=== Rock Paper Scissors Plus (AI Judge) ===")
print("Type quit to exit\n")

while True:
    user_input = input("Your move: ").strip()

    if user_input.lower() in ["quit", "exit", "q"]:
        print("\nGame ended.")
        break

    bot_move = random.choice(BOT_MOVES)

    ai_response = call_ai_judge(user_input, bot_move, state)

    print("\n--- AI JUDGE DECISION ---")
    print(ai_response)
    print("------------------------\n")

    state["round"] += 1
