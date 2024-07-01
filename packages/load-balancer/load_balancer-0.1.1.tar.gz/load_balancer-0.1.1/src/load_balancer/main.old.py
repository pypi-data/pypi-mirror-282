from typing import Sequence
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx

async def proxy_request(request: Request, *, endpoint: str = 'http://localhost', port: int):
  async with httpx.AsyncClient() as client:
    url = f'{endpoint}:{port}{request.url.path}'
    async with client.stream(
      method=request.method,
      url=url,
      headers=request.headers.raw,
      content=await request.body()
    ) as response:
      # Stream the response back to the client
      headers = dict(response.headers)
      return StreamingResponse(
        response.aiter_raw(),
        status_code=response.status_code,
        headers=headers
      )

def round_robin(ports: Sequence[int]) -> FastAPI:
  worker = 0
  app = FastAPI()
  @app.route('/{path:path}')
  async def proxy(request: Request):
    nonlocal worker
    port = ports[worker]
    worker = (worker + 1) % len(ports)
    print(f'Proxying to port {port}')
    return await proxy_request(request, port=port)
  
  return app


def session_affinity(ports: Sequence[int]) -> FastAPI:
  """Uses a cookie to store the client's port assignment."""
  next_worker = 0
  app = FastAPI()

  def safe_port(x):
    try:
      return ports[int(x)]
    except:
      nonlocal next_worker
      port = ports[next_worker]
      next_worker = (next_worker + 1) % len(ports)
      return port

  @app.middleware('http')
  async def session_affinity_middleware(request: Request, _):
    if (worker_cookie := request.cookies.get('assigned-worker')) is None:
      nonlocal next_worker
      port = ports[next_worker]
      next_worker = (next_worker + 1) % len(ports)
    else:
      port = safe_port(worker_cookie)
    response = await proxy_request(request, port=port)
    if not worker_cookie:
      assigned_worker = str(ports.index(port))
      response.set_cookie('assigned-worker', assigned_worker)
    return response
  
  return app