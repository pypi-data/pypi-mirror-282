from fastapi import Request
from fastapi.responses import StreamingResponse
import aiohttp

async def proxy_request(request: Request, *, endpoint: str = 'https://localhost', uds_path: str):
  connector = aiohttp.UnixConnector(path=uds_path)
  session = aiohttp.ClientSession(connector=connector)
  
  try:
    response = await session.request(
      method=request.method,
      url=endpoint + request.url.path,
      headers=request.headers,
      data=await request.body()
    )

    async def stream_response(response):
      async for chunk in response.content.iter_any():
        yield chunk
      await session.close()

    return StreamingResponse(
      stream_response(response),
      status_code=response.status,
      headers=dict(response.headers)
    )
  except Exception as e:
    await session.close()
    raise e