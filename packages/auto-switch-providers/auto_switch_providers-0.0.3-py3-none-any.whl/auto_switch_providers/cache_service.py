from json import dumps
from time import perf_counter

from .services.redis_service import RedisClient


class CacheService:
    def __init__(self, config: dict = None) -> None:
        self.client = None
        if config is not None:
            self.config = config
            start_time = perf_counter()
            self.client = RedisClient(self.config).get_client()
            if self.client:
                try:
                    self.client.ping()
                    self.status = True
                    exec_time = perf_counter() - start_time
                    host_name = self.config.get("host")
                    print(
                        f"⚡️ Redis enabled! (ping: {exec_time*1000:.2f} ms, host: {host_name})"
                    )
                except Exception:
                    self.status = False
                    print("⛔️ Redis disabled!")
                    print(dumps(self.config))
                    pass
