"""
Syntax Validator - Checks code for common syntax errors
Provides helpful error messages in Hinglish
"""

import re
import ast

def validate_python(code: str) -> dict:
    """
    Validate Python code syntax
    Returns: {"valid": bool, "errors": list, "warnings": list}
    """
    errors = []
    warnings = []
    
    lines = code.split('\n')
    
    # Check for indentation issues
    for i, line in enumerate(lines, 1):
        stripped = line.lstrip()
        
        # Check if line should be indented (after :)
        if i > 1:
            prev_line = lines[i-2].rstrip()
            if prev_line.endswith(':'):
                # This line should be indented
                if stripped and not line.startswith((' ', '\t')):
                    errors.append({
                        "line": i,
                        "message": f"Line {i}: Indentation missing after colon",
                        "kannada": f"Line {i}: Colon (:) ನಂತರ indentation ಕಡ್ಡಾಯ! 4 spaces ಅಥವಾ Tab ಹಾಕಿ.",
                        "suggestion": f"    {stripped}",
                        "type": "IndentationError"
                    })
        
        # Check for common mistakes
        if stripped.startswith('for ') or stripped.startswith('while '):
            if not stripped.endswith(':'):
                errors.append({
                    "line": i,
                    "message": f"Line {i}: Missing colon after loop statement",
                    "kannada": f"Line {i}: Loop ನಂತರ colon (:) ಹಾಕಲು ಮರೆತಿದ್ದೀರಿ!",
                    "suggestion": stripped + ':',
                    "type": "SyntaxError"
                })
        
        if stripped.startswith('if ') or stripped.startswith('elif ') or stripped.startswith('else'):
            if not stripped.endswith(':'):
                errors.append({
                    "line": i,
                    "message": f"Line {i}: Missing colon after conditional",
                    "kannada": f"Line {i}: If/else ನಂತರ colon (:) ಕಡ್ಡಾಯ!",
                    "suggestion": stripped + ':',
                    "type": "SyntaxError"
                })
        
        if stripped.startswith('def '):
            if not stripped.endswith(':'):
                errors.append({
                    "line": i,
                    "message": f"Line {i}: Missing colon after function definition",
                    "kannada": f"Line {i}: Function define ಮಾಡುವಾಗ colon (:) ಹಾಕಿ!",
                    "suggestion": stripped + ':',
                    "type": "SyntaxError"
                })
        
        # Check for assignment vs comparison
        if re.search(r'\bif\s+\w+\s*=\s*\w+', stripped):
            warnings.append({
                "line": i,
                "message": f"Line {i}: Using '=' in condition, did you mean '=='?",
                "kannada": f"Line {i}: Condition ನಲ್ಲಿ '=' ಬಳಸಿದ್ದೀರಿ, '==' ಬೇಕಿತ್ತೇ?",
                "type": "Warning"
            })
    
    # Try to parse with AST
    if not errors:
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append({
                "line": e.lineno if e.lineno else 0,
                "message": f"Syntax Error: {e.msg}",
                "kannada": f"Syntax ತಪ್ಪಾಗಿದೆ line {e.lineno} ನಲ್ಲಿ. ಎಚ್ಚರಿಕೆಯಿಂದ ಪರಿಶೀಲಿಸಿ!",
                "type": "SyntaxError"
            })
        except IndentationError as e:
            errors.append({
                "line": e.lineno if e.lineno else 0,
                "message": f"Indentation Error: {e.msg}",
                "kannada": f"Indentation ತಪ್ಪಾಗಿದೆ line {e.lineno} ನಲ್ಲಿ. Spaces/tabs ಪರಿಶೀಲಿಸಿ!",
                "type": "IndentationError"
            })
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def validate_java(code: str) -> dict:
    """
    Validate Java code syntax
    """
    errors = []
    warnings = []
    
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Check for missing semicolons
        if stripped and not stripped.endswith((';', '{', '}', '//', '/*', '*/')):
            if any(keyword in stripped for keyword in ['int ', 'String ', 'double ', 'float ', 'boolean ', 'char ', 'return ']):
                if not stripped.startswith(('if', 'for', 'while', 'else', 'public', 'private', 'class', 'void')):
                    errors.append({
                        "line": i,
                        "message": f"Line {i}: Missing semicolon",
                        "kannada": f"Line {i}: Semicolon (;) ಹಾಕಲು ಮರೆತಿದ್ದೀರಿ!",
                        "suggestion": stripped + ';',
                        "type": "SyntaxError"
                    })
        
        # Check for missing braces
        if any(keyword in stripped for keyword in ['if (', 'for (', 'while (']):
            if ')' in stripped and '{' not in stripped:
                warnings.append({
                    "line": i,
                    "message": f"Line {i}: Missing opening brace",
                    "kannada": f"Line {i}: Control statement ನಂತರ opening brace {{}} ಹಾಕಿ!",
                    "type": "Warning"
                })
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def validate_c_cpp(code: str) -> dict:
    """
    Validate C/C++ code syntax
    """
    errors = []
    warnings = []
    
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Check for missing semicolons
        if stripped and not stripped.endswith((';', '{', '}', '//', '/*', '*/')):
            if any(keyword in stripped for keyword in ['int ', 'float ', 'double ', 'char ', 'return ', 'printf', 'cout']):
                if not stripped.startswith(('if', 'for', 'while', 'else', '#', 'void')):
                    errors.append({
                        "line": i,
                        "message": f"Line {i}: Missing semicolon",
                        "kannada": f"Line {i}: Statement ಕೊನೆಯಲ್ಲಿ semicolon (;) ಕಡ್ಡಾಯ!",
                        "suggestion": stripped + ';',
                        "type": "SyntaxError"
                    })
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def validate_javascript(code: str) -> dict:
    """
    Validate JavaScript code syntax
    """
    errors = []
    warnings = []
    
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Check for var usage (should use let/const)
        if stripped.startswith('var '):
            warnings.append({
                "line": i,
                "message": f"Line {i}: Using 'var' is outdated",
                "kannada": f"Line {i}: 'var' ಹಳೆಯ ವಿಧಾನ, 'let' ಅಥವಾ 'const' ಬಳಸಿ!",
                "type": "Warning"
            })
        
        # Check for == vs ===
        if '==' in stripped and '===' not in stripped and '!=' in stripped:
            warnings.append({
                "line": i,
                "message": f"Line {i}: Consider using '===' for strict equality",
                "kannada": f"Line {i}: Strict comparison ಗಾಗಿ '===' ಬಳಸಿ!",
                "type": "Warning"
            })
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def validate_code(code: str, language: str) -> dict:
    """
    Main validation function
    """
    if not code.strip():
        return {
            "valid": False,
            "errors": [{
                "message": "Code is empty",
                "kannada": "Code ಖಾಲಿ ಇದೆ! ಮೊದಲು ಏನಾದರೂ ಬರೆಯಿರಿ.",
                "type": "EmptyCode"
            }],
            "warnings": []
        }
    
    validators = {
        "Python": validate_python,
        "Java": validate_java,
        "C": validate_c_cpp,
        "C++": validate_c_cpp,
        "JavaScript": validate_javascript
    }
    
    validator = validators.get(language)
    
    if validator:
        return validator(code)
    else:
        # No validator available, assume valid
        return {
            "valid": True,
            "errors": [],
            "warnings": []
        }

def format_validation_message(validation_result: dict) -> str:
    """
    Format validation results for display
    """
    if validation_result["valid"] and not validation_result["warnings"]:
        return "✅ Code syntax ಸರಿಯಾಗಿದೆ!"
    
    message = ""
    
    if validation_result["errors"]:
        message += "❌ **Syntax ದೋಷಗಳು ಕಂಡುಬಂದಿವೆ:**\n\n"
        for error in validation_result["errors"]:
            message += f"**Line {error.get('line', '?')}:** {error.get('kannada', error['message'])}\n"
            if 'suggestion' in error:
                message += f"```\n{error['suggestion']}\n```\n"
            message += "\n"
    
    if validation_result["warnings"]:
        message += "⚠️ **ಎಚ್ಚರಿಕೆಗಳು:**\n\n"
        for warning in validation_result["warnings"]:
            message += f"**Line {warning.get('line', '?')}:** {warning.get('kannada', warning['message'])}\n\n"
    
    return message
