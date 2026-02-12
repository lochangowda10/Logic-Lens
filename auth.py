import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

def check_authentication():
    """Handle Google OAuth authentication"""
    
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
    st.markdown("*Apne code ko samajhne ka sabse aasan tarika*")
    
    st.info("🔐 Please login with Google to continue")
    
    # For hackathon demo - simplified auth
    st.markdown("### Demo Login")
    email = st.text_input("Enter your email (demo mode)")
    
    if st.button("Login with Google (Demo)", use_container_width=True):
        if email:
            st.session_state.authenticated = True
            st.session_state.user_email = email
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Please enter an email")
    
    st.markdown("---")
    st.markdown("*For production: Configure Google OAuth credentials in .env file*")
    
    return False

def get_google_oauth_flow():
    """Initialize Google OAuth flow (for production)"""
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        return None
    
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://localhost:8501"]
            }
        },
        scopes=["openid", "email", "profile"]
    )
    
    return flow
