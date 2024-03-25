from fastapi import FastAPI, Request
from routers.member import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)
app.include_router(router)

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)  # include_in_schema 控制 swagger ui上是否顯示
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
