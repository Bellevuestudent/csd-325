# Patrice Moracchini
# CSD-325
# Module 12.2 Assignment
# 12/21/2025
# This program fetches and displays information about planets from the SWAPI (Star Wars API).

import sys
import json
import requests

# When i tried  to  test the connection to SWAPI at first I got this error: (CERTIFICATE_VERIFY_FAILED … certificate has expired) 
#I had to find an alternative address for the SWAPI to make it work, and found it on this website: https://swapi.py4e.com/

BASE_URL = "https://swapi.py4e.com/api"
PLANETS_URL = f"{BASE_URL}/planets/"
TIMEOUT_SECONDS = 10

# Function to test the connection to the API
def test_connection(url: str) -> None:
    print("*** CONNECTION TEST ***")
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
        print(f"GET {url}")
        print(f"Final URL: {response.url}")
        print(f"Status code: {response.status_code}")
        print(f"OK: {response.ok}")
        print()
    except requests.RequestException as exc:
        print(f"Connection test failed: {exc}")
        sys.exit(1)

# Function to get response from the API
def get_response(url: str, params=None) -> requests.Response:
    try:
        response = requests.get(url, params=params, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        sys.exit(1)

# Function to print raw response
def print_raw_response(response: requests.Response) -> None:
    print("===========RESPONSE (NO FORMATTING)===========")
    # print the raw data from the server
    print(response.text)
    print()

# Function to print formatted planet list (SWAPI /planets/)
def print_formatted_planets(response: requests.Response) -> None:
    print("===========FORMATTED RESPONSE============")
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Error: Response was not valid JSON.")
        sys.exit(1)

    count = data.get("count", 0)
    results = data.get("results", [])
    next_url = data.get("next")

    print(f"Total planets (count): {count}")
    print(f"Planets returned on this page: {len(results)}")
    if next_url:
        print(f"Next page: {next_url}")
    print("Planets:")

    for planet in results:
        name = planet.get("name", "Unknown")
        population = planet.get("population", "Unknown")
        climate = planet.get("climate", "Unknown")
        terrain = planet.get("terrain", "Unknown")
        print(f" - {name} | population: {population} | climate: {climate} | terrain: {terrain}")

    print()


def main() -> None:
    test_connection(BASE_URL)

    # If a planet name is provided, search for it; otherwise list the first page of planets.
    if len(sys.argv) > 1:
        planet_name = " ".join(sys.argv[1:]).strip()
        resp = get_response(PLANETS_URL, params={"search": planet_name})
    else:
        resp = get_response(PLANETS_URL)

    # print out response with no formatting
    print_raw_response(resp)

    # print out response with formatting
    print_formatted_planets(resp)


if __name__ == "__main__":
    main()