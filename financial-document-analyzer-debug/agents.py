import os
from crewai_tools import PDFSearchTool
from crewai import Agent

# Load tool
pdf_tool = PDFSearchTool()

# Define financial analysis agent
pdf_agent = Agent(
    role="Financial Analyst",
    goal="Analyze financial PDF documents like quarterly reports",
    backstory="Expert in financial analysis with the ability to extract insights from reports.",
    tools=[pdf_tool],
    verbose=True
)
