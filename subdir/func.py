# test loading repo from git in different mlrun runtimes
# contain function code (this) and locally imported lib (mylib)

from mylib import myfunc

tag = "refs/heads/tst"

# mlrun job runtime entry
def job_handler(context):
  myfunc()
  context.log_result("tag", tag)

# mlrun nuclio runtime entry
def nuclio_handler(context, event):
    myfunc()
    return context.Response(body=f'tag={tag}',
                            headers={},
                            content_type='text/plain',
                            status_code=200)

# mlrun serving runtime entry
def echo(event):
    myfunc()
    return f'tag={tag}'
  
# serving runtime hooks
from mlrun.runtimes import nuclio_init_hook

def init_context(context):
    nuclio_init_hook(context, globals(), "serving_v2")

def handler(context, event):
    return context.mlrun_handler(context, event)
