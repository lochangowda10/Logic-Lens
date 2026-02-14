# LogicLens AI - Troubleshooting Guide

## Common Issues and Solutions

### 1. API Quota Exhausted (429 Error)

**Error Message:**
```
Error analyzing code: 429 RESOURCE_EXHAUSTED
You exceeded your current quota
```

**What it means:**
You've hit the free tier rate limits for Gemini API.

**Solutions:**

#### Option A: Wait and Retry
Free tier limits reset after:
- Per minute: Wait 60 seconds
- Per day: Wait until next day (resets at midnight UTC)

#### Option B: Use Demo Mode (Built-in)
The app automatically falls back to demo mode after 3 retry attempts. Demo mode provides:
- Basic pattern-based analysis
- Simple Hinglish analogies
- Works offline without API calls

#### Option C: Get More Quota
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Check your quota limits
3. Consider upgrading to paid tier for higher limits

#### Option D: Use Alternative Free Models
Try these models with higher free tier limits:
- `gemini-2.5-flash-lite` - Lighter, faster, higher quota
- `gemini-flash-lite-latest` - Latest lite version

To change model, edit `logic_analyzer.py`:
```python
response = client.models.generate_content(
    model='gemini-2.5-flash-lite',  # Change here
    contents=prompt
)
```

### 2. Model Not Found (404 Error)

**Error Message:**
```
404 models/gemini-xxx is not found
```

**Solution:**
Check available models by running:
```bash
python check_models.py
```

Update `logic_analyzer.py` with a valid model name from the list.

### 3. Invalid API Key

**Error Message:**
```
401 UNAUTHENTICATED
API key not valid
```

**Solution:**
1. Verify your API key at [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Check `.env` file has correct key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
3. Restart the Streamlit app after updating `.env`

### 4. Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'google.genai'
```

**Solution:**
```bash
pip install --upgrade google-genai
pip install -r requirements.txt
```

### 5. Streamlit Not Starting

**Error Message:**
```
streamlit: command not found
```

**Solution:**
```bash
pip install streamlit
# Or
python -m streamlit run app.py
```

### 6. Port Already in Use

**Error Message:**
```
Address already in use
```

**Solution:**
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill existing process (Windows)
netstat -ano | findstr :8501
taskkill /PID <process_id> /F
```

## Rate Limits Reference

### Gemini Free Tier Limits (as of 2025)

| Model | Requests/Min | Requests/Day | Tokens/Min |
|-------|--------------|--------------|------------|
| gemini-2.0-flash | 15 | 1,500 | 1M |
| gemini-2.5-flash-lite | 30 | 3,000 | 2M |
| gemini-flash-lite-latest | 30 | 3,000 | 2M |

**Tips to avoid hitting limits:**
1. Test with shorter code snippets
2. Wait 4-5 seconds between requests
3. Use demo mode for rapid testing
4. Cache results for repeated queries

## Demo Mode Features

When API quota is exhausted, the app automatically uses demo mode:

**What Demo Mode Provides:**
- ✅ Pattern-based code analysis
- ✅ Basic Hinglish analogies
- ✅ Concept identification (loops, conditions, functions)
- ✅ Works completely offline
- ❌ Less detailed than AI analysis
- ❌ No context-aware explanations

**Demo Mode Detection:**
```python
# Automatically detects:
- Loops (for, while)
- Conditions (if, else)
- Functions (def, function)
- Basic patterns
```

## Optimization Tips

### 1. Reduce Token Usage
```python
# Keep code snippets under 200 lines
# Focus on specific functions/methods
# Remove unnecessary comments before analysis
```

### 2. Implement Caching
```python
# Add to logic_analyzer.py
from functools import lru_cache

@lru_cache(maxsize=50)
def analyze_code_cached(code_hash):
    return analyze_code_logic(code, language)
```

### 3. Batch Processing
For multiple code snippets, wait between requests:
```python
import time
time.sleep(5)  # 5 seconds between requests
```

## Getting Help

### Check API Status
1. Visit [Google AI Status](https://status.cloud.google.com/)
2. Check [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

### Monitor Usage
1. Go to [AI Studio Usage](https://aistudio.google.com/app/usage)
2. View current quota consumption
3. See when limits reset

### Community Support
- [Google AI Forum](https://discuss.ai.google.dev/)
- [Stack Overflow - gemini-api tag](https://stackoverflow.com/questions/tagged/gemini-api)

## For Hackathon Judges

If you encounter quota issues while testing:

1. **Demo Mode is Intentional**: The app gracefully degrades to demo mode
2. **Shows Resilience**: Demonstrates error handling and fallback strategies
3. **Still Functional**: Core features work without API
4. **Video Demo**: Check our demo video for full AI-powered experience

## Production Deployment

For production use:

1. **Upgrade to Paid Tier**
   - Higher rate limits
   - Better SLA
   - Priority support

2. **Implement Redis Caching**
   ```python
   import redis
   cache = redis.Redis(host='localhost', port=6379)
   ```

3. **Add Request Queue**
   ```python
   from celery import Celery
   # Queue requests to avoid rate limits
   ```

4. **Monitor Usage**
   ```python
   # Track API calls
   # Alert before hitting limits
   # Auto-switch to demo mode
   ```

## Quick Fixes Checklist

- [ ] Check `.env` file exists and has valid API key
- [ ] Run `pip install -r requirements.txt`
- [ ] Verify internet connection
- [ ] Check API quota at aistudio.google.com
- [ ] Try demo mode (automatic after retries)
- [ ] Restart Streamlit app
- [ ] Clear browser cache
- [ ] Try different model (gemini-2.5-flash-lite)

## Contact

For issues specific to this hackathon project:
- Check GitHub Issues
- Review TECHNICAL_DESIGN.md
- See SETUP_GUIDE.md

---

**Remember**: Demo mode is a feature, not a bug! It ensures the app remains functional even when API limits are reached.
