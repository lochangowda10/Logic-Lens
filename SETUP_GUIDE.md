# LogicLens AI - Setup Guide

## Quick Start for Hackathon Demo

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Note: The app now uses the newer `google-genai` package (the old `google-generativeai` is deprecated).

### 2. Get Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

### 3. Configure Environment

Create a `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_CLIENT_ID=optional_for_demo
GOOGLE_CLIENT_SECRET=optional_for_demo
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## For Production Deployment

### Google OAuth Setup (Optional for Demo)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URI: `http://localhost:8501`
6. Download credentials and add to `.env`

### Mobile Optimization

The app is already optimized for mobile with:
- Responsive layout
- Touch-friendly buttons
- Collapsed sidebar by default
- Mobile-first CSS

### Deployment Options

- **Streamlit Cloud**: Push to GitHub and deploy via streamlit.io
- **Heroku**: Use Procfile for deployment
- **Railway**: Direct deployment from GitHub

## Testing the App

1. Login with any email (demo mode)
2. Paste sample code:
```python
for i in range(5):
    print(i)
```
3. Click "Analyze Logic"
4. View the Hinglish explanation!

## Troubleshooting

- **API Quota Error (429)**: The app automatically retries and falls back to demo mode. See TROUBLESHOOTING.md
- **API Error**: Check your Gemini API key in `.env`
- **Import Error**: Run `pip install --upgrade google-genai`
- **Port in use**: Change port with `streamlit run app.py --server.port 8502`

For detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
