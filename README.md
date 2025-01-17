# SesamUtils

[![Build Status](https://dev.azure.com/sesam-community/Community%20Python%20Packages/_apis/build/status/sesam-community.sesamutils?branchName=master)](https://dev.azure.com/sesam-community/Community%20Python%20Packages/_build/latest?definitionId=1&branchName=master)

**Python module to simplify common tasks when developing microservices for the Sesam integration platform.**


### Usage examples

**Environment Variables**

You can use the VariablesConfig class to load environment variables into your service. It requires a list of required variables. It also support an optional list of variables as a second argument.

```python
from sesamutils import VariablesConfig
import sys

required_env_vars = ["username", "password", "hostname"]
optional_env_vars = ["debug", ("auth_type", "user")] # Default values can be given to optional environment variables by the use of tuples

config = VariablesConfig(required_env_vars, optional_env_vars=optional_env_vars)

if not config.validate():
    sys.exit(1)


print(config.username)

```

**Dotdictify**

A class to help traversing and modifying large nested dictionaries. Lets you navigate by dot notation.

```python
from sesamutils import Dotdictify

example_dict = {
    "test": {
        "my_thing": "hello"
    }
}

dot_dict = Dotdictify(example_dict)

print(dot_dict.test.my_thing)

# hello

```
**Profiler**

 You can use this (A profiling decorator) to see complete details of execution time taken by a function in your program. 
 Based on that, you can optimize your python code if required.

```python
from sesamutils import profiler

@profiler
def <Name of your method>():
    <your method definition>

# Apply to any function with @profiler
# Profiles the function using cProfile, and prints out a report to screen.
# belwo are few lines for illustration  purpose.
ncalls tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.312    0.312 C:/Work/PycharmProjects/node-notification-handler/service/notification-handler.py:143(get_node_members_and_roles)
2    0.000    0.000    0.311    0.156 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\requests\sessions.py:537(get)
2    0.000    0.000    0.311    0.156 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\requests\sessions.py:466(request)
2    0.000    0.000    0.309    0.154 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\requests\sessions.py:617(send)
2    0.000    0.000    0.308    0.154 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\requests\adapters.py:394(send)
2    0.000    0.000    0.306    0.153 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\urllib3\connectionpool.py:446(urlopen)
2    0.000    0.000    0.306    0.153 C:\Users\ravish.ranjan\AppData\Local\Programs\Python\Python36\lib\site-packages\urllib3\connectionpool.py:319(_make_request)
1    0.000    0.000    0.258    0.258 C:\Work\PycharmProjects\node-notification-handler\service\portal.py:34(get_subscription_members)
```

**Sesam Logger**

 You can use this to save time and lines of code. It provides the standard customization of root level logging- 
 configuration and gives you SESAM uniform standard settings.

```python
from sesamutils import sesam_logger

logger = sesam_logger('<name of your module or logger>')

# User can provide environment variable "LOG_LEVEL" with valid values else log level will be 'INFO' by default.
# While logging to screen, timestamp is set to false by default, since sesam-node has it's own. 
# However if you want to make it enable, then you just need to create instance like this:  
      logger = sesam_logger('<name of your module or logger>', timestamp=True)     

```

### Installation

```python
pip install sesamutils
```
