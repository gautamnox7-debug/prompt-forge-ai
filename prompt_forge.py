"""
PromptForge AI - Interactive Prompt Engineering CLI
Author: Gautam Mishra (@gautamnox7-debug)
"""

import sys
import os

TEMPLATES = {
    "1": {
        "title": "Software Architect & Lead Engineer",
        "description": "Transforms high-level requirements into scalable system designs.",
        "prompt": (
            "You are an Elite Principal Software Architect. Your job is to analyze "
            "requirements and produce clean, modular, production-grade solutions. "
            "Always follow SOLID principles, specify edge cases, and provide clear code snippets."
        )
    },
    "2": {
        "title": "Autonomous Agent Tool-Use Chain",
        "description": "Guides LLMs through observation, reasoning, action, and verification loops.",
        "prompt": (
            "You are an Autonomous AI Agent. For every task, reason step-by-step: "
            "1. Analyze goal. 2. Formulate action plan. 3. Execute step. 4. Verify results. "
            "Never assume facts; always ground answers in evidence."
        )
    },
    "3": {
        "title": "Deterministic JSON Schema Enforcer",
        "description": "Forces the model to return pure, parseable JSON without chat fluff.",
        "prompt": (
            "You are an API Data Extractor. Your output MUST be strict, valid JSON conforming "
            "to the schema provided. Do not include markdown ticks, introductory greetings, "
            "or closing explanations. Output ONLY raw JSON."
        )
    },
    "4": {
        "title": "Root Cause Bug Hunter",
        "description": "Pinpoints tricky bugs from stack traces and logs.",
        "prompt": (
            "You are a Senior Debugging Specialist. Analyze the error log or buggy code provided. "
            "Identify: 1. Root Cause, 2. Failing Line/Condition, 3. The exact fix with diff, "
            "4. Unit test to prevent regression."
        )
    }
}

def display_banner():
    banner = r"""
  ____                            _ _____                     
 |  _ \ _ __ ___  _ __ ___  _ __ | |_   _|__  _ __ __ _  ___ 
 | |_) | '__/ _ \| '_ ` _ \| '_ \| | | |/ _ \| '__/ _` |/ _ \
 |  __/| | | (_) | | | | | | |_) | | | | (_) | | | (_| |  __/
 |_|   |_|  \___/|_| |_| |_| .__/|_| |_|\___/|_|  \__, |\___|
                           |_|                    |___/       
        ⚡ Prompt Engineering Toolkit by Gautam Mishra ⚡
    """
    print(banner)

def main():
    display_banner()
    while True:
        print("\nSelect a Prompt Engineering Template to Inspect & Export:")
        for key, item in TEMPLATES.items():
            print(f"  [{key}] {item['title']} - {item['description']}")
        print("  [q] Exit")

        choice = input("\nEnter choice (1-4 or q): ").strip()
        if choice.lower() == 'q':
            print("\nHappy Prompting! Exiting...")
            break

        if choice in TEMPLATES:
            selected = TEMPLATES[choice]
            print("\n" + "="*60)
            print(f"🔥 TEMPLATE: {selected['title']}")
            print("="*60)
            print(selected['prompt'])
            print("="*60)
            
            save = input("\nSave this prompt to a local file? (y/n): ").strip().lower()
            if save == 'y':
                filename = f"prompt_template_{choice}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(selected['prompt'])
                print(f"✅ Saved successfully to {filename}")
        else:
            print("❌ Invalid selection. Please choose 1, 2, 3, 4, or q.")

if __name__ == "__main__":
    main()
