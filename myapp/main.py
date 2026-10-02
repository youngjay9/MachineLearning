from mytools.finance import BankAccount
acc = BankAccount("Jay", 100)
acc.deposit(50)
print(acc.get_balance())

from mytools import APIClient, APIError, get_json

print("=== 1. 函式：get_json ===")
todo = get_json("https://jsonplaceholder.typicode.com/todos/1")
print(todo["title"])

print("=== 2. 類別：APIClient（共用 base_url 與連線）===")
with APIClient("https://jsonplaceholder.typicode.com") as api:
    posts = api.get("/posts", params={"userId": 1})
    print(len(posts), posts[0]["title"])

    created = api.post("/posts", data={"title": "hello", "body": "from myapp", "userId": 1})
    print(created)

print("=== 3. 錯誤處理：APIError ===")
try:
    get_json("https://jsonplaceholder.typicode.com/not-exist")
except APIError as e:
    print("捕捉到 APIError：", e)
