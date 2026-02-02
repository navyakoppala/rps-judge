import random
from pathlib import Path


# Load prompts

BASE_DIR = Path(__file__).parent
SYSTEM_PROMPT = (BASE_DIR / "Prompts" / "system_prompt.txt").read_text()
INSTRUCTION_PROMPT = (BASE_DIR / "Prompts" / "instruction_prompt.txt").read_text()


# Minimal game state (AI-readable)

state = {
    "round": 1,
    "user_bomb_used": False
}

BOT_MOVES = ["rock", "paper", "scissors", "bomb"]


# AI Judge (prompt-driven)

def call_ai_judge(user_input, bot_move, state):
    """
    This function represents the AI Judge.
    All decision-making is delegated to the AI via prompts.
    The code does NOT apply any game rules.
    """

    full_prompt = f"""
{SYSTEM_PROMPT}

{INSTRUCTION_PROMPT}

Current State:
- Round: {state['round']}
- User bomb already used: {state['user_bomb_used']}

User input:
"{user_input}"

Bot move:
"{bot_move}"

Respond ONLY in the following format:

Round: <number>
User Move: <interpreted move or raw input>
Bot Move: <bot move>
Move Status: <VALID | INVALID | UNCLEAR>
Winner: <User | Bot | Draw | None>
Explanation: <clear reasoning>
"""

    
    # Placeholder AI response
    # (Replace with Gemini / LLM call later)
    
    return f"""
Round: {state['round']}
User Move: {user_input}
Bot Move: {bot_move}
Move Status: (AI decides)
Winner: (AI decides)
Explanation: The AI Judge evaluates the user's intent, applies the rules from the prompt, and produces this decision.
"""


# Game loop (glue only)

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

    # State update happens ONLY after AI response
    if "User Move: bomb" in ai_response:
        state["user_bomb_used"] = True

    state["round"] += 1
