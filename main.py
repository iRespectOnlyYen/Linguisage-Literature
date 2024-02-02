import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.api_v1 import router as api_v1_router
from fastapi.middleware.cors import CORSMiddleware

from src.core import settings
from src.core.database import db_helper
from src.utils import make_static_folders
from sqladmin import Admin
from src.admin import AdminLiteratureEpub


make_static_folders()
app = FastAPI()
app.title = "Literature"
app.summary = (
    "One of Linguisage microservices that have response for literature management"
)

origins = [
    "http://192.168.31.23:3000",
    "http://93.81.252.160:8001",
    "http://93.81.252.160:7777",
    "http://localhost:3000",
    "http://192.168.31.1:0000",
]

headers = [
    "Authorization",
    "Content-Type",
    "Set-Cookie",
    "Accept",
    "Content-Length",
    "User-Agent",
    "Proxy-Authorization",
    "Proxy-Connection",
    "User-Agent",
    "Access-Control-Allow-Headers",
    "Access-Control-Request-Method",
    "Access-Control-Allow-Origin",
]

method = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
#     allow_headers=headers,
# )
#
app.mount(
    "/static",
    StaticFiles(directory=settings.static_path),
    name="static_files",
)
app.include_router(api_v1_router)


admin = Admin(app, engine=db_helper.engine)
admin.add_view(AdminLiteratureEpub)
