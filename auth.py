import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def check_authentication():
    """Handle authentication - Demo mode for hackathon"""
    
    # Check if user is already authenticated
    if "authenticated" in st.session_state and st.session_state.authenticated:
        st.sidebar.success(f"✅ Logged in as {st.session_state.get('user_email', 'User')}")
        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.user_email = None
            st.rerun()
        return True
    
    # Show login interface
    st.markdown("## Welcome to LogicLens AI! 👋")
    st.markdown("*ನಿಮ್ಮ code ಅನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸುಲಭವಾದ ಮಾರ್ಗ*")
    
    st.info("🔐 Please login to continue")
    
    # Demo login
    st.markdown("### Demo Login")
    email = st.text_input("Enter your email (demo mode)", placeholder="student@example.com")
    
    if st.button("Login with Google (Demo)", use_container_width=True):
        if email:
            st.session_state.authenticated = True
            st.session_state.user_email = email
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Please enter an email")
    
    st.markdown("---")
    st.markdown("*Demo mode for hackathon - No actual Google OAuth required*")
    
    return False
