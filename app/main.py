from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import logs

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://www.jamesresume.online",
    "https://james-resume-av9x.vercel.app"
]

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头
)

app.include_router(logs.router, prefix="/api")
