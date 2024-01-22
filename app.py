# Necessary Imports
from fastapi import FastAPI  
from fastapi import Request, Form    
from fastapi.responses import RedirectResponse             # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app


# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing
# Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="public")


# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())
    
# Example route: return a static HTML page
@app.get("/library", response_class=HTMLResponse)
def get_library() -> HTMLResponse:
    with open("page.html") as html:
        return HTMLResponse(content=html.read())

# Example route: return a static HTML page
@app.get("/redirect", response_class=HTMLResponse)
def get_redirect() -> HTMLResponse:
    with open("redirect.html") as html:
        return HTMLResponse(content=html.read())

"""
Form: POST Methods
"""
# Example route: return JSON
@app.post("/")
def post_names(request: Request, fname: str = Form(...), lname: str = Form(...)):
    return {"first_name": fname, "last_name": lname}


# Example route: return JSON
@app.post("/beverage")
def post_beverage(request: Request, beverage: str = Form(...)):
    status = "Failed"
    if beverage != '':
        status = "Success"
    return {"favorite beverage": beverage, "Status": status}


# Example route: return JSON
@app.post("/season") #this calls the def after it??
def post_season(request: Request, season: str = Form(...)):
    # Do stuff with the form post here...
    # Redirect to the route /redirect, which is the redirected page
    return RedirectResponse(url="/redirect", status_code=302)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)