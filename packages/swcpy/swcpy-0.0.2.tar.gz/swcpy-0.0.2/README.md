# swcpy software development kit (SDK)
This is an example python SDK to to interact with the SportsWorldCentral Football API, which was created for the book [Hands-On APIs for AI and Data Science](https://hands-on-api-book.com).

## Example Usage

To call the SDK functions for normal API endpoints, here is an example:

```python
from swcpy import SWCClient
from swcpy import SWCConfig

config = SWCConfig(url="http://127.0.0.1:8000",backoff=False)
client = SWCClient(config)    
leagues_response = client.list_leagues()
print(leagues_response)
```

