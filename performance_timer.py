import time

def pef_timer(func):
    """time the performance of a function that provided in.

    Args:
        func (func): a function to benchmark

    Returns:
        None: None
    """
    start = str(time.time_ns())
    func()
    stop = str(time.time_ns())
    start = float(start)
    stop = float(stop)
    result = stop - start
    print(f'start: {start/1_000_000_000}\nstop: {stop/1_000_000_000}\nresult: {result/1_000_000_000}')
    return None