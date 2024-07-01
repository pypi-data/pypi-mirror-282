# Load Balancer

> Simple FastAPI load balancer

```bash
pip install load-balancer
```

## Usage

```python
from multiprocessing import Process
from fastapi import FastAPI
import uvicorn
from load_balancer import session_affinity, # or round_robin

myapp = FastAPI()
# ...

NUM_WORKERS = 4
UDP_PATHS = [f'udp-{i}.sock' for i in range(NUM_WORKERS)]
balancer = session_affinity(UDP_PATHS)

procs = [Process(target=uvicorn.run, args=(balancer,))] + [
  Process(target=uvicorn.run, args=(myapp, path))
  for path in UDP_PATHS
]

for proc in procs:
  proc.start()

for proc in procs:
  proc.join()
```