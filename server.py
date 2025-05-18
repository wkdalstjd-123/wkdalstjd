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
            # ✅ 보낸 사람 포함 모든 클라이언트에게 메시지 전송
            for client in clients:
                await client.send_text(data)
    except:
        clients.remove(websocket)

@app.get("/")
def get():
    return HTMLResponse("WebSocket server is running.")


