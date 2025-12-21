"""
Patrice Moracchini
CSD-325 Module 9.2 - API Tutorial Program
This program tests the connection, finds current astronauts
Then prints raw response (no formatting) and finally prints formatted response in a tutorial format.
"""

import json
import sys
import requests


ASTROS_URL = "http://api.open-notify.org/astros.json"


def test_connection(url: str) -> None:
    print("*** CONNECTION TEST ***")
    try:
        response = requests.get(url, timeout=10)
        print(f"GET {url}")
        print(f"Status code: {response.status_code}")
        print(f"OK: {response.ok}")
        print()
    except requests.RequestException as exc:
        print(f"Connection test failed: {exc}")
        sys.exit(1)

# Function to get response from the API
def get_response(url: str) -> requests.Response:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        sys.exit(1)

# Function to print raw response
def print_raw_response(response: requests.Response) -> None:
    print("*** RESPONSE (NO FORMATTING) ***")
    # This prints exactly what the server returned without any formatting (difficult to read, text not separated by new lines,
    # everything is in one line)
    print(response.text)
    print()

# Function to print formatted response
def print_formatted_astronauts(response: requests.Response) -> None:
    print("*** FORMATTED RESPONSE ***") # way prettier, with new lines, indentations and signets.
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Error: Response was not valid JSON.")
        sys.exit(1)

    number = data.get("number", 0)
    people = data.get("people", [])

    print(f"Number of people in space: {number}")
    print("People currently in space:")

    for person in people:
        name = person.get("name", "Unknown")
        craft = person.get("craft", "Unknown")
        print(f" - {name} ({craft})")

    print()


def main() -> None:
    test_connection(ASTROS_URL)

    resp = get_response(ASTROS_URL)

    # print out response with no formatting
    print_raw_response(resp)

    # print out response with formatting like tutorial
    print_formatted_astronauts(resp)


if __name__ == "__main__":
    main()