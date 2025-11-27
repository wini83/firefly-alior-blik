from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates("templates")

@router.get("/file/{file_id}")
def preview(request: Request, file_id: str):
 
    #ensure_token(request)

    return templates.TemplateResponse("file.html", {
        "request": request,
        "file_id": file_id,
        "step": "preview",
        "page_title": "BLIK CSV File Preview"
    })