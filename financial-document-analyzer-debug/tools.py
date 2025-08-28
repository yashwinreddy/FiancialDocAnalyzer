# tools.py
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools import PDFSearchTool, SerperDevTool

# Creating search tool for general web search
search_tool = SerperDevTool()

class FinancialDocumentTool:
    # Initialize the PDF search tool with Tesla's Q2 financial document
    search_tesla_q2_docs = PDFSearchTool(
        pdf='data/sample.pdf',  # Path to Tesla's Q2 financial PDF
        config=dict(
            llm=dict(
                provider="openai",
                config=dict(
                    model="gpt-3.5-turbo",
                    temperature=0.1,
                ),
            ),
            embedder=dict(
                provider="openai",
                config=dict(
                    model="text-embedding-ada-002",
                ),
            ),
        )
    )

    @staticmethod
    def create_dynamic_pdf_tool(pdf_path: str = 'data/sample.pdf'):
        """
        Create a dynamic PDF search tool for a different/local file
        """
        return PDFSearchTool(
            pdf=pdf_path,
            config=dict(
                llm=dict(
                    provider="openai",
                    config=dict(
                        model="gpt-3.5-turbo",
                        temperature=0.1,
                    ),
                ),
                embedder=dict(
                    provider="openai",
                    config=dict(
                        model="text-embedding-ada-002",
                    ),
                ),
            )
        )
