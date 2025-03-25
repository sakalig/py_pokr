import sys
import requests
import json
from constants import get_logo, get_version


def main():
    # Substitute with argparse
    if len(sys.argv) == 2:
        # TODO: Process arguments to be viable search string
        print(get_logo() + " v" + get_version())
        # Proceed to append
        print("Searching artists' songs...")
        # TODO: Simulate fetch request for network timeout tests

        # Handle connection error
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=8&term=" + sys.argv[1])
        if not response:
            print("Response NOT valid")
        j = response.json()
        # For dev consumption
        print(json.dumps(j, indent=2))

        # TODO: Make items selectable
            # ... while True: default selection brackets [ song ] on first list item; listen for user input; update direction respectively
        for result in j["results"]:
            print(result["trackName"])
    elif len(sys.argv) > 2:
        print("Kindly pass multiple arguments within quotes")
    else:
        print("Usage: main.py <search_term>")

def get_api_list():
    print("Fetching API list")


if __name__ == "__main__":
    main()