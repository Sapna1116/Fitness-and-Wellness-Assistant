# Pydantic is a data validation library that uses Python type annotations to define data schemas. In our FastAPI application, we use Pydantic models to define the structure of our request and response data. 
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    GPT4_O = "gpt-4o"
    GPT4_O_MINI = "gpt-4o-mini"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GPT4_O_MINI)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime
    # file_size: int  # New field
    # content_type: str  # New field

class DeleteFileRequest(BaseModel):
    file_id: int
