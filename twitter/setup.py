import json
from typing import Dict

credentials: Dict[str, str] = {
    'CONSUMER_KEY': "u5yJQ6iroEtWpzWYlFYPHBpBU",
    'CONSUMER_SECRET': "Rs7GbJm5utyxAKFX8PfldLYoH82lW1eBKrEgYIwI8zbuqKVPTq",
    'ACCESS_TOKEN': "24362380-zUS0onYqF0lNWB82bz9s0gJjQPDA09SgqxJ0pvhC7",
    'ACCESS_SECRET': "hv5M6DnKHW0xYHr2nnPaP5lkLzAzSoKVUS4QUxxhDKAKG"
}

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
