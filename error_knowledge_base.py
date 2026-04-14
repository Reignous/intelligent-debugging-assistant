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
    },
    "ImportError": {
        "explanation": "Python could not import a module or a name from a module.",
        "suggestion": "Check if the module is installed and the import statement is correct."
    },
"TabError": {
    "explanation": "Mixing tabs and spaces in indentation.",
    "suggestion": "Use either tabs or spaces consistently (prefer 4 spaces)."
},
"FileNotFoundError": {
    "explanation": "The file you are trying to access does not exist.",
    "suggestion": "Check the file path and ensure the file exists."
},

"IOError": {
    "explanation": "An input/output operation failed.",
    "suggestion": "Check file permissions and file availability."
},

"AssertionError": {
    "explanation": "An assert statement has failed.",
    "suggestion": "Check the condition inside the assert statement."
},

"MemoryError": {
    "explanation": "Python ran out of memory.",
    "suggestion": "Try optimizing your code or using smaller data structures."
},

"OverflowError": {
    "explanation": "A calculation exceeds the maximum limit for a numeric type.",
    "suggestion": "Check calculations and use appropriate data types."
},

"RecursionError": {
    "explanation": "Maximum recursion depth exceeded.",
    "suggestion": "Ensure your recursive function has a proper base case."
},

"StopIteration": {
    "explanation": "Raised when there are no more items in an iterator.",
    "suggestion": "Handle iteration properly or use loops instead of manual next()."
},

"RuntimeError": {
    "explanation": "A generic error that does not fall into other categories.",
    "suggestion": "Check the specific message for more details."
},

"KeyboardInterrupt": {
    "explanation": "Program execution was interrupted manually (Ctrl+C).",
    "suggestion": "Handle interruption using try-except if needed."
},

"PermissionError": {
    "explanation": "You do not have permission to perform an operation.",
    "suggestion": "Check file or system permissions."
},

"IsADirectoryError": {
    "explanation": "Expected a file but found a directory instead.",
    "suggestion": "Ensure the path points to a file, not a folder."
},

"NotADirectoryError": {
    "explanation": "Expected a directory but found a file instead.",
    "suggestion": "Check the path and ensure it's a directory."
},

"UnboundLocalError": {
    "explanation": "A local variable is referenced before assignment.",
    "suggestion": "Assign a value before using the variable."
},

"EOFError": {
    "explanation": "Input() reached end-of-file condition without reading data.",
    "suggestion": "Ensure input is being provided correctly."
},

"FloatingPointError": {
    "explanation": "A floating-point operation failed.",
    "suggestion": "Check numerical operations and enable error handling if needed."
}
}
