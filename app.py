from fastapi import FastAPI, Request, APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Montujemy statyczne pliki (np. CSS, JS) w folderze "static"
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ustawiamy katalog dla szablonów Jinja2 na "templates"
templates = Jinja2Templates(directory="templates")

# Nowa ścieżka dla strony powitalnej
@app.get("/", response_class=HTMLResponse)
async def read_welcome(request: Request):
    return templates.TemplateResponse(
        request=request, name="welcome.html", context={}
    )

@app.get("/home", response_class=HTMLResponse)
async def read_welcome(request: Request):

    return templates.TemplateResponse(
        request=request, name="home.html", context={}
    )

@app.get("/devices_info", response_class=HTMLResponse)
async def read_welcome(request: Request):
    username = "Milosz"
    return templates.TemplateResponse(
        request=request, name="devices_info.html", context={"username": username}
    )
    
@app.get("/devices_control", response_class=HTMLResponse)
async def read_welcome(request: Request):
    return templates.TemplateResponse(
        request=request, name="devices_control.html", context={}
    )

@app.get("/devices_reports", response_class=HTMLResponse)
async def read_welcome(request: Request):
    return templates.TemplateResponse(
        request=request, name="devices_reports.html", context={}
    )


@app.get("/logout", response_class=HTMLResponse)
async def read_welcome(request: Request):

    #logout...
    print("Wylogowano...")

    return RedirectResponse("/")


# Istniejąca ścieżka do strony z pojedynczym przedmiotem (przykład)
@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
