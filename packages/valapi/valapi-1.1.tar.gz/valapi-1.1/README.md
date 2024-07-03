# valclient.py

### API wrapper for VALORANT's client API

## Installation
```python
pip install valapi
```

## Example

```python
from valapi import Client

client = Client(region="na")
client.activate()

name = "" #NAME
tag = "" #TAG FOR THE NAME

client.party_invite_by_display_name(name, tag)
```
