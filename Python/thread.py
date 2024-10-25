import threading
import time
def thread_task():
    print("Thread {} is running".format(threading.current_thread().name))
    time.sleep(2)
    print("Thread {} is exiting".format(threading.current_thread().name))
    
def main():
    # 创建线程
    thread1 = threading.Thread(target=thread_task, name='Thread 1')
    thread2 = threading.Thread(target=thread_task, name='Thread 2')
    
    # 启动线程
    thread1.start()
    thread2.start()
    
    # 等待线程执行完成
    thread1.join()
    thread2.join()
    
    print("All threads have finished")

if __name__ == "__main__":
    main()

