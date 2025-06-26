from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def home(): return

@app.get("/download")
async def get_link(filename: str):
    # Link đích có thể là local hoặc external
    file_url = f"http://localhost:8000/download/{filename}"  # hoặc link Google Drive, v.v
    return RedirectResponse(url=file_url)
