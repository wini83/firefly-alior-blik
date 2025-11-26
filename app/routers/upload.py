from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates("templates")

@router.get("/upload")
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {
        "request": request,
        "title": "Upload CSV",
        "step": "upload"
    })