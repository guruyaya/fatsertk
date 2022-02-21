from tortoise import run_async

def async_test(func):
    def async_test_wrapper():
        return run_async(func())
    return async_test_wrapper