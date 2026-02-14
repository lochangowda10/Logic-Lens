"""
Programming Language Syntax and Rules Guide
Provides offline reference for common programming concepts
"""

SYNTAX_GUIDE = {
    "Python": {
        "basics": {
            "Variables": {
                "syntax": "variable_name = value",
                "example": "age = 21\nname = 'Rahul'",
                "kannada": "Variable ಒಂದು ಪೆಟ್ಟಿಗೆ ಅಲ್ಲಿ value store ಆಗುತ್ತದೆ. Locker ನಲ್ಲಿ ವಸ್ತುಗಳನ್ನು ಇಡುವಂತೆ.",
                "rules": [
                    "Variable names can contain letters, numbers, underscore",
                    "Cannot start with a number",
                    "Case sensitive (age ≠ Age)",
                    "No spaces allowed"
                ]
            },
            "Print Statement": {
                "syntax": "print(value)",
                "example": "print('Hello')\nprint(age)",
                "kannada": "Print ಅಂದರೆ screen ನಲ್ಲಿ ತೋರಿಸುವುದು. WhatsApp ನಲ್ಲಿ message ಕಳುಹಿಸುವಂತೆ.",
                "rules": [
                    "Use parentheses ()",
                    "Strings need quotes",
                    "Can print multiple values with comma"
                ]
            },
            "Comments": {
                "syntax": "# This is a comment",
                "example": "# Calculate total\ntotal = 100  # Price",
                "kannada": "Comment ಅಂದರೆ notes - computer ignore ಮಾಡುತ್ತದೆ, ನಿಮಗೆ ಮಾತ್ರ.",
                "rules": [
                    "Start with # symbol",
                    "Computer doesn't execute comments",
                    "Use for explanations"
                ]
            }
        },
        "control_flow": {
            "If-Else": {
                "syntax": "if condition:\n    # code\nelse:\n    # code",
                "example": "if marks >= 40:\n    print('Pass')\nelse:\n    print('Fail')",
                "kannada": "ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ logic. ATM ನಲ್ಲಿ - balance ಇದ್ದರೆ ಹಣ ಸಿಗುತ್ತದೆ, ಇಲ್ಲದಿದ್ದರೆ sorry!",
                "rules": [
                    "Colon (:) is mandatory",
                    "Indentation (4 spaces) is required",
                    "Condition must be True/False",
                    "else is optional"
                ]
            },
            "For Loop": {
                "syntax": "for variable in sequence:\n    # code",
                "example": "for i in range(5):\n    print(i)",
                "kannada": "Loop ಅಂದರೆ repeat ಮಾಡುವುದು. Railway counter ನಲ್ಲಿ token system ಹಾಗೆ - ಎಲ್ಲರ ಸರದಿ ಬರುತ್ತದೆ.",
                "rules": [
                    "Colon (:) required",
                    "Indentation mandatory",
                    "range(n) gives 0 to n-1",
                    "Can loop over lists, strings, etc."
                ]
            },
            "While Loop": {
                "syntax": "while condition:\n    # code",
                "example": "count = 0\nwhile count < 5:\n    print(count)\n    count += 1",
                "kannada": "Condition true ಇರುವವರೆಗೆ ಚಾಲನೆಯಲ್ಲಿರುತ್ತದೆ. Fan on ಇದ್ದರೆ ತಿರುಗುತ್ತಿರುವಂತೆ.",
                "rules": [
                    "Condition checked before each iteration",
                    "Must update condition inside loop",
                    "Risk of infinite loop if not careful",
                    "Use break to exit early"
                ]
            }
        },
        "functions": {
            "Function Definition": {
                "syntax": "def function_name(parameters):\n    # code\n    return value",
                "example": "def add(a, b):\n    return a + b\n\nresult = add(5, 3)",
                "kannada": "Function ಒಂದು machine - input ಕೊಡಿ, output ಸಿಗುತ್ತದೆ. Calculator ಹಾಗೆ.",
                "rules": [
                    "Start with 'def' keyword",
                    "Colon (:) after parameters",
                    "return sends value back",
                    "Can have multiple parameters"
                ]
            }
        },
        "data_structures": {
            "List": {
                "syntax": "list_name = [item1, item2, item3]",
                "example": "fruits = ['apple', 'banana', 'mango']\nfruits[0]  # 'apple'",
                "kannada": "List ಒಂದು shopping bag - ಬಹಳಷ್ಟು ವಸ್ತುಗಳನ್ನು ಒಟ್ಟಿಗೆ ಇಡಬಹುದು.",
                "rules": [
                    "Use square brackets []",
                    "Index starts from 0",
                    "Can store different types",
                    "Mutable (can change)"
                ]
            },
            "Dictionary": {
                "syntax": "dict_name = {key: value}",
                "example": "student = {'name': 'Raj', 'age': 20}\nstudent['name']  # 'Raj'",
                "kannada": "Dictionary ಅಂದರೆ phone ನ contact list - ಹೆಸರಿನಿಂದ number ಸಿಗುತ್ತದೆ.",
                "rules": [
                    "Use curly braces {}",
                    "Key-value pairs",
                    "Keys must be unique",
                    "Access using keys"
                ]
            }
        }
    },
    "Java": {
        "basics": {
            "Variables": {
                "syntax": "dataType variableName = value;",
                "example": "int age = 21;\nString name = \"Rahul\";",
                "kannada": "Variable declare ಮಾಡುವಾಗ type ಹೇಳಬೇಕು - int, String, etc.",
                "rules": [
                    "Must declare data type",
                    "Semicolon (;) at end",
                    "CamelCase naming convention",
                    "Strongly typed language"
                ]
            },
            "Print Statement": {
                "syntax": "System.out.println(value);",
                "example": "System.out.println(\"Hello\");\nSystem.out.println(age);",
                "kannada": "Print ಮಾಡುವ ವಿಧಾನ Java ನಲ್ಲಿ ಸ್ವಲ್ಪ ಉದ್ದವಾಗಿದೆ - System.out.println",
                "rules": [
                    "Semicolon required",
                    "println adds new line",
                    "print doesn't add new line",
                    "Strings use double quotes"
                ]
            }
        },
        "control_flow": {
            "If-Else": {
                "syntax": "if (condition) {\n    // code\n} else {\n    // code\n}",
                "example": "if (marks >= 40) {\n    System.out.println(\"Pass\");\n} else {\n    System.out.println(\"Fail\");\n}",
                "kannada": "ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ logic, curly braces {} ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Condition in parentheses ()",
                    "Code in curly braces {}",
                    "Semicolons inside blocks",
                    "else is optional"
                ]
            },
            "For Loop": {
                "syntax": "for (init; condition; update) {\n    // code\n}",
                "example": "for (int i = 0; i < 5; i++) {\n    System.out.println(i);\n}",
                "kannada": "Loop ನ syntax ಸ್ವಲ್ಪ complex - initialization, condition, ಮತ್ತು increment ಒಟ್ಟಿಗೆ.",
                "rules": [
                    "Three parts separated by semicolons",
                    "Curly braces for code block",
                    "i++ means i = i + 1",
                    "Declare variable in loop"
                ]
            }
        },
        "functions": {
            "Method Definition": {
                "syntax": "returnType methodName(parameters) {\n    // code\n    return value;\n}",
                "example": "public int add(int a, int b) {\n    return a + b;\n}",
                "kannada": "Java ನಲ್ಲಿ function ಅನ್ನು method ಎಂದು ಕರೆಯುತ್ತಾರೆ. Return type ಹೇಳುವುದು ಕಡ್ಡಾಯ.",
                "rules": [
                    "Must specify return type",
                    "public/private access modifier",
                    "void if no return value",
                    "Parameters need types"
                ]
            }
        }
    },
    "C": {
        "basics": {
            "Variables": {
                "syntax": "dataType variableName = value;",
                "example": "int age = 21;\nchar grade = 'A';",
                "kannada": "C ನಲ್ಲಿ type declare ಮಾಡುವುದು mandatory. Memory management ನೀವೇ ಮಾಡಬೇಕು.",
                "rules": [
                    "Must declare type",
                    "Semicolon required",
                    "char uses single quotes",
                    "No string type (use char array)"
                ]
            },
            "Print Statement": {
                "syntax": "printf(\"format\", variables);",
                "example": "printf(\"Age: %d\\n\", age);\nprintf(\"Name: %s\\n\", name);",
                "kannada": "Printf ನಲ್ಲಿ format specifier ಬಳಸುತ್ತೇವೆ - %d for int, %s for string.",
                "rules": [
                    "%d for integers",
                    "%f for floats",
                    "%c for characters",
                    "%s for strings",
                    "\\n for new line"
                ]
            }
        },
        "control_flow": {
            "If-Else": {
                "syntax": "if (condition) {\n    // code\n} else {\n    // code\n}",
                "example": "if (marks >= 40) {\n    printf(\"Pass\");\n} else {\n    printf(\"Fail\");\n}",
                "kannada": "Java ಹಾಗೆಯೇ syntax, printf ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Condition in parentheses",
                    "Curly braces for blocks",
                    "Semicolons required",
                    "0 is false, non-zero is true"
                ]
            },
            "For Loop": {
                "syntax": "for (init; condition; update) {\n    // code\n}",
                "example": "for (int i = 0; i < 5; i++) {\n    printf(\"%d\\n\", i);\n}",
                "kannada": "Loop structure Java ಹಾಗೆಯೇ ಇದೆ, printf ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Three parts in parentheses",
                    "Curly braces for body",
                    "i++ increments by 1",
                    "Semicolons separate parts"
                ]
            }
        }
    },
    "C++": {
        "basics": {
            "Variables": {
                "syntax": "dataType variableName = value;",
                "example": "int age = 21;\nstring name = \"Rahul\";",
                "kannada": "C++ ನಲ್ಲಿ C ನ ಎಲ್ಲಾ features + extra features ಇವೆ. String type ಲಭ್ಯವಿದೆ.",
                "rules": [
                    "Type declaration required",
                    "Semicolon at end",
                    "string type available",
                    "Can use auto keyword"
                ]
            },
            "Print Statement": {
                "syntax": "cout << value << endl;",
                "example": "cout << \"Hello\" << endl;\ncout << age << endl;",
                "kannada": "Cout ಅನ್ನು printing ಗಾಗಿ ಬಳಸುತ್ತೇವೆ. << operator ನಿಂದ values ಕಳುಹಿಸುತ್ತೇವೆ.",
                "rules": [
                    "Use cout for output",
                    "<< is insertion operator",
                    "endl for new line",
                    "Can chain multiple values"
                ]
            }
        },
        "control_flow": {
            "If-Else": {
                "syntax": "if (condition) {\n    // code\n} else {\n    // code\n}",
                "example": "if (marks >= 40) {\n    cout << \"Pass\";\n} else {\n    cout << \"Fail\";\n}",
                "kannada": "C ಮತ್ತು Java ಹಾಗೆಯೇ syntax, output ಗಾಗಿ cout ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Same as C/Java",
                    "Use cout for output",
                    "Curly braces required",
                    "Boolean type available"
                ]
            }
        }
    },
    "JavaScript": {
        "basics": {
            "Variables": {
                "syntax": "let variableName = value;\nconst constantName = value;",
                "example": "let age = 21;\nconst name = 'Rahul';",
                "kannada": "let ನಿಂದ variable ಮಾಡುತ್ತೇವೆ ಅದು change ಆಗಬಹುದು. const ನಿಂದ constant ಮಾಡುತ್ತೇವೆ.",
                "rules": [
                    "Use let for variables",
                    "Use const for constants",
                    "Avoid var (old style)",
                    "No type declaration needed"
                ]
            },
            "Print Statement": {
                "syntax": "console.log(value);",
                "example": "console.log('Hello');\nconsole.log(age);",
                "kannada": "Console.log ನಿಂದ browser console ನಲ್ಲಿ print ಆಗುತ್ತದೆ.",
                "rules": [
                    "Use console.log()",
                    "Semicolon optional",
                    "Can print multiple values",
                    "Shows in browser console"
                ]
            }
        },
        "control_flow": {
            "If-Else": {
                "syntax": "if (condition) {\n    // code\n} else {\n    // code\n}",
                "example": "if (marks >= 40) {\n    console.log('Pass');\n} else {\n    console.log('Fail');\n}",
                "kannada": "Java ಹಾಗೆಯೇ syntax, console.log ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Parentheses for condition",
                    "Curly braces for blocks",
                    "Semicolons optional",
                    "=== for strict equality"
                ]
            },
            "For Loop": {
                "syntax": "for (let i = 0; i < n; i++) {\n    // code\n}",
                "example": "for (let i = 0; i < 5; i++) {\n    console.log(i);\n}",
                "kannada": "Loop structure Java ಹಾಗೆಯೇ ಇದೆ, variable ಗಾಗಿ let ಬಳಸುತ್ತೇವೆ.",
                "rules": [
                    "Use let in loop",
                    "Three parts in parentheses",
                    "Curly braces for body",
                    "Can use for...of for arrays"
                ]
            }
        },
        "functions": {
            "Function Definition": {
                "syntax": "function functionName(parameters) {\n    // code\n    return value;\n}",
                "example": "function add(a, b) {\n    return a + b;\n}\nconst result = add(5, 3);",
                "kannada": "Function define ಮಾಡಲು ಎರಡು ವಿಧಾನಗಳು - function keyword ಅಥವಾ arrow function.",
                "rules": [
                    "Use function keyword",
                    "No type declaration",
                    "return sends value back",
                    "Arrow functions: (a, b) => a + b"
                ]
            }
        }
    }
}

