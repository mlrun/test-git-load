# test loading repo from git in different mlrun runtimes
# contain function code (this) and locally imported lib (mylib)

from rootlib import myfunc

tag = "main"

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
