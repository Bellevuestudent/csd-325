"""
sitka_high_low_pm.py
Patrice Moracchini CSD-325
Modified from sitka_highs.py for the High/Low Temperatures assignment.

Changes made:
- Read both high and low temperatures from the CSV file.
- Added a text menu to let the user choose Highs, Lows, or Exit.
- Plots highs in red or lows in blue based on the user's choice.
- Loops until the user chooses to exit.
- Prints an exit message and uses sys.exit() when exiting.
"""

# Import necessary modules
import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

# Read the weather data once at the start
FILENAME = "sitka_weather_2018_simple.csv"


def load_weather_data(filename):
    """Load dates, highs, and lows from a CSV weather file."""
    dates = []
    highs = []
    lows = []

    try:
        # Open the CSV file and create a reader object
        with open(filename, newline="", encoding="utf-8") as f: # Open the file with UTF-8 encoding
            reader = csv.reader(f) # Create a CSV reader object
            
            header_row = next(reader, None) # Read the header row

            # Process each row in the CSV file
            for row in reader:
                # Some rows may be missing or invalid; skip them safely
                try:
                    current_date = datetime.strptime(row[2], "%Y-%m-%d") # Parse the date
                    high = int(row[5]) # Parse the high temperature
                    low = int(row[6]) # Parse the low temperature
                except (ValueError, IndexError):
                    # Skip rows with missing or invalid data
                    continue

                # Append valid data to the lists
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: Could not find data file '{filename}'.")
        sys.exit(1) # Exit the program in case of an error code

    return dates, highs, lows


# Load the data once so it can be reused by the plotting functions
dates, highs, lows = load_weather_data(FILENAME)


def plot_highs():
    """Plot the high temperatures in red."""
    fig, ax = plt.subplots() # Create a new figure and axis for the plot
    ax.plot(dates, highs, c="red") # Plot the high temperatures in red

    # Add titles and labels
    plt.title("Daily high temperatures - 2018", fontsize=24) # Set the title of the plot
    plt.xlabel("", fontsize=16) # Set the x-axis label
    fig.autofmt_xdate() # Automatically format the x-axis dates for better readability
    plt.ylabel("Temperature (F)", fontsize=16) # Set the y-axis label
    plt.tick_params(axis="both", which="major", labelsize=16) # Set the tick parameters for both axes

    plt.show() # Display the plot


def plot_lows():
    """Plot the low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c="blue")

    # Add titles and labels
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def print_menu():
    """Display the menu options."""
    print("\nHigh / Low Temperatures Menu")
    print("----------------------------")
    print("H - Show high temperatures graphic")
    print("L - Show low temperatures graphic")
    print("E - Exit program")


def main():
    """Main program loop."""
    print("Welcome to the Sitka Weather Viewer!")
    print("You can view daily high or low temperatures for 2018.\n")

    # Loop until the user chooses to exit
    while True:
        print_menu()
        choice = input("Enter your choice (H, L, or E): ").strip().upper() # Get user input without outer spaces and in uppercase.

        if choice == "H":
            plot_highs()
        elif choice == "L":
            plot_lows()
        elif choice == "E":
            print("Thank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter H, L, or E.")

# Run the main program loop
if __name__ == "__main__":
    main()