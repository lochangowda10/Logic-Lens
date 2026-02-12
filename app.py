import streamlit as st
from auth import check_authentication
from logic_analyzer import analyze_code_logic
from flowchart_generator import generate_mermaid_flowchart
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
    st.markdown("*Samajhne ka naya tarika - Code ko apni bhasha mein!*")
    
    # Authentication check
    if not check_authentication():
        return
    
    # Main interface
    st.markdown("### Enter your code:")
    code_input = st.text_area(
        "Paste your code here",
        height=200,
        placeholder="# Example:\nfor i in range(5):\n    print(i)"
    )
    
    language = st.selectbox(
        "Programming Language",
        ["Python", "Java", "C", "C++", "JavaScript"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        analyze_btn = st.button("🔍 Analyze Logic", use_container_width=True)
    with col2:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)
    
    if clear_btn:
        st.rerun()
    
    if analyze_btn and code_input.strip():
        with st.spinner("Analyzing... Thoda wait karo!"):
            result = analyze_code_logic(code_input, language)
            
            if result:
                # Create tabs for different views
                tab1, tab2, tab3 = st.tabs(["📖 Explanation", "🎯 Analogy", "📊 Flowchart"])
                
                with tab1:
                    st.markdown("### Logic Explanation")
                    st.info(result["explanation"])
                    
                    if result.get("key_concepts"):
                        st.markdown("### 💡 Key Concepts")
                        for concept in result["key_concepts"]:
                            st.markdown(f"- {concept}")
                
                with tab2:
                    st.markdown("### Hinglish Analogy")
                    st.success(result["analogy"])
                
                with tab3:
                    st.markdown("### Visual Flow")
                    try:
                        mermaid_code = generate_mermaid_flowchart(code_input, language)
                        st.code(mermaid_code, language="mermaid")
                        st.info("💡 Tip: Copy this Mermaid code to visualize at mermaid.live")
                    except Exception as e:
                        st.warning("Flowchart generation unavailable for this code")
    
    elif analyze_btn:
        st.warning("Please enter some code first!")
    
    # Footer
    st.markdown("---")
    st.markdown("*Made for AI for Bharat Hackathon 🇮🇳*")

if __name__ == "__main__":
    main()
