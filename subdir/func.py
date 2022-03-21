tag = "main"

def job_handler(context):
  context.log_result("tag", tag)
  
def nuclio_handler(context, event):
    return context.Response(body=f'tag={tag}',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
