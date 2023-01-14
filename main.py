from fastapi import FastAPI
import uvicorn
from controller.lancamento_controller import lancamento_route
app = FastAPI()

app.include_router(lancamento_route, prefix="/lancamento", tags=["lancamento"])

@app.get("/")
def main():
    return {"Hello", "World"}



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)