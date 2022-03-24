tag = "main"

# mlrun serving runtime entry
def echo(event):
    return f'tag={tag}'
  
# serving runtime hooks
from mlrun.runtimes import nuclio_init_hook

def init_context(context):
    nuclio_init_hook(context, globals(), "serving_v2")

def handler(context, event):
    return context.mlrun_handler(context, event)
