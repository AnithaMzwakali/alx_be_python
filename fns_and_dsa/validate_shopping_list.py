import os
import ast

FILE = "shopping_list_manager.py"

def check_file_exists_and_not_empty():
    if os.path.isfile(FILE) and os.path.getsize(FILE) > 0:
        return True
    return False

def check_display_menu_defined(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "display_menu":
            return True
    return False

def check_shopping_list_defined(tree):
    for node in ast.walk(tree):
        # look for shopping_list = []
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "shopping_list":
                    if isinstance(node.value, ast.List):
                        return True
    return False

def check_display_menu_called(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "display_menu":
            return True
    return False

def check_choice_input_number(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Call):
                if getattr(node.value.func, "id", "") == "input":
                    return True
    return False

def main():
    if not check_file_exists_and_not_empty():
        print("❌ File does not exist or is empty")
        return
    
    with open(FILE, "r") as f:
        source = f.read()
    
    tree = ast.parse(source)
    
    print("Check 1 - File exists and not empty:", "✅ Passed" if check_file_exists_and_not_empty() else "❌ Failed")
    print("Check 2 - display_menu defined:", "✅ Passed" if check_display_menu_defined(tree) else "❌ Failed")
    print("Check 3 - shopping_list defined as a list:", "✅ Passed" if check_shopping_list_defined(tree) else "❌ Failed")
    print("Check 4 - display_menu called:", "✅ Passed" if check_display_menu_called(tree) else "❌ Failed")
    print("Check 5 - choice input implemented:", "✅ Passed" if check_choice_input_number(tree) else "❌ Failed")

if __name__ == "__main__":
    main()

