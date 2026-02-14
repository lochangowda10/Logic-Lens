"""
Programming Language Syntax and Rules Guide - Kannada Version
Provides offline reference for common programming concepts in Kannada
"""

# Kannada translations for syntax guide
KANNADA_TRANSLATIONS = {
    "Variable ek dabba hai jisme value store hoti hai. Jaise locker mein cheez rakhte ho.": 
        "Variable ಒಂದು ಪೆಟ್ಟಿಗೆ ಅಲ್ಲಿ value store ಆಗುತ್ತದೆ. Locker ನಲ್ಲಿ ವಸ್ತುಗಳನ್ನು ಇಡುವಂತೆ.",
    
    "Print matlab screen pe dikhana. Jaise WhatsApp pe message bhejte ho.":
        "Print ಅಂದರೆ screen ನಲ್ಲಿ ತೋರಿಸುವುದು. WhatsApp ನಲ್ಲಿ message ಕಳುಹಿಸುವಂತೆ.",
    
    "Comment matlab notes - computer ignore karta hai, sirf tumhare liye hai.":
        "Comment ಅಂದರೆ notes - computer ignore ಮಾಡುತ್ತದೆ, ನಿಮಗೆ ಮಾತ್ರ.",
    
    "Agar-warna logic. Jaise ATM mein - agar balance hai toh paisa milega, warna sorry!":
        "ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ logic. ATM ನಲ್ಲಿ - balance ಇದ್ದರೆ ಹಣ ಸಿಗುತ್ತದೆ, ಇಲ್ಲದಿದ್ದರೆ sorry!",
    
    "Loop matlab repeat karna. Jaise railway counter pe token system - sabki baari aayegi.":
        "Loop ಅಂದರೆ repeat ಮಾಡುವುದು. Railway counter ನಲ್ಲಿ token system ಹಾಗೆ - ಎಲ್ಲರ ಸರದಿ ಬರುತ್ತದೆ.",
    
    "Jab tak condition true hai, tab tak chalta rahega. Jaise fan on hai toh ghoomta rahega.":
        "Condition true ಇರುವವರೆಗೆ ಚಾಲನೆಯಲ್ಲಿರುತ್ತದೆ. Fan on ಇದ್ದರೆ ತಿರುಗುತ್ತಿರುವಂತೆ.",
    
    "Function ek machine hai - input do, output milta hai. Jaise calculator.":
        "Function ಒಂದು machine - input ಕೊಡಿ, output ಸಿಗುತ್ತದೆ. Calculator ಹಾಗೆ.",
    
    "List ek shopping bag hai - bahut saari cheezein ek saath rakh sakte ho.":
        "List ಒಂದು shopping bag - ಬಹಳಷ್ಟು ವಸ್ತುಗಳನ್ನು ಒಟ್ಟಿಗೆ ಇಡಬಹುದು.",
    
    "Dictionary matlab phone ki contact list - naam se number nikalta hai.":
        "Dictionary ಅಂದರೆ phone ನ contact list - ಹೆಸರಿನಿಂದ number ಸಿಗುತ್ತದೆ.",
    
    "Variable declare karte waqt type batana padta hai - int, String, etc.":
        "Variable declare ಮಾಡುವಾಗ type ಹೇಳಬೇಕು - int, String, etc.",
    
    "Print karne ka tarika thoda lamba hai Java mein - System.out.println":
        "Print ಮಾಡುವ ವಿಧಾನ Java ನಲ್ಲಿ ಸ್ವಲ್ಪ ಉದ್ದವಾಗಿದೆ - System.out.println",
    
    "Agar-warna logic, bas curly braces {} use karte hain.":
        "ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ logic, curly braces {} ಬಳಸುತ್ತೇವೆ.",
    
    "Loop ka syntax thoda complex hai - initialization, condition, aur increment ek saath.":
        "Loop ನ syntax ಸ್ವಲ್ಪ complex - initialization, condition, ಮತ್ತು increment ಒಟ್ಟಿಗೆ.",
    
    "Java mein function ko method kehte hain. Return type batana zaroori hai.":
        "Java ನಲ್ಲಿ function ಅನ್ನು method ಎಂದು ಕರೆಯುತ್ತಾರೆ. Return type ಹೇಳುವುದು ಕಡ್ಡಾಯ.",
    
    "C mein type declare karna mandatory hai. Memory management khud karna padta hai.":
        "C ನಲ್ಲಿ type declare ಮಾಡುವುದು mandatory. Memory management ನೀವೇ ಮಾಡಬೇಕು.",
    
    "Printf mein format specifier use karte hain - %d for int, %s for string.":
        "Printf ನಲ್ಲಿ format specifier ಬಳಸುತ್ತೇವೆ - %d for int, %s for string.",
    
    "Java jaisa hi syntax, bas printf use karte hain.":
        "Java ಹಾಗೆಯೇ syntax, printf ಬಳಸುತ್ತೇವೆ.",
    
    "Loop structure Java jaisa hai, bas printf use karte hain.":
        "Loop structure Java ಹಾಗೆಯೇ ಇದೆ, printf ಬಳಸುತ್ತೇವೆ.",
    
    "C++ mein C ke saare features + extra features hain. String type available hai.":
        "C++ ನಲ್ಲಿ C ನ ಎಲ್ಲಾ features + extra features ಇವೆ. String type ಲಭ್ಯವಿದೆ.",
    
    "Cout use karte hain printing ke liye. << operator se values bhejte hain.":
        "Cout ಅನ್ನು printing ಗಾಗಿ ಬಳಸುತ್ತೇವೆ. << operator ನಿಂದ values ಕಳುಹಿಸುತ್ತೇವೆ.",
    
    "C aur Java jaisa syntax, cout use karte hain output ke liye.":
        "C ಮತ್ತು Java ಹಾಗೆಯೇ syntax, output ಗಾಗಿ cout ಬಳಸುತ್ತೇವೆ.",
    
    "let se variable banate hain jo change ho sakta hai. const se constant banate hain.":
        "let ನಿಂದ variable ಮಾಡುತ್ತೇವೆ ಅದು change ಆಗಬಹುದು. const ನಿಂದ constant ಮಾಡುತ್ತೇವೆ.",
    
    "Console.log se browser console mein print hota hai.":
        "Console.log ನಿಂದ browser console ನಲ್ಲಿ print ಆಗುತ್ತದೆ.",
    
    "Java jaisa syntax, bas console.log use karte hain.":
        "Java ಹಾಗೆಯೇ syntax, console.log ಬಳಸುತ್ತೇವೆ.",
    
    "Loop structure Java jaisa hai, let use karte hain variable ke liye.":
        "Loop structure Java ಹಾಗೆಯೇ ಇದೆ, variable ಗಾಗಿ let ಬಳಸುತ್ತೇವೆ.",
    
    "Function define karne ke do tarike - function keyword ya arrow function.":
        "Function define ಮಾಡಲು ಎರಡು ವಿಧಾನಗಳು - function keyword ಅಥವಾ arrow function."
}

def translate_to_kannada(hinglish_text):
    """Translate Hinglish to Kannada"""
    return KANNADA_TRANSLATIONS.get(hinglish_text, hinglish_text)
