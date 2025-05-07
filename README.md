# TalkFashion - The programming language that helps you stay in style!

A domain-specific language (DSL) for generating outfit suggestions based on  
user-provided clothing items and event type.

Created by Melanie Vaknin

## Overview

**TalkFashion** is a personal styling language designed for use in virtual wardrobe assistants and event planning tools.  
It simplifies the process of choosing appropriate outfits by matching clothes with the right occasions using simple, human-readable code.

Whether you’re dressing for a formal event, a casual outing, or a business meeting, TalkFashion helps you plan the perfect outfit from your own closet items.

### Key Features

- **Easy input system** to collect clothing items from the user
- **Conditional logic** to suggest outfits based on event type
- **Custom function support** for styling logic
- **Built-in outfit recommendation printing**
- **Simple, beginner-friendly syntax** for non-programmers

## Installation

### Prerequisites

- Python 3.8 or higher
- textX (for language parsing)

### Setup

1. Clone the repository:
2. 
git clone https://github.com/melanievaknin/talkfashion-language.git

3. Navigate to the project directory:

cd talkfashion-language

3. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

4. Run an example program:
python run_talkfashion.py examples/sample_outfit.talk

shell
Copy
Edit

## Language Syntax

### Variables

var top: String = input("Enter your top: ");
var bottom: String = input("Enter your bottom: ");
var event: String = input("What's the event?");

shell
Copy
Edit

### Control Structures

if (event == "party") {
suggest outfit top + bottom + "heels" for event;
} else {
suggest outfit top + bottom + "sneakers" for event;
}

shell
Copy
Edit

### Functions

func planOutfit(event: String, items: List<String>) -> Outfit {
return "For " + event + ", wear: " + items[0] + ", " + items[1] + ", and " + items[2];
}

shell
Copy
Edit

## Example Programs

### Hello World

// Hello World in TalkFashion
func main() {
print("Welcome to TalkFashion!");
}

main();

shell
Copy
Edit

### Outfit Suggestion Based on Input

// Basic outfit planner
func main() {
var top: String = input("Enter top:");
var bottom: String = input("Enter bottom:");
var shoes: String = input("Enter shoes:");
var event: String = input("Enter event:");

csharp
Copy
Edit
if (event == "business") {
    suggest outfit top + bottom + shoes for event;
} else {
    suggest outfit "jeans + t-shirt + sneakers" for "casual day";
}
}

main();

shell
Copy
Edit

### Function-Based Planner

// Outfit suggestion using a function
func main() {
var event: String = input("Event type:");
var items = collectClosetItems();
var suggestion = planOutfit(event, items);
print(suggestion);
}

main();

shell
Copy
Edit

## Project Structure

talkfashion-language/
├── examples/ # Example TalkFashion programs
│ ├── hello_world.talk
│ ├── sample_outfit.talk
├── src/
│ ├── talkfashion_grammar.py # textX grammar
│ └── talkfashion_interpreter.py # Interpreter logic
├── run_talkfashion.py # Runner script
├── README.md
└── requirements.txt

markdown
Copy
Edit

## Implementation Details

The TalkFashion language is built with:

1. **textX** to define the DSL grammar and parse user programs
2. **Python** to handle interpretation and output
3. A custom **AST-based interpreter** that simulates fashion advice logic

## License

This project is provided for educational and creative use under the MIT License.

## Acknowledgments

- Special thanks to the `textX` team for enabling easy DSL creation
- Inspired by real-world fashion apps and virtual wardrobe systems
