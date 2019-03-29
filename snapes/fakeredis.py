# TODO: actually find a good mocking library for redis
class FakeRedis():
    def __init__(self):
        self.data = {
            'https://www.charlieharrington.com': 'I am Charlie Harrington blog'
        }

    def set(self, key: str, val: str):
        self.data[key] = val

    def get(self, key: str):
        return self.data[key]

    def exists(self, key: str):
        return key in self.data

    def delete(self, key: str):
        try:
            del self.data[key]
            return True
        except KeyError:
            return True

    def expire(self, key: str, max_age: int):
        pass
