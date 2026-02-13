#!/usr/bin/env python3
import json
import random
import os
import sys

DECK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decks")

def load_deck(name):
    path = os.path.join(DECK_DIR, f"{name}.json")
    if not os.path.exists(path):
        print(f"Deck '{name}' not found.")
        return []
    with open(path, "r") as f:
        return json.load(f)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    if len(sys.argv) < 2:
        print("Usage: ./study.py <deck_name>")
        decks = [f.replace(".json", "") for f in os.listdir(DECK_DIR) if f.endswith(".json")]
        print(f"Available decks: {', '.join(decks)}")
        return

    deck_name = sys.argv[1]
    cards = load_deck(deck_name)
    if not cards:
        return

    random.shuffle(cards)
    print(f"Loaded {len(cards)} cards from '{deck_name}'. Enter answer, 'q' to quit.")

    for i, card in enumerate(cards, 1):
        input("\nPress Enter for next card...")
        clear()
        print(f"Card {i}/{len(cards)} [{', '.join(card.get('tags', []))}]")
        print("-" * 40)
        print(f"Q: {card['question']}")
        print("-" * 40)
        
        user_ans = input("Your Answer: ").strip()
        if user_ans.lower() == 'q':
            break

        correct_ans = card['answer'].strip()
        
        # Check strict equality (case-sensitive? CLI commands usually are, but maybe relax for concepts)
        is_correct = user_ans == correct_ans

        print("-" * 40)
        if is_correct:
            print(f"\033[92mCORRECT!\033[0m")
            print(f"Your Answer: \033[92m{user_ans}\033[0m")
        else:
            print(f"\033[91mWRONG!\033[0m")
            print(f"Your Answer:    \033[91m{user_ans}\033[0m")
            print(f"Correct Answer: \033[92m{correct_ans}\033[0m")

        if 'explanation' in card:
            print(f"\nExplanation: {card['explanation']}")
        print("-" * 40)

    print("\nSession complete.")

if __name__ == "__main__":
    main()
