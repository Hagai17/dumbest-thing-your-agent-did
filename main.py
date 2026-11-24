"""Write one line about the dumbest thing my agent did today to /output/entry.txt.

The line is a single line of at most 200 characters: a concrete, believable
failure from a real working day, with the punch in the last few words.
"""

import os

LINE = "My agent wrote a script to count the files in a folder, ran it 11 times because the count kept climbing, and never noticed the script wrote a new log file on every run."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
