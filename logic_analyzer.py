from google import genai
from google.genai import types
import os
import time
import re
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_demo_response(code: str, language: str) -> dict:
    """
    Fallback demo response when API quota is exhausted
    """
    
    # Simple pattern matching for demo
    has_loop = bool(re.search(r'(for|while)\s+', code))
    has_condition = bool(re.search(r'if\s+', code))
    has_function = bool(re.search(r'def\s+\w+', code))
    
    explanation = f"This {language} code "
    analogy = ""
    concepts = []
    
    if has_function:
        explanation += "defines a function that performs a specific task. "
        analogy += "ಈ function ಒಂದು machine ಹಾಗೆ - input ಕೊಡಿ, output ಸಿಗುತ್ತದೆ. "
        concepts.append("Functions - Reusable code blocks")
    
    if has_loop:
        explanation += "It uses a loop to repeat operations multiple times. "
        analogy += "Loop ಅಂದರೆ ಒಂದು ಸಾಲಿನಲ್ಲಿ ನಿಂತಿರುವ ಜನರು - ಎಲ್ಲರ ಸರದಿ ಬರುತ್ತದೆ. "
        concepts.append("Loops - Repetition of code")
    
    if has_condition:
        explanation += "It includes conditional logic to make decisions. "
        analogy += "If-else ಅಂದರೆ ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ - ATM ನಲ್ಲಿ balance check ಮಾಡುವಂತೆ. "
        concepts.append("Conditionals - Decision making")
    
    if not (has_loop or has_condition or has_function):
        explanation = "This code performs sequential operations, executing statements one after another."
        analogy = "ಈ code ಒಂದು recipe ಹಾಗೆ - step by step instructions follow ಮಾಡುತ್ತದೆ. ಮೊದಲು ಇದು, ನಂತರ ಅದು!"
        concepts = ["Sequential execution", "Basic statements"]
    
    return {
        "explanation": explanation.strip(),
        "analogy": analogy.strip() or "Code ಅನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸುಲಭವಾದ ವಿಧಾನ step-by-step ನೋಡುವುದು!",
        "key_concepts": concepts if concepts else ["Programming basics"]
    }

def analyze_code_logic(code: str, language: str) -> dict:
    """
    Analyze code logic using Gemini API and generate Hinglish analogies
    With retry logic and demo fallback
    """
    
    max_retries = 3
    retry_delay = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            prompt = f"""
You are LogicLens AI, an assistant for 1st-year B.Tech students in Karnataka, India. 
Analyze this {language} code and explain it in a way that's easy to understand.

Code:
```{language.lower()}
{code}
```

Provide your response in this format:

1. EXPLANATION: A clear, simple explanation of what the code does (in English with some Kannada words where natural)

2. KANNADA ANALOGY: Create a relatable analogy using everyday Karnataka/Indian scenarios. Use Kannada naturally. Think of examples like:
   - Loops as "ಒಂದು ಸಾಲಿನಲ್ಲಿ ನಿಂತಿರುವ ಜನರು" (people standing in a queue)
   - Variables as "ಪೆಟ್ಟಿಗೆ" (container) 
   - Functions as "machine ಅದು ಕೆಲಸ ಮಾಡುತ್ತದೆ"
   - Conditions as "ಇದ್ದರೆ-ಇಲ್ಲದಿದ್ದರೆ" situations
   Make it fun and memorable!

3. KEY CONCEPTS: List 2-3 important programming concepts used (in simple terms)

Keep it conversational and friendly. Use Kannada naturally, not forced.
"""
            
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=prompt
            )
            result_text = response.text
            # Parse the response
            sections = result_text.split("\n\n")
            
            explanation = ""
            analogy = ""
            key_concepts = []
            
            current_section = None
            for line in result_text.split("\n"):
                line = line.strip()
                if "EXPLANATION" in line.upper():
                    current_section = "explanation"
                elif "KANNADA ANALOGY" in line.upper() or "ANALOGY" in line.upper():
                    current_section = "analogy"
                elif "KEY CONCEPTS" in line.upper():
                    current_section = "concepts"
                elif line and current_section:
                    if current_section == "explanation":
                        explanation += line + " "
                    elif current_section == "analogy":
                        analogy += line + " "
                    elif current_section == "concepts" and line.startswith("-"):
                        key_concepts.append(line[1:].strip())
            
            # Fallback if parsing fails
            if not explanation and not analogy:
                explanation = result_text[:len(result_text)//2]
                analogy = result_text[len(result_text)//2:]
            
            return {
                "explanation": explanation.strip() or "Code analysis completed!",
                "analogy": analogy.strip() or "Think of this code as a step-by-step recipe!",
                "key_concepts": key_concepts if key_concepts else ["Programming logic", "Code structure"]
            }
            
        except Exception as e:
            error_msg = str(e)
            
            # Check if it's a quota/rate limit error
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
                if attempt < max_retries - 1:
                    # Retry with exponential backoff
                    wait_time = retry_delay * (2 ** attempt)
                    print(f"Rate limit hit. Retrying in {wait_time}s... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                    continue
                else:
                    # Use demo mode after all retries
                    print("⚠️ API quota exhausted. Using demo mode...")
                    return get_demo_response(code, language)
            
            # For other errors, return immediately
            return {
                "explanation": f"Error analyzing code: {error_msg}",
                "analogy": "Please check your Gemini API key configuration or try again later.",
                "key_concepts": []
            }
    
    # If all retries failed, use demo mode
    return get_demo_response(code, language)