def get_syntax_info(language: str, topic: str = None) -> dict:
    """
    Get syntax information for a specific language and topic
    """
    if language not in SYNTAX_GUIDE:
        return None
    
    if topic:
        # Search for specific topic
        for category, topics in SYNTAX_GUIDE[language].items():
            if topic in topics:
                return {
                    "language": language,
                    "topic": topic,
                    "category": category,
                    **topics[topic]
                }
        return None
    
    # Return all topics for the language
    return SYNTAX_GUIDE[language]

def search_syntax(query: str, language: str = None) -> list:
    """
    Search for syntax information across languages
    """
    results = []
    query_lower = query.lower()
    
    languages = [language] if language else SYNTAX_GUIDE.keys()
    
    for lang in languages:
        if lang not in SYNTAX_GUIDE:
            continue
            
        for category, topics in SYNTAX_GUIDE[lang].items():
            for topic_name, topic_data in topics.items():
                if (query_lower in topic_name.lower() or 
                    query_lower in topic_data.get('kannada', '').lower()):
                    results.append({
                        "language": lang,
                        "topic": topic_name,
                        "category": category,
                        **topic_data
                    })
    
    return results

def get_all_topics(language: str) -> list:
    """
    Get list of all available topics for a language
    """
    if language not in SYNTAX_GUIDE:
        return []
    
    topics = []
    for category, category_topics in SYNTAX_GUIDE[language].items():
        for topic_name in category_topics.keys():
            topics.append({
                "name": topic_name,
                "category": category
            })
    
    return topics
