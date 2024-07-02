from langroid.utils.configuration import settings as lsettings
lsettings.cache_type = "fakeredis"
import langroid as lr

from typing import Dict, List, Optional
from redis_om import JsonModel, EmbeddedJsonModel, Field
from langroid.language_models.base import LLMMessage

from pydantic import BaseModel, Extra, HttpUrl, EmailStr
from datetime import date


### Models for Kiwi

class Product(JsonModel):
    product_id: str = Field(None, description="Unique identifier for the product", index=True)
    name: str = Field(..., description="Name of the product", index=True)
    description: str = Field(..., description="Description of the product")
    category: str = Field(None, description="Category the product belongs to")
    price: Optional[float] = Field(None, description="Price of the product")
    currency: Optional[str] = Field(None, description="Currency for the price")
    stock_quantity: Optional[int] = Field(None, description="Number of items in stock")
    sku: Optional[str] = Field(None, description="Stock Keeping Unit identifier")
    manufacturer: Optional[str] = Field(None, description="Manufacturer of the product")
    warranty: Optional[str] = Field(None, description="Warranty period for the product")
    dimensions: Optional[tuple] = Field(None, description="Dimensions of the product (length, width, height)")
    weight: Optional[float] = Field(None, description="Weight of the product")
    color: Optional[str] = Field(None, description="Color of the product")
    release_date: Optional[date] = Field(None, description="Release date of the product")
    end_of_life_date: Optional[date] = Field(None, description="End of life date of the product")
    download_url: Optional[HttpUrl] = Field(None, description="URL to download the product, if applicable")
    documentation_url: Optional[HttpUrl] = Field(None, description="URL to the documentation, if applicable")
    features: Optional[List[str]] = Field(None, description="List of features of the product")

class Service(JsonModel):
    service_id: str = Field(None, description="Unique identifier for the service", index=True)
    name: str = Field(..., description="Name of the service", index=True)
    description: str = Field(..., description="Description of the service")
    category: Optional[str] = Field(None, description="Category the service belongs to")
    price: Optional[float] = Field(None, description="Price of the service")
    currency: Optional[str] = Field(None, description="Currency for the price")
    availability: Optional[str] = Field(None, description="Availability status of the service")
    provider: Optional[str] = Field(None, description="Provider of the service")
    contact_email: Optional[EmailStr] = Field(None, description="Contact email for the service provider")
    contact_phone: Optional[str] = Field(None, description="Contact phone number for the service provider")
    website: Optional[HttpUrl] = Field(None, description="Website URL for the service")
    service_area: Optional[str] = Field(None, description="Geographical area where the service is offered")
    service_start_date: Optional[date] = Field(None, description="Start date of the service availability")
    service_end_date: Optional[date] = Field(None, description="End date of the service availability")
    features: Optional[List[str]] = Field(None, description="List of features or benefits of the service")


class Company(JsonModel, extra=Extra.allow):
    name: str = Field(..., description="Name of the company", index=True)
    vision: Optional[str] = Field(None, description="Vision of the company")
    mission: Optional[str] = Field(None, description="Mission of the company")  
    description: Optional[str] = Field(None, description="Description of the company")
    company_culture: Optional[str] = Field(None, description="company culture")
    values: Optional[Dict] = Field(None, description="company values")
    industry: Optional[str] = Field(None, description="Industry the company operates in")
    founded: Optional[int] = Field(None, description="Year the company was founded")
    num_employees: Optional[int] = Field(None, description="Number of employees in the company")
    headquarters: Optional[str] = Field(None, description="Location of the company's headquarters")
    website: Optional[HttpUrl] = Field(None, description="Website URL of the company")
    email: Optional[EmailStr] = Field(None, description="Contact email of the company")
    phone: Optional[str] = Field(None, description="Contact phone number of the company")
    address: Optional[str] = Field(None, description="Physical address of the company")
    social_media: Optional[dict] = Field(None, description="Social media links of the company")
    products: Optional[List[str]] = Field(None, description="List of references to products offered by the company")
    services: Optional[List[str]] = Field(None, description="List of references to services offered by the company")


    def get_contact_info(self) -> str:
        contact_info = f"Email: {self.email}, Phone: {self.phone}"
        return contact_info

    def get_summary(self) -> str:
        summary = (
            f"Company Name: {self.name}\n"
            f"Industry: {self.industry}\n"
            f"Founded: {self.founded}\n"
            f"Number of Employees: {self.num_employees}\n"
            f"Headquarters: {self.headquarters}\n"
            f"Website: {self.website}\n"
        )
        return summary
    
    def __str__(self):
        return '\n'.join({f"{k.upper()} : {v}" for k,v in self.dict().items() if v and k!='pk'})





