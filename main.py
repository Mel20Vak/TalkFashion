from textx import metamodel_from_file
import os

def suggest_outfit(top, bottom, shoes, event):
    print("\n--- OUTFIT SUGGESTION ---")
    print(f"Event Type: {event}")
    print(f"Top: {top}")
    print(f"Bottom: {bottom}")
    print(f"Shoes: {shoes}")

    if event.lower() == "business":
        print("Style Match: Professional")
        print("Tip: Consider a blazer or neutral colors.")
    elif event.lower() == "party":
        print("Style Match: Trendy & Bold")
        print("Tip: Add accessories or statement colors!")
    elif event.lower() == "casual":
        print("Style Match: Comfortable & Relaxed")
        print("Tip: Sneakers and soft fabrics work best.")
    else:
        print("Style Match: Mixed")
        print("Tip: Dress according to your comfort and confidence!")

def run_program(file_path):
    grammar_file = os.path.join(os.path.dirname(__file__), '..', 'grammar', 'talkfashion.tx')
    mm = metamodel_from_file(grammar_file)
    model = mm.model_from_file(file_path)

    outfits = {}
    for stmt in model.statements:
        if stmt.__class__.__name__ == "UserOutfit":
            outfits[stmt.name] = stmt
        elif stmt.__class__.__name__ == "Suggest":
            outfit = outfits.get(stmt.name)
            if outfit:
                suggest_outfit(
                    outfit.top.strip('"'),
                    outfit.bottom.strip('"'),
                    outfit.shoes.strip('"'),
                    outfit.event.strip('"')
                )

if __name__ == '__main__':
    print("Choose an option:")
    print("1 - Run example from file")
    print("2 - Enter custom outfit input")
    choice = input("Enter number: ")

    if choice == "1":
        print("Choose an example:")
        print("1 - Basic Outfit")
        print("2 - Party Look")
        print("3 - Business Style")
        file_choice = input("Enter example number: ")

        example_files = {
            "1": os.path.join(os.path.dirname(__file__), '..', 'programs', 'basic_outfit.talk'),
            "2": os.path.join(os.path.dirname(__file__), '..', 'programs', 'party_look.talk'),
            "3": os.path.join(os.path.dirname(__file__), '..', 'programs', 'business_style.talk'),
        }

        file_path = example_files.get(file_choice)
        if file_path and os.path.exists(file_path):
            run_program(file_path)
        else:
            print("Invalid choice or file not found.")

    elif choice == "2":
        print("Enter your outfit information:")
        top = input("Top: ")
        bottom = input("Bottom: ")
        shoes = input("Shoes: ")
        event = input("Event Type (e.g., casual, business, party): ")

        suggest_outfit(top, bottom, shoes, event)
    else:
        print("Invalid selection.")
