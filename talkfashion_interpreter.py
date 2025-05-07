from textx import metamodel_from_file
import os

from src.talkfashion_grammar import talkfashion_metamodel  # Assuming grammar is in this module


class TalkFashionInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.return_value = None

    def interpret(self, program_file):
        model = talkfashion_metamodel.model_from_file(program_file)
        return self.execute_program(model)

    def execute_program(self, program):
        for statement in program.statements:
            self.execute_statement(statement)
        return self.variables

    def execute_statement(self, statement):
        if hasattr(statement, 'name') and hasattr(statement, 'type') and hasattr(statement, 'expression'):
            # Variable declaration
            value = self.evaluate_expression(statement.expression) if statement.expression else None
            self.variables[statement.name] = value
        elif hasattr(statement, 'name') and hasattr(statement, 'prompt'):
            # Input statement
            user_input = input(self.evaluate_expression(statement.prompt))
            self.variables[statement.name] = user_input
        elif hasattr(statement, 'expression') and type(statement).__name__ == 'PrintStatement':
            print(self.evaluate_expression(statement.expression))
        elif hasattr(statement, 'condition') and hasattr(statement, 'thenBlock'):
            # If statement
            condition_result = self.evaluate_expression(statement.condition)
            if condition_result:
                self.execute_statement(statement.thenBlock)
            elif hasattr(statement, 'elseBlock'):
                self.execute_statement(statement.elseBlock)
        elif hasattr(statement, 'statements'):
            for s in statement.statements:
                self.execute_statement(s)
        elif hasattr(statement, 'name') and hasattr(statement, 'params') and hasattr(statement, 'body'):
            self.functions[statement.name] = statement
        elif hasattr(statement, 'name') and hasattr(statement, 'args'):
            self.call_function(statement.name, statement.args)
        elif hasattr(statement, 'expression') and hasattr(statement, 'event'):
            self.suggest_outfit(self.evaluate_expression(statement.expression), statement.event)
        elif hasattr(statement, 'expression') and type(statement).__name__ == 'ReturnStatement':
            self.return_value = self.evaluate_expression(statement.expression)
        else:
            raise Exception(f"Unknown statement: {type(statement).__name__}")

    def evaluate_expression(self, expr):
        if hasattr(expr, 'value'):
            return expr.value
        elif type(expr) == str:
            return self.variables.get(expr, expr)
        elif hasattr(expr, 'name') and hasattr(expr, 'args'):
            return self.call_function(expr.name, expr.args)
        elif hasattr(expr, 'left') and hasattr(expr, 'operator') and hasattr(expr, 'right'):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            return self.apply_operator(expr.operator, left, right)
        elif hasattr(expr, 'expression'):
            return str(self.evaluate_expression(expr.expression))
        elif hasattr(expr, 'left') and hasattr(expr, 'right'):
            return str(self.evaluate_expression(expr.left)) + str(self.evaluate_expression(expr.right))
        else:
            return expr

    def apply_operator(self, op, left, right):
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right
        if op == '+': return str(left) + str(right)
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '&&': return bool(left) and bool(right)
        if op == '||': return bool(left) or bool(right)
        raise Exception(f"Unsupported operator: {op}")

    def call_function(self, name, args):
        if name in self.functions:
            function = self.functions[name]
            saved_vars = self.variables.copy()

            for i, param in enumerate(function.params):
                self.variables[param.name] = self.evaluate_expression(args[i]) if i < len(args) else None

            self.return_value = None
            self.execute_statement(function.body)
            result = self.return_value
            self.variables = saved_vars
            return result
        elif name == "collectClosetItems":
            return self.collect_closet_items()
        elif name == "planOutfit":
            event = self.evaluate_expression(args[0])
            items = self.evaluate_expression(args[1])
            return self.plan_outfit(event, items)
        else:
            raise Exception(f"Unknown function: {name}")

    def collect_closet_items(self):
        items = []
        while True:
            item = input("Add item (or press Enter to stop): ")
            if item == "":
                break
            items.append(item)
        return items

    def plan_outfit(self, event, items):
        if not isinstance(items, list):
            items = [items]
        suggestion = f"For a {event} event, wear: " + ", ".join(items[:3])
        return suggestion

    def suggest_outfit(self, outfit_description, event_name):
        print("\n--- SUGGESTED OUTFIT ---")
        print("Outfit:", outfit_description)
        if event_name:
            print("Event:", event_name)
        print("Style Tip: Dress with confidence!")

# Entry point
def run_talkfashion_program(file_path):
    interpreter = TalkFashionInterpreter()
    return interpreter.interpret(file_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        run_talkfashion_program(sys.argv[1])
    else:
        print("Please provide a TalkFashion .talk program file.")
