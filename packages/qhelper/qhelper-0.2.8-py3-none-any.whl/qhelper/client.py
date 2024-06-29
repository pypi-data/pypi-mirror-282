from dask.distributed import Client
from .scheduler import init_scheduler

def init_client():
    client = Client()
    futures = {
        "scheduler": client.submit(init_scheduler)
    }

    print(client.dashboard_link)
    return futures