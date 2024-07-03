import unittest
from rate_limiter import RateLimiter
import time

class TestRateLimiter(unittest.TestCase):

    def setUp(self):
        self.rate_limiter = RateLimiter(redis_host="localhost", redis_port="6379", redis_db=0, bucket_capacity=5, refill_rate=1)

    def test_is_allowed(self):
        user_key = "test_user"
        for _ in range(5):
            self.assertTrue(self.rate_limiter.is_allowed(user_key))
        self.assertFalse(self.rate_limiter.is_allowed(user_key))

    def test_rate_limit_reset(self):
        user_key = "test_user"

        for _ in range(5):
            self.rate_limiter.is_allowed(user_key)
        time.sleep(1)
        self.assertTrue(self.rate_limiter.is_allowed(user_key))


if __name__ == '__main__':
    unittest.main()