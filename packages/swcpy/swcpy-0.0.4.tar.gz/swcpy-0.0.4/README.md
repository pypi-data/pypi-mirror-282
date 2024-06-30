# swcpy software development kit (SDK)
This is an example python SDK to to interact with the SportsWorldCentral Football API. This code is for educational purposes.

## Example Usage

To call the SDK functions for normal API endpoints, here is an example:

```python
from swcpy import SWCClient
from swcpy import SWCConfig

config = SWCConfig(url="http://127.0.0.1:8000",backoff=False)
client = SWCClient(config)    
response = client.get_health_check()
print(response)
```

