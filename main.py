from fastapi import  FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine

app = FastAPI()

app.title = "YoshinoGames Api"
app.description = "Api Diseñaada para el proyecto de YoshinoGames"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

@app.get("/", tags=['home'] )
def home ():
    return HTMLResponse(content="<h1>YoshinoGames Api</h1>")
