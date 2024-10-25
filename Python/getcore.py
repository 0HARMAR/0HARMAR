import os
import multiprocessing

def get_cpu_count():
    try:
        cpu_count = multiprocessing.cpu_count()
        return cpu_count
    except NotImplementedError:
        return os.cpu_count()

if __name__ == "__main__":
    print(f"Number of CPU cores: {get_cpu_count()}")
