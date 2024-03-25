import signal
import time


def timeout(seconds):
    def decorator(func):
        def handler(signum, frame):
            raise Exception("Time's out!")
        
        def wrappped(*args):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args)
            finally:
                signal.alarm(seconds)
            return result
        
        return wrappped
    return decorator


@timeout(2)
def useless_function():
    time.sleep(0)
    print("Hello, World!")

try:
    useless_function()
except Exception as error:
    print(error)
