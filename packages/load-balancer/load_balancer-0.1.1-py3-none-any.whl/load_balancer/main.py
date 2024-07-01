from typing import Sequence
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx
from .uds import proxy_request

def round_robin(uds_paths: Sequence[str], *, endpoint: str = 'http://localhost') -> FastAPI:
  worker = 0
  app = FastAPI()
  @app.route('/{path:path}')
  async def proxy(request: Request):
    nonlocal worker
    uds_path = uds_paths[worker]
    worker = (worker + 1) % len(uds_paths)
    return await proxy_request(request, uds_path=uds_path, endpoint=endpoint)
  
  return app


def session_affinity(uds_paths: Sequence[str], *, endpoint: str = 'http://localhost') -> FastAPI:
  """Uses a cookie to store the client's port assignment."""
  next_worker = 0
  app = FastAPI()

  def safe_path(x):
    try:
      return uds_paths[int(x)]
    except:
      nonlocal next_worker
      uds_path = uds_paths[next_worker]
      next_worker = (next_worker + 1) % len(uds_paths)
      return uds_path

  @app.middleware('http')
  async def session_affinity_middleware(request: Request, _):
    if (worker_cookie := request.cookies.get('assigned-worker')) is None:
      nonlocal next_worker
      uds_path = uds_paths[next_worker]
      next_worker = (next_worker + 1) % len(uds_paths)
    else:
      uds_path = safe_path(worker_cookie)
    response = await proxy_request(request, uds_path=uds_path, endpoint=endpoint)
    if not worker_cookie:
      assigned_worker = str(uds_paths.index(uds_path))
      response.set_cookie('assigned-worker', assigned_worker)
    return response
  
  return app