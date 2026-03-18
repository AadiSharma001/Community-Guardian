# Community Guardian

## Problem
Users face alert fatigue due to scattered and noisy safety information.

## Solution
A calm, AI-powered safety digest platform that filters noise and provides actionable insights.

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

## How to Run

pip install -r requirements.txt
uvicorn app.main:app --reload

Run CLI:
python cli.py

## Tests

pytest

## Design Decisions
- Area-level location → privacy
- Summaries → reduce anxiety
- Fallback → reliability without AI

## Future Improvements
- Real-time ingestion (Kafka)
- Trust scoring
- Graph-based clustering