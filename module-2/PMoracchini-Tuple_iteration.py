
# Patrice Moracchini
# 09/14/2025
# Description:  This program demonstrates the use of a tuple in Python.
# It initializes a tuple named 'playlist' with singers' names,
# displays the contents in a single statement, then iterates
# through the collection displaying formatted sentences using f-strings.
# Finally, the program repeats the output in reverse order
# with a different context string.


def main():
    # Step 1: Initialize a Tuple named 'playlist' with 20 singers
    playlist = (
        "Taylor Swift", "Beyoncé", "Ed Sheeran", "Adele", "Bruno Mars",
        "Ariana Grande", "Lady Gaga", "Justin Bieber", "Billie Eilish", "Rihanna",
        "Katy Perry", "Harry Styles", "Shawn Mendes", "Selena Gomez", "Sam Smith",
        "Dua Lipa", "Sabrina Carpenter", "Madonna", "Drake", "The Weeknd"
    )

    # Step 2: Display the contents in a single statement
    print("Playlist of popular singers:")
    print(playlist)  

    print("\n--- Singers in Sentences ---")
    # Step 3: Iterate through and display each value as a complete sentence
    for singer in playlist:
        print(+f"{singer} is one of the most well-known singers in the world.")

    print("\n--- Singers in Reverse Order (Different Context) ---")
    # Step 4: Repeat in reverse order, different f-string context
    for singer in reversed(playlist):
        print(f"If I could go to a concert, I would love to see {singer} perform live.")

# Run the program
if __name__ == "__main__":
    main()