# encoding: utf-8
# version: redis==5.0.7

import asyncio


class AsyncRedis(object):

    def __init__(self, redis_uri=None, redis_db=None, decode_responses=True):
        from redis import asyncio as aioredis
        self.redis_uri = redis_uri
        self.redis_db = redis_db
        if not redis_uri:
            self.redis_uri = 'redis://localhost:6379'

        if not redis_db:
            self.redis_db = "0"

        self.client = aioredis.Redis.from_url(url=self.redis_uri, db=self.redis_db, decode_responses=decode_responses)
        print(f'init redis client: uri={redis_uri}, db={redis_db}')

    def __str__(self):
        return f"AsyncRedis client at: {self.redis_uri}/{self.redis_db}"

    async def close(self):
        if self.client:
            try:
                await self.client.aclose()
            except Exception as e:
                print(e)


async def test_redis():
    redis_uri = "redis://:Dangerous!@192.168.10.99:6379"
    redis_db = "1"
    aio_rds = AsyncRedis(redis_uri, redis_db)
    print(aio_rds)

    keys = await aio_rds.client.keys("access_to_refresh:*")

    print("keys =", keys[:3])

    await aio_rds.close()


if __name__ == '__main__':
    pass
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_redis())
