import time

def pef_timer(func):
    start = str(time.time_ns())
    func()
    stop = time.time_ns()
    result = stop-start
    print(f'start: {start/1_000_000_000}\nstop: {stop/1_000_000_000}\nresult: {result/1_000_000_000}')
    return func
    