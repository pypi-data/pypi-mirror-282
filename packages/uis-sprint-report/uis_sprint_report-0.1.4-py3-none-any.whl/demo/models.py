from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List


class Activity(BaseModel):
    title: str = Field(..., description="The title of the activity, summarizing the main goal or purpose of the activity.")
    brief_desc_status: str = Field(..., description="A short and concise description of the status activity, summarizing its main status.")
    status: str = Field(..., description="The current status of the activity, indicating its progress such as 'Planned', 'InProgress', or 'Completed'.")


class SprintReport(BaseModel):
    activities: List[Activity] = Field(..., description="A list of main activities, each described with a title, brief description status, and current status, summarizing the sprint's progress.")


class ResponseModel(BaseModel):
    response: str = Field(..., description="The response to the user query, providing the requested information.")