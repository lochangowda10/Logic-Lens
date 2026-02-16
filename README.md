# LogicLens AI

AI-powered learning assistant for 1st-year B.Tech students in India, translating technical code logic into regional analogies (Hinglish).

## 🌐 Live Demo

**Try LogicLens AI**: https://logic-lens.streamlit.app/

<!-- After deployment, replace above with:
**Try LogicLens AI**: [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)
-->

## Features

- Google OAuth authentication
- Streamlit-based mobile-friendly interface
- **Real-time Syntax Validation** - Checks code before analysis
  - Detects indentation errors (Python)
  - Finds missing semicolons (Java, C, C++)
  - Identifies missing colons and braces
  - Provides fix suggestions in Hinglish
- Gemini API integration for semantic logic analysis
- Logic-to-Analogy engine with Hinglish explanations
- **Offline Syntax Guide** - Complete programming reference without API calls
  - Python, Java, C, C++, JavaScript syntax
  - Hinglish explanations for every concept
  - Searchable topics
  - Code examples with rules
- Visual flowchart generation
- Demo mode fallback when API quota is exhausted

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
- Offline Syntax Database (No API needed)

