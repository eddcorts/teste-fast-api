from typing import Optional
from datetime import datetime as dt

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    time = dt.now()
    
    with open('conexoes.log', 'r+') as logs:
        for line in logs:
            pass
        idx, _ = line.split(': ') if line.strip() else ('0', '')
        
        logs.write(f"{int(idx)+1}: {time}\n")
        
    return {
        "eae": "gay",
        "n_acessos": int(idx) + 1
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
