from pydantic import BaseModel, Field
from typing import List, Optional

# --- Pydantic Models ---

class ExperienceItem(BaseModel):
    title: str
    duration: str
    responsibilities: List[str]

class Language(BaseModel):
    language: str
    level: str

class Skills(BaseModel):
    # Mapping "skill_name" to a string. 
    # If the model outputs a comma-separated string of skills, this captures it.
    skill_name: str 
    spokenlanguages: List[Language]

class EducationItem(BaseModel):
    title: str
    # Use Field(alias=...) to map the JSON key "school name" to Python variable "school_name"
    school_name: str = Field(alias="school name") 
    grade: str
    description: str

class Summary(BaseModel):
    description: str

class ProjectItem(BaseModel):
    title: str
    description: str

class ResumeStructure(BaseModel):
    experience: List[ExperienceItem]
    skills: Skills
    education: List[EducationItem]
    summary: Summary
    projects: List[ProjectItem]