import os

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
app.mount("/assets", StaticFiles(directory="static/assets"), name="static")
class FormData(BaseModel):
    SNOW_INTENSITY: float
    BACKGROUND_COLOUR: list[int]
    SNOW_COLOUR: list[int]
    FADE_UP_SPEED: int
    FADE_DOWN_SPEED: int

@app.post("/{id}.json")
async def update_data(id, form_data: FormData):
    with open(f"./profiles/{id}.json", "w") as file:
        json.dump(form_data.model_dump(), file, indent=2)
    return {"message": "Data updated successfully"}

@app.post("/presets/{id}.json")
async def update_preset_data(id, form_data: FormData):
    with open(f"./presets/{id}.json", "w") as file:
        json.dump(form_data.model_dump(), file, indent=2)
    return {"message": "Data updated successfully"}

@app.get("/presets")
async def get_all_presets():
     return [a.split(".json")[0] for a in list(os.walk("./presets/"))[0][2]]


@app.delete("/presets/{id}.json")
async def delete_preset_data(id):
    os.remove(f"presets/{id}.json")

@app.get("/{id}.json")
async def get_config(id):
    with open(f"./profiles/{id}.json", "r") as file:
         return json.load(file)


@app.get("/presets/{id}.json")
async def get_preset(id):
    with open(f"./presets/{id}.json", "r") as file:
         return json.load(file)
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)
