import logging

from mytools import BankAccount, log_call

# 使用端負責設定 log 要輸出到哪裡、什麼格式（模組本身不設定）
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)


print("=== 1. 不帶參數：@log_call ===")


@log_call
def add(a, b):
    return a + b


add(10, 20)
print("函式名稱仍是：", add.__name__)  # functools.wraps 保留原名稱


print("=== 2. 帶參數：@log_call(...) ===")


@log_call(level=logging.DEBUG, log_result=False)
def load_prices(symbol, days=30):
    return list(range(days))


load_prices("2330", days=500)


print("=== 3. 例外：記錄 traceback 後重新拋出 ===")


@log_call
def divide(a, b):
    return a / b


try:
    divide(1, 0)
except ZeroDivisionError:
    print("呼叫端仍然收到 ZeroDivisionError")


print("=== 4. 裝飾 method、指定 logger ===")

audit = logging.getLogger("audit")


class Account(BankAccount):
    @log_call(logger=audit)
    def deposit(self, amount):
        super().deposit(amount)


acc = Account("Jay", 100)
acc.deposit(50)
print("餘額：", acc.get_balance())
