# Community Guardian
A calm, AI-powered safety digest that reduces alert fatigue and provides actionable insights.

## Problem
Users face alert fatigue due to scattered and noisy safety information.

## Solution
A calm, AI-powered safety digest platform that filters noise and provides actionable insights.

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

## Features
- Incident creation
- AI + fallback summarization
- Search & filtering
- Status updates

## AI + Fallback
- AI summarizes and categorizes incidents
- Fallback rule-based system ensures reliability

## Tech Stack
- FastAPI (backend)
- CLI interface
- JSON storage

## Environment Setup
cp .env.example .env
# Add your API key inside .env

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload

Run CLI:
python cli.py

## Tests

python -m pytest

## Design Decisions
- Area-level location → privacy
- Summaries → reduce anxiety
- Fallback → reliability without AI

## Future Improvements
- Real-time ingestion (Kafka)
- Trust scoring
- Graph-based clustering