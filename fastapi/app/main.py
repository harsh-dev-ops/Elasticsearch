from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os


from app.api.routers import api_router
from app.api.auth import token
from app.conf.settings import settings

app = FastAPI(title="Elastic Search Fastapi", version="1.0.0")

for folder in ['app/static', 'app/templates']:
    os.makedirs(folder, exist_ok=True)

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='app/static'), name='static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix='/api'
)

app.include_router(
    token.router,
    prefix='',
    tags=['Tokens'],
)