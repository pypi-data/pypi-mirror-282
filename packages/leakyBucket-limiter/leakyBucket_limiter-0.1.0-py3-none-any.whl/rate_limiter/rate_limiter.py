import time
import redis

class RateLimiter:

    def __init__(self, redis_host="localhost", redis_port=6739, redis_db=0, bucket_capacity=10, refill_rate=1):

        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
        self.bucket_capacity = bucket_capacity
        self.refill_rate = refill_rate

    def is_allowed(self, user_key):

        current_time = time.time()
        bucket_key = f"busket:{user_key}"
        bucket = self.redis_client.get(bucket_key)

        if bucket is None:
            bucket = {
                "tokens": self.bucket_capacity,
                "last_refill": current_time
            }

        else:
            bucket = eval(bucket)


        elpsed_time = current_time - bucket["last_refill"]
        tokens_to_add = elpsed_time * self.refill_rate
        bucket["tokens"] = min(self.bucket_capacity, bucket["tokens"] + tokens_to_add)
        bucket["last_refill"] = current_time


        if bucket["tokens"] >=1:
            bucket["tokens"] -= 1
            self.redis_client.set(bucket_key, str(bucket))
            return True
        else:
            self.redis_client.set(bucket_key, str(bucket))
            return False