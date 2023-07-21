from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/items/", response_class=HTMLResponse)
async def create_item(request: Request, name: str = None):
    if name is None:
        raise HTTPException(status_code=400, detail="Name field is required")
    return RedirectResponse(url=f"/result/{name}", status_code=302)

@app.get("/result/{name}", response_class=HTMLResponse)
def show_result(name: str, request: Request):
    return templates.TemplateResponse("result.html", {"request": request, "name": name})




