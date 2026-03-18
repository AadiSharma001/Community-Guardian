from pydantic import BaseModel

class IncidentCreate(BaseModel):
    description: str
    location: str
    severity: str