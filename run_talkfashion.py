"""
TalkFashion Language Runner
Usage: python run_talkfashion.py <program_file.talk>
"""

import sys
import os
from src.talkfashion_interpreter import run_talkfashion_program

def main():
    programs_dir = os.path.join(os.path.dirname(__file__), 'programs')

    if len(sys.argv) < 2:
        print("TalkFashion Language Runner")
        print("Usage: python run_talkfashion.py <program_file.talk> or select a number:")
        print("\nAvailable example programs:")

        examples = [f for f in os.listdir(programs_dir) if f.endswith('.talk')]
        for i, example in enumerate(examples, 1):
            print(f"{i}. {example}")
        print(f"{len(examples)+1}. Run All Programs")

        choice = input("\nEnter the number of the example to run (or press Enter to exit): ")

        if not choice:
            return

        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(examples):
                program_file = os.path.join(programs_dir, examples[choice_num - 1])
                print(f"\nRunning: {examples[choice_num - 1]}\n")
                run_talkfashion_program(program_file)
            elif choice_num == len(examples) + 1:
                for program in examples:
                    print(f"\n=== Running {program} ===\n")
                    run_talkfashion_program(os.path.join(programs_dir, program))
                    print("\n===========================\n")
            else:
                print("Invalid choice.")
        else:
            print("Invalid input.")
    else:
        program_file = sys.argv[1]
        if not os.path.exists(program_file):
            print(f"Error: File '{program_file}' does not exist.")
            return
        run_talkfashion_program(program_file)

if __name__ == "__main__":
    main()