### Models used by Pickey
class Question(EmbeddedJsonModel):
    qnum: str
    question: str
    category: Optional[str]
    skill: Optional[str]
    options: Optional[List[str]] # for multiple choice questions

    def __str__(self):
        return f"{self.question}\n"+'\n'.join(f"{i}: {o}" for i,o in enumerate(self.options)) if self.options else f"{self.question}"
    
    def __str_with_skills__(self):
        qstr = f"Q: {self.question}\nCAT: {self.category}\nSKILL: {self.skill}"
        return qstr+'\nOPTIONS:\n'+'\n'.join(f"{i}: {o}" for i,o in enumerate(self.options)) if self.options else qstr



class Questionnaire(EmbeddedJsonModel):
    questions: List[Question]
    def __str__(self):
        return  f"Questions: ({len(self.questions)})\n"+'\n\n'.join(str(q) for q in self.questions)
    def __str_with_skills__(self):
        return  f"Questions: ({len(self.questions)})\n"+'\n\n'.join(q.__str_with_skills__() for q in self.questions)



# Evaluation of a CV by the Evaluator agent
class CVEvaluation(JsonModel):
    candidate: str = Field(index=True)# candidate pk
    company: Optional[str] = ""# company ref
    jobdesc: Optional[str] = ""# job description reftr
    skills_evaluation : List[Dict[str, List[Dict[str, str]]]]
    grade: str
    summary: str

# Interview contents
class Interview(JsonModel):
    date: float # unix epoch
    candidate: str = Field(index=True)
    job_description: str = Field(index=True) # Link to Job description
    questions: Questionnaire # interview questions
    interview: List[LLMMessage] = []
    evaluation: List[Dict] = []

    def __str__(self):
         return self.questions.__str_with_skills__()+"\n\nINTERVIEW:\n".join([f"{msg.role}: {msg.content}" for msg in self.interview])



class Candidate(JsonModel, extra=Extra.allow):
    name: str = Field(index=True)
    resume: str
    resume_classified: Optional[Dict] # processed resume with a local model
    jobs_applied: List[str] = [] # list of job references the candidate applied for 
    interviews: List[str] = [] # reference to interviews (pk)
    questions: Optional[Questionnaire]# questions generated for the candidate only (not a vacancy)

    def __str__(self):
        if self.resume_classified:
            return '\n'.join({f"{k.upper()} : {v}" for k,v in self.resume_classified.items() if v})
        else:
            return self.resume


class JobDescription(JsonModel, extra=Extra.allow):
    reference: str = Field(index=True)
    job_title: str
    company: str = Field(index=True) # Reference to the company
    job_description: Optional[str]
    active: bool = True # whether the job listing is still active
    questions: Optional[Questionnaire] # job-only questions

    def __str__(self):
         return '\n'.join({f"{k.upper()} : {v}" for k,v in self.dict().items() if v and k!='pk'})







# Wrapper for langroid agents
class Agent(BaseModel):
    agent: lr.ChatAgent
    task: lr.Task = None
    msgs: int = 0
    class Config:
        arbitrary_types_allowed = True

### Models for Kopi

### Models for Lumina

### Other Models

# Define the ANSI escape sequences for various colors and reset
class Colors(BaseModel):
    RED: str = "\033[31m"
    BLUE: str = "\033[34m"
    GREEN: str = "\033[32m"
    ORANGE: str = "\033[33m"  # no standard ANSI color for orange; using yellow
    CYAN: str = "\033[36m"
    MAGENTA: str = "\033[35m"
    YELLOW: str = "\033[33m"
    BLACK: str = "\033[30m"
    RESET: str = "\033[0m"

