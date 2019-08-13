# SesamUtils

**Python module to simplify common tasks when developing microservices for the Sesam integration platform.**


### Usage examples

```bash
from sesamutils import VariablesConfig

required_env_vars = ["username", "password", "hostname"]

config = VariablesConfig(required_env_vars)

if not config.validate():
    sys.exit(1)


```



### Installation

```bash
pip install sesamutils
```