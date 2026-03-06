from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from gemini_ai import generate_workout_plan

app = FastAPI(title="FitBuddy AI")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-plan", response_class=HTMLResponse)
def generate_plan(request: Request,
                  name: str = Form(...),
                  age: int = Form(...),
                  weight: int = Form(...),
                  goal: str = Form(...),
                  intensity: str = Form(...)):

    plan = generate_workout_plan(name, age, weight, goal, intensity)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "plan": plan
    })