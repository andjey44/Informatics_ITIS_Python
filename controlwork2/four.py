import threading
import time
arr = []
def func0():
    while True:
        arr.append(input())
def func1():
    while True:
        if arr == True:
            print(arr.pop(0))
        time.sleep(3)
threading.Thread(target=func0).start()
threading.Thread(target=func1).start()