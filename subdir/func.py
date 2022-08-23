# Copyright 2022 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# test loading repo from git in different mlrun runtimes
# contain function code (this) and locally imported lib (mylib)

from mylib import myfunc

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
