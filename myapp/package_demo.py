"""示範如何使用自建套件 mytools：finance 與 web 兩個子套件。"""

from mytools import APIClient, APIError, get_json
from mytools.finance import BankAccount

BASE_URL = "https://jsonplaceholder.typicode.com"


def demo_bank_account():
    print("=== 0. 子套件：mytools.finance.BankAccount ===")
    acc = BankAccount("Jay", 100)
    acc.deposit(50)
    print(acc.get_balance())


def demo_get_json():
    print("=== 1. 函式：get_json ===")
    todo = get_json(f"{BASE_URL}/todos/1")
    print(todo["title"])


def demo_api_client():
    print("=== 2. 類別：APIClient（共用 base_url 與連線）===")
    with APIClient(BASE_URL) as api:
        posts = api.get("/posts", params={"userId": 1})
        print(len(posts), posts[0]["title"])

        created = api.post(
            "/posts", data={"title": "hello", "body": "from myapp", "userId": 1}
        )
        print(created)


def demo_api_error():
    print("=== 3. 錯誤處理：APIError ===")
    try:
        get_json(f"{BASE_URL}/not-exist")
    except APIError as e:
        print("捕捉到 APIError：", e)


def main():
    demo_bank_account()
    demo_get_json()
    demo_api_client()
    demo_api_error()


if __name__ == "__main__":
    main()
