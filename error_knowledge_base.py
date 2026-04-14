# error_knowledge_base.py

ERROR_DATABASE = {
    "SyntaxError": {
        "explanation": "There is a syntax mistake in your code. Python cannot understand this line.",
        "suggestion": "Check for missing colons (:), brackets, quotes, or incorrect indentation."
    },
    "NameError": {
        "explanation": "You are trying to use a variable or function that has not been defined.",
        "suggestion": "Make sure the variable or function name is spelled correctly and declared before use."
    },
    "TypeError": {
        "explanation": "An operation was applied to an object of inappropriate type.",
        "suggestion": "Check if you are mixing incompatible data types like int and string."
    },
    "ValueError": {
        "explanation": "A function received the correct type but an inappropriate value.",
        "suggestion": "Check if the value passed to the function is valid."
    },
    "IndexError": {
        "explanation": "You are trying to access an index that does not exist in a list.",
        "suggestion": "Check the length of the list before accessing elements."
    },
    "KeyError": {
        "explanation": "You are trying to access a dictionary key that does not exist.",
        "suggestion": "Make sure the key exists in the dictionary before accessing it."
    },
    "ZeroDivisionError": {
        "explanation": "You are dividing a number by zero.",
        "suggestion": "Ensure the denominator is not zero before division."
    },
    "ModuleNotFoundError": {
        "explanation": "Python cannot find the module you are trying to import.",
        "suggestion": "Check if the module is installed or if the import name is correct."
    },
    "IndentationError": {
        "explanation": "There is incorrect indentation in your code.",
        "suggestion": "Ensure consistent indentation (use 4 spaces per level)."
    },
    "AttributeError": {
        "explanation": "You are trying to access an attribute that does not exist for that object.",
        "suggestion": "Check if the object has that attribute or method."
    }
}
