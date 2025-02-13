from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
   a = 2 + 2
   return {"message": "Hello World"}
