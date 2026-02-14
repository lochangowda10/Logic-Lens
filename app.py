import streamlit as st
from auth import check_authentication
from logic_analyzer import analyze_code_logic
from flowchart_generator import generate_mermaid_flowchart
from syntax_guide import get_all_topics, get_syntax_info, search_syntax
from syntax_validator import validate_code, format_validation_message
import os

# Page config for mobile optimization
st.set_page_config(
    page_title="LogicLens AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile-friendly UI
st.markdown("""
<style>
    .main { padding: 1rem; }
    .stTextArea textarea { font-family: monospace; }
    @media (max-width: 768px) {
        .main { padding: 0.5rem; }
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🔍 LogicLens AI")
    st.markdown("*ಕೋಡ್ ಅನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಹೊಸ ಮಾರ್ಗ - ನಿಮ್ಮ ಸ್ವಂತ ಭಾಷೆಯಲ್ಲಿ!*")
    
    # Authentication check
    if not check_authentication():
        return
    
    # Main tabs
    main_tab1, main_tab2 = st.tabs(["💻 Code Analyzer", "📚 Syntax Guide"])
    
    with main_tab1:
        show_code_analyzer()
    
    with main_tab2:
        show_syntax_guide()
    
    # Footer
    st.markdown("---")
    st.markdown("*Made for AI for Bharat Hackathon 🇮🇳*")

def show_code_analyzer():
    """Code analysis interface"""
    st.markdown("### Enter your code:")
    
    # Show example button
    col_ex1, col_ex2 = st.columns([3, 1])
    with col_ex2:
        if st.button("📝 Load Example", use_container_width=True):
            st.session_state.show_example = True
    
    # Example code snippets
    examples = {
        "Python": """# Python Example - Correct Syntax
for i in range(5):
    print(i)  # Note: Indented with 4 spaces

if i > 2:
    print("Greater than 2")
else:
    print("Less than or equal to 2")""",
        "Java": """// Java Example - Correct Syntax
for (int i = 0; i < 5; i++) {
    System.out.println(i);  // Note: Semicolon at end
}

if (i > 2) {
    System.out.println("Greater");
} else {
    System.out.println("Less");
}""",
        "C": """// C Example - Correct Syntax
for (int i = 0; i < 5; i++) {
    printf("%d\\n", i);  // Note: Semicolon required
}

if (i > 2) {
    printf("Greater");
} else {
    printf("Less");
}""",
        "C++": """// C++ Example - Correct Syntax
for (int i = 0; i < 5; i++) {
    cout << i << endl;  // Note: Semicolon at end
}

if (i > 2) {
    cout << "Greater";
} else {
    cout << "Less";
}""",
        "JavaScript": """// JavaScript Example - Correct Syntax
for (let i = 0; i < 5; i++) {
    console.log(i);  // Note: Use let, not var
}

if (i > 2) {
    console.log("Greater");
} else {
    console.log("Less");
}"""
    }
    
    code_input = st.text_area(
        "Paste your code here",
        height=200,
        placeholder="# Example:\nfor i in range(5):\n    print(i)",
        key="code_input"
    )
    
    language = st.selectbox(
        "Programming Language",
        ["Python", "Java", "C", "C++", "JavaScript"]
    )
    
    # Quick syntax reminder
    syntax_reminders = {
        "Python": "💡 ನೆನಪಿಡಿ: Python ನಲ್ಲಿ colon (:) ನಂತರ indentation (4 spaces) ಬೇಕು",
        "Java": "💡 ನೆನಪಿಡಿ: Java ನಲ್ಲಿ semicolons (;) ಮತ್ತು curly braces {} ಬೇಕು",
        "C": "💡 ನೆನಪಿಡಿ: C ನಲ್ಲಿ semicolons (;) ಮತ್ತು curly braces {} ಬೇಕು",
        "C++": "💡 ನೆನಪಿಡಿ: C++ ನಲ್ಲಿ semicolons (;) ಮತ್ತು curly braces {} ಬೇಕು",
        "JavaScript": "💡 ನೆನಪಿಡಿ: var ಬದಲು let/const ಬಳಸಿ, semicolons optional"
    }
    
    st.info(syntax_reminders.get(language, ""))
    
    # Show example if requested
    if st.session_state.get('show_example'):
        with st.expander("📝 Example Code (Click to copy)", expanded=True):
            st.code(examples.get(language, ""), language=language.lower())
            if st.button("❌ Close Example"):
                st.session_state.show_example = False
                st.rerun()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        analyze_btn = st.button("🔍 Analyze Logic", use_container_width=True)
    with col2:
        validate_btn = st.button("✅ Check Syntax", use_container_width=True)
    with col3:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_btn:
        st.rerun()
    
    # Validate syntax first if requested
    if validate_btn and code_input.strip():
        validation_result = validate_code(code_input, language)
        
        if validation_result["valid"] and not validation_result["warnings"]:
            st.success("✅ Code syntax ಸರಿಯಾಗಿದೆ! ಈಗ analyze ಮಾಡಬಹುದು.")
        else:
            message = format_validation_message(validation_result)
            if validation_result["errors"]:
                st.error(message)
            else:
                st.warning(message)
    
    if analyze_btn and code_input.strip():
        # First validate syntax
        validation_result = validate_code(code_input, language)
        
        if not validation_result["valid"]:
            st.error("⚠️ Syntax ದೋಷಗಳು ಕಂಡುಬಂದಿವೆ! ದಯವಿಟ್ಟು ಮೊದಲು ಅವುಗಳನ್ನು ಸರಿಪಡಿಸಿ.")
            message = format_validation_message(validation_result)
            st.markdown(message)
            st.info("💡 ಸಲಹೆ: ವಿವರವಾದ ದೋಷಗಳನ್ನು ನೋಡಲು 'Check Syntax' ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.")
            return
        
        # Show warnings but continue
        if validation_result["warnings"]:
            with st.expander("⚠️ ಎಚ್ಚರಿಕೆಗಳು (ಕೋಡ್ ಅನ್ನು ಇನ್ನೂ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತದೆ)"):
                st.warning(format_validation_message(validation_result))
        
        with st.spinner("ವಿಶ್ಲೇಷಣೆ ಮಾಡುತ್ತಿದೆ... ಸ್ವಲ್ಪ ಕಾಯಿರಿ!"):
            result = analyze_code_logic(code_input, language)
            
            if result:
                # Check if demo mode was used
                if "Error analyzing code: 429" in result.get("explanation", ""):
                    st.warning("⚠️ API quota ಮಿತಿ ತಲುಪಿದೆ. ಈ ವಿಶ್ಲೇಷಣೆಗಾಗಿ demo mode ಬಳಸುತ್ತಿದೆ.")
                
                # Create tabs for different views
                tab1, tab2, tab3 = st.tabs(["📖 Explanation", "🎯 Analogy", "📊 Flowchart"])
                
                with tab1:
                    st.markdown("### Logic Explanation")
                    if "Error" in result["explanation"]:
                        st.error(result["explanation"])
                    else:
                        st.info(result["explanation"])
                    
                    if result.get("key_concepts"):
                        st.markdown("### 💡 Key Concepts")
                        for concept in result["key_concepts"]:
                            st.markdown(f"- {concept}")
                
                with tab2:
                    st.markdown("### ಕನ್ನಡ ಉದಾಹರಣೆ")
                    st.success(result["analogy"])
                
                with tab3:
                    st.markdown("### Visual Flow")
                    try:
                        mermaid_code = generate_mermaid_flowchart(code_input, language)
                        st.code(mermaid_code, language="mermaid")
                        st.info("💡 ಸಲಹೆ: ಈ Mermaid code ಅನ್ನು mermaid.live ನಲ್ಲಿ visualize ಮಾಡಲು copy ಮಾಡಿ")
                    except Exception as e:
                        st.warning("ಈ ಕೋಡ್‌ಗೆ Flowchart generation ಲಭ್ಯವಿಲ್ಲ")
    
    elif analyze_btn:
        st.warning("ದಯವಿಟ್ಟು ಮೊದಲು ಕೋಡ್ ಅನ್ನು ನಮೂದಿಸಿ!")

def show_syntax_guide():
    """Syntax and rules reference guide"""
    st.markdown("### 📖 Programming Language Reference")
    st.info("💡 Offline guide - API calls ಬೇಕಿಲ್ಲ! ನಿಮ್ಮ language ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ಕಲಿಯಿರಿ.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        language = st.selectbox(
            "Select Language",
            ["Python", "Java", "C", "C++", "JavaScript"],
            key="syntax_lang"
        )
    
    with col2:
        search_query = st.text_input("🔍 Search topic", placeholder="e.g., loop, function")
    
    if search_query:
        # Search mode
        results = search_syntax(search_query, language)
        
        if results:
            st.success(f"{len(results)} ಫಲಿತಾಂಶ(ಗಳು) ಕಂಡುಬಂದಿವೆ")
            for result in results:
                with st.expander(f"📌 {result['topic']} ({result['category'].title()})"):
                    st.code(result['syntax'], language=language.lower())
                    
                    st.markdown("**Example:**")
                    st.code(result['example'], language=language.lower())
                    
                    st.markdown("**ಕನ್ನಡ ವಿವರಣೆ:**")
                    st.info(result['kannada'])
                    
                    st.markdown("**Rules:**")
                    for rule in result['rules']:
                        st.markdown(f"- {rule}")
        else:
            st.warning("ಫಲಿತಾಂಶಗಳು ಕಂಡುಬಂದಿಲ್ಲ. ವಿಭಿನ್ನ keywords ಪ್ರಯತ್ನಿಸಿ!")
    else:
        # Browse mode - show all topics
        topics = get_all_topics(language)
        
        if topics:
            # Group by category
            categories = {}
            for topic in topics:
                cat = topic['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(topic['name'])
            
            for category, topic_names in categories.items():
                st.markdown(f"### {category.replace('_', ' ').title()}")
                
                for topic_name in topic_names:
                    info = get_syntax_info(language, topic_name)
                    
                    with st.expander(f"📌 {topic_name}"):
                        col_a, col_b = st.columns([1, 1])
                        
                        with col_a:
                            st.markdown("**Syntax:**")
                            st.code(info['syntax'], language=language.lower())
                            
                            st.markdown("**Example:**")
                            st.code(info['example'], language=language.lower())
                        
                        with col_b:
                            st.markdown("**ಕನ್ನಡ ವಿವರಣೆ:**")
                            st.info(info['kannada'])
                            
                            st.markdown("**Rules:**")
                            for rule in info['rules']:
                                st.markdown(f"- {rule}")
        else:
            st.warning(f"{language} ಗಾಗಿ syntax guide ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ.")
    
    # Quick reference card
    st.markdown("---")
    st.markdown("### 🎯 ತ್ವರಿತ ಸಲಹೆಗಳು")
    
    tips_col1, tips_col2 = st.columns(2)
    
    with tips_col1:
        st.markdown("""
        **ಸಾಮಾನ್ಯ ತಪ್ಪುಗಳು:**
        - Semicolons ಮರೆಯುವುದು (Java, C, C++)
        - ತಪ್ಪು indentation (Python)
        - Comparison ಗಾಗಿ == ಬದಲು = ಬಳಸುವುದು
        - Brackets/braces ಮುಚ್ಚಲು ಮರೆಯುವುದು
        """)
    
    with tips_col2:
        st.markdown("""
        **ಪ್ರೊ ಸಲಹೆಗಳು:**
        - ಅರ್ಥಪೂರ್ಣ variable names ಬಳಸಿ
        - ಸಂಕೀರ್ಣ logic ಗಾಗಿ comments ಸೇರಿಸಿ
        - ಸಣ್ಣ examples ನೊಂದಿಗೆ ಮೊದಲು test ಮಾಡಿ
        - ಪ್ರತಿದಿನ 30 ನಿಮಿಷ ಅಭ್ಯಾಸ ಮಾಡಿ
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*💡 ಸಲಹೆ: ನಿಮಗೆ ಬೇಕಾದುದನ್ನು ತ್ವರಿತವಾಗಿ ಹುಡುಕಲು search box ಬಳಸಿ!*")

if __name__ == "__main__":
    main()
