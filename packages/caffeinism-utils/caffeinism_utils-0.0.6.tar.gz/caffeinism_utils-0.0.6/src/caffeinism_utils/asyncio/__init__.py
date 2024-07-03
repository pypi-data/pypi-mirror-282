import asyncio
from functools import partial


def run_in_threadpool(func, *args, **kwargs):
    return run_in_executor(None, func, *args, **kwargs)


def run_in_executor(pool, func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    func = partial(func, *args, **kwargs)
    return loop.run_in_executor(pool, func)


class GracefulTerminator:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def handle(self, *args):
        async with self.lock:
            loop = asyncio.get_running_loop()
            loop.stop()

    @property
    def do_not_disturb(self):
        return self.lock

    def __call__(self, *args):
        return asyncio.create_task(self.handle(*args))
