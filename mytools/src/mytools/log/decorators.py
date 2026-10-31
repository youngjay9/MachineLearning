import functools
import logging
import reprlib
import time

# 參數或回傳值太長時（例如很大的 list、DataFrame），只印出縮短後的內容
_repr = reprlib.Repr()
_repr.maxstring = 80
_repr.maxother = 80


def log_call(func=None, *, logger=None, level=logging.INFO, log_args=True, log_result=True):
    """紀錄函式呼叫的共用 decorator。

    會紀錄：呼叫參數、回傳值、執行時間；發生例外時以 ERROR 紀錄 traceback 並重新拋出。

    兩種用法皆可：
        @log_call
        @log_call(level=logging.DEBUG, log_result=False)
    """

    def decorator(function):
        # 沒指定 logger 時，用「被裝飾函式所在的模組名稱」，log 才看得出是誰呼叫的
        log = logger or logging.getLogger(function.__module__)
        name = function.__qualname__

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if log_args:
                params = [_repr.repr(a) for a in args]
                params += [f"{k}={_repr.repr(v)}" for k, v in kwargs.items()]
                log.log(level, "呼叫 %s(%s)", name, ", ".join(params))
            else:
                log.log(level, "呼叫 %s", name)

            start = time.perf_counter()
            try:
                result = function(*args, **kwargs)
            except Exception:
                elapsed = time.perf_counter() - start
                log.exception("%s 發生例外（%.3fs）", name, elapsed)
                raise

            elapsed = time.perf_counter() - start
            if log_result:
                log.log(level, "%s 回傳 %s（%.3fs）", name, _repr.repr(result), elapsed)
            else:
                log.log(level, "%s 完成（%.3fs）", name, elapsed)
            return result

        return wrapper

    # @log_call 不加括號：Python 直接把函式傳進來
    if callable(func):
        return decorator(func)
    # @log_call(...) 有加括號：先回傳 decorator，再由 Python 把函式傳進去
    return decorator
