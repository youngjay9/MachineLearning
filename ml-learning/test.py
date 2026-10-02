def log_execution(func):
    def wrapper():
        print("開始執行")
        func()
        print("執行結束")
        
    return wrapper


@log_execution
def create_order():
    print("建立訂單")