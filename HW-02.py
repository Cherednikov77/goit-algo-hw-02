import queue
request_queue = queue.Queue()
request_counter = 0
def generation_request():
    global request_counter
    request_counter +=1
    new_request = f"Order №{request_counter}"
    request_queue.put(new_request)
    print(f"Make and add:{new_request}.Order:{request_counter}")

#####
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Order processing:{request}")
        request_queue.task_done()
        print(f"Order:{request} processing good.")
    else:
        print("No orders")






Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
