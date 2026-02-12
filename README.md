# LogicLens AI

AI-powered learning assistant for 1st-year B.Tech students in India, translating technical code logic into regional analogies (Hinglish).

## Features

- Google OAuth authentication
- Streamlit-based mobile-friendly interface
- Gemini API integration for semantic logic analysis
- Logic-to-Analogy engine with Hinglish explanations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GEMINI_API_KEY=your_gemini_api_key
```

3. Run the app:
```bash
streamlit run app.py
```

## Tech Stack

- Streamlit (UI)
- Google OAuth (Authentication)
- Gemini API (Logic Analysis)
- Python 3.9+
