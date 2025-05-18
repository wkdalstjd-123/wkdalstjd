#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for client in clients:
                if client != websocket:
                    await client.send_text(data)
    except:
        clients.remove(websocket)

@app.get("/")
def get():
    return HTMLResponse("WebSocket Server is running.")

