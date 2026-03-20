# Community Guardian

## Candidate Name:
Aadi Sharma

## Scenario Chosen:
Community Guardian — AI-powered platform to aggregate and simplify local safety and digital security alerts into calm, actionable insights.

## Project Structure

community-guardian/
│
├── app/
│   ├── main.py        # FastAPI server
│   ├── models.py      # Data models
│   ├── ai.py          # AI + fallback logic
│   ├── fallback.py    # Rule-based fallback
│   ├── storage.py     # JSON storage
│
├── data/
│   └── incidents.json # Synthetic dataset
│
├── tests/
│   └── test_app.py    # Unit tests
│
├── cli.py             # CLI interface
├── requirements.txt
├── .env.example
├── README.md

## Estimated Time Spent:
~5–6 hours

## Problem
Users face alert fatigue due to scattered and noisy safety information.

## Solution

## Quick Start:

### ● Prerequisites:
- Python 3.9+
- pip
- (Optional) Virtual environment

---

### ● Run Commands:

# Clone repo
git clone https://github.com/YOUR_USERNAME/community-guardian.git
cd community-guardian

# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

## Environment Setup
cp .env.example .env
# Add your API key inside .env

# How to run

Run server:
uvicorn app.main:app --reload

Run CLI:
python cli.py

## Tests

python -m pytest

## AI Disclosure

### ● Did you use an AI assistant (Copilot, ChatGPT, etc.)?
Yes

### ● How did you verify the suggestions?
- Manually reviewed all generated code before integrating  
- Ran the backend (FastAPI) and CLI locally to validate functionality  
- Checked API endpoints via `/docs` (Swagger UI)  
- Verified outputs (categorization, summaries, actions) matched expected behavior  
- Added and executed unit tests (happy path + edge case)  

### ● Give one example of a suggestion you rejected or changed:
- Initially used relative imports (e.g., `from models import IncidentCreate`)  
- This caused module resolution errors when running the server  
- Refactored to absolute imports (`from app.models import IncidentCreate`) for stability  

---

## Tradeoffs & Prioritization

### ● What did you cut to stay within the 4–6 hour limit?
- Skipped building a frontend UI (used CLI instead)  
- Did not integrate a real AI API (used fallback logic for reliability)  
- Avoided database setup (used JSON storage for simplicity)  
- Did not implement authentication or user accounts  
- Skipped real-time data ingestion  

### ● What would you build next if you had more time?
- React-based dashboard for better user experience  
- Trust scoring system for ranking incident reliability  
- Daily digest feature to reduce alert fatigue  
- Real-time ingestion pipeline (e.g., Kafka + stream processing)  
- Graph-based clustering to detect emerging threat patterns  

### ● Known limitations:
- Uses static JSON instead of a scalable database  
- No real-time or external data sources  
- AI responses are simulated or rule-based  
- CLI interface is not user-friendly for non-technical users  
- No authentication or multi-user support  

## Demo video link
https://youtu.be/EdSoMO0wMzQ