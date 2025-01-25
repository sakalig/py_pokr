import sys
import requests
import json

def main():
    if len(sys.argv) == 2:
        # TODO: Process arguments to be viable search string
        # Proceed to append
        print("Searching artists' songs...")
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=8&term=" + sys.argv[1])
        j = response.json()
        # For dev consumption
        print(json.dumps(j, indent=2))

        for result in j["results"]:
            print(result["trackName"])
    elif len(sys.argv) > 2:
        print("Kindly pass multiple arguments within quotes")
    else:
        pass

if __name__ == "__main__":
    main()