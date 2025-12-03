import queue

request_queue = queue.Queue()
request_counter = 0
def generate_request():
    global request_counter
    request_counter +=1
    new_request = f"Order №{request_counter}"
    request_queue.put(new_request)
    print(f"Make and add:{new_request}.Queue size:{request_queue.qsize()}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Order processing:{request}")
        request_queue.task_done()
        print(f"Order:{request} processing good.")
    else:
        print("No orders")

generate_request()
process_request()





