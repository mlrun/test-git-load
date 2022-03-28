import mlrun
from mylib import myfunc

tag = "main"

if __name__ == "__main__":
    with mlrun.get_or_create_ctx("test_load") as context:
        myfunc()
        context.log_result("tag", tag)
