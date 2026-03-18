from fastapi import FastAPI, HTTPException
from app.models import IncidentCreate
from app.storage import load_data, save_data, get_next_id
from app.ai import process_with_ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Community Guardian API"}

@app.get("/incidents")
def get_incidents(location: str = None, category: str = None):
    data = load_data()

    if location:
        data = [i for i in data if i["location"].lower() == location.lower()]

    if category:
        data = [i for i in data if i["type"].lower() == category.lower()]

    return data

@app.post("/incidents")
def create_incident(incident: IncidentCreate):
    if not incident.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")

    data = load_data()

    ai_result = process_with_ai(incident.description)

    new_incident = {
        "id": get_next_id(data),
        "type": ai_result["category"],
        "description": incident.description,
        "summary": ai_result["summary"],
        "actions": ai_result["actions"],
        "location": incident.location,
        "severity": incident.severity,
        "status": "open"
    }

    data.append(new_incident)
    save_data(data)

    return new_incident

@app.put("/incidents/{incident_id}")
def update_incident(incident_id: int, status: str):
    data = load_data()

    for incident in data:
        if incident["id"] == incident_id:
            incident["status"] = status
            save_data(data)
            return incident

    raise HTTPException(status_code=404, detail="Incident not found")