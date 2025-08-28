# 📊 Financial Report Analyzer (FastAPI + CrewAI)

An API to analyze and search inside financial reports (PDFs) using **FastAPI**, **CrewAI**, and **OpenAI**.

---

## 🐛 Bugs Found and How They Were Fixed

1. **Missing `.env` Handling**
   - **Bug:** API keys were hardcoded or missing.
   - **Fix:** Added `.env` support using `python-dotenv`. Now `OPENAI_API_KEY` and `CREWAI_API_KEY` are securely loaded.

2. **Wrong Imports**
   - **Bug:** Incorrect imports for CrewAI tools (`pdfsearch_tool` not properly imported).
   - **Fix:** Updated imports to use `from crewai_tools import PDFSearchTool`.

3. **Inefficient Prompts**
   - **Bug:** Original prompts were too verbose and unfocused, leading to irrelevant answers.
   - **Fix:** Rewrote prompts to be concise and role-specific.
     Example:
     ```python
     system_prompt = "You are a financial analyst. Summarize the uploaded financial report focusing on revenue, expenses, and key insights."
     ```

4. **PDF Handling**
   - **Bug:** Uploaded PDF was not read correctly by CrewAI.
   - **Fix:** Ensured file saving, path handling, and correct parsing via `PDFSearchTool`.

5. **FastAPI Response Issues**
   - **Bug:** API endpoints sometimes returned raw Python objects.
   - **Fix:** Ensured all responses return JSON (`JSONResponse` or `dict`).

---

## ⚡ Setup and Usage Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/financial-analyser-fixed.git
cd financial-analyser-fixed


python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key
CREWAI_API_KEY=your_crewai_api_key

uvicorn app:app --reload

## 📖 API Documentation

### 1. Health Check

- **Endpoint:** `GET /`
- **Description:** Returns status of the API.

**Response Example:**
```json
{
  "status": "ok"
}


📖 API Documentation
1. Health Check

Endpoint: GET /

Description: Returns status of the API.

Response:

{ "status": "ok" }

2. Upload and Analyze PDF

Endpoint: POST /analyze-pdf

Description: Uploads a financial report (PDF) and returns analysis summary.

Request Example:

curl -X POST "http://127.0.0.1:8000/analyze-pdf" \
  -F "file=@Tesla_Q2.pdf"


Response Example:

{
  "summary": {
    "revenue": "24.9B (up 10% YoY)",
    "expenses": "18.2B",
    "net_income": "3.1B",
    "key_insights": [
      "Energy storage revenue doubled",
      "Vehicle margins declined",
      "R&D spending increased"
    ]
  }
}

3. Search within PDF

Endpoint: POST /search-pdf

Description: Search for specific terms inside uploaded PDF.

Request Example:

curl -X POST "http://127.0.0.1:8000/search-pdf" \
  -F "file=@Tesla_Q2.pdf" \
  -F "query=revenue growth"


Response Example:

{
  "matches": [
    "Total revenue grew 10% year-over-year...",
    "Revenue from energy storage doubled compared to last quarter..."
  ]
}
