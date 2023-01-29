from fastapi import FastAPI
import uvicorn
from controller.lancamento_controller import lancamento_route
from controller.relatorio_controller import relatorio_route
from controller.moeda_controller import moeda_route
app = FastAPI()

app.include_router(lancamento_route, prefix="/lancamento", tags=["lancamento"])
app.include_router(relatorio_route, prefix="/relatorio", tags=["relatorio"])
app.include_router(moeda_route, prefix="/moeda", tags=["moeda"])
@app.get("/")
def main():
    return {"Hello", "World"}



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)