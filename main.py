from typing import Optional
from datetime import datetime as dt

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def main(request: Request):
    ip = request.client.host
    time = dt.now()
    
    with open('conexoes.log', 'r+') as logs:
        for line in logs:
            pass
        idx, *_ = line.split(': ') if line.strip() else ('0', '')
        
        content = f"{int(idx)+1}: {time}: {ip}\n"
        
        logs.write(content)
        print(f"Novo Acesso: {content}")
        
    return {
        "eae": "gay",
        "n_acessos": int(idx) + 1
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    print(f"TEM ALGUEM AQUI!!!! item_id: {item_id} query: {q}")
    return {"item_id": item_id, "q": q}
