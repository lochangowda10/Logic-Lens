import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_code_logic(code: str, language: str) -> dict:
    """
    Analyze code logic using Gemini API and generate Hinglish analogies
    """
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
You are LogicLens AI, an assistant for 1st-year B.Tech students in India. 
Analyze this {language} code and explain it in a way that's easy to understand.

Code:
```{language.lower()}
{code}
```

Provide your response in this format:

1. EXPLANATION: A clear, simple explanation of what the code does (in English with some Hinglish words where natural)

2. HINGLISH ANALOGY: Create a relatable analogy using everyday Indian scenarios. Use Hinglish naturally. Think of examples like:
   - Loops as "ek line mein khade log" (people standing in a queue)
   - Variables as "dabba" (container) 
   - Functions as "machine jo kaam karta hai"
   - Conditions as "agar-warna" situations
   Make it fun and memorable!

3. KEY CONCEPTS: List 2-3 important programming concepts used (in simple terms)

Keep it conversational and friendly. Use Hinglish naturally, not forced.
"""
        
        response = model.generate_content(prompt)
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
            elif "HINGLISH ANALOGY" in line.upper() or "ANALOGY" in line.upper():
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
        return {
            "explanation": f"Error analyzing code: {str(e)}",
            "analogy": "Please check your Gemini API key configuration.",
            "key_concepts": []
        }
