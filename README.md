# SesamUtils

**Python module to simplify common tasks when developing microservices for the Sesam integration platform.**


### Usage examples

**Environment Variables**
```bash
from sesamutils import VariablesConfig

required_env_vars = ["username", "password", "hostname"]
optional_env_vars = ["debug", ("auth_type", "user")] # Default values can be given to optional environment variables by the use of tuples

config = VariablesConfig(required_env_vars, optional_env_vars=optional_env_vars)

if not config.validate():
    sys.exit(1)


print(config.username)

```

**Dotdictify**
```bash
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
```bash
from profiler import profile

@profile
def get_node_members_and_roles():
    <your method definition>

# Apply to any function with @profile
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
..............................
................................
```

### Installation

```bash
pip install sesamutils
```