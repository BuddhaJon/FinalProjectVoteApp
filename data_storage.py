import csv
from typing import Dict, Set

FILE_NAME = 'results.csv'

def append_session_results(votes: Dict[str, int], voter_id: int) -> None:
    """Append the current session's results along with the voter ID."""
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([voter_id, votes.get('John', 0), votes.get('Jane', 0)])

def load_votes() -> Dict[str, int]:
    """Load votes, assuming structure has voter ID, John's votes, and Jane's votes."""
    votes = {"John": 0, "Jane": 0}
    try:
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:  # Ensuring there are exactly three elements: ID, John's votes, Jane's votes
                    try:
                        votes['John'] += int(row[1])
                        votes['Jane'] += int(row[2])
                    except ValueError:
                        continue  # Skip rows where conversion to int fails
    except FileNotFoundError:
        pass  # If the file doesn't exist, return the default votes dict
    return votes

def load_ids() -> Set[int]:
    """Load voter IDs to track previous voters."""
    ids = set()
    try:
        with open(FILE_NAME, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ensuring the row is not empty
                    try:
                        ids.add(int(row[0]))
                    except ValueError:
                        continue  # Skip rows where ID conversion fails
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty set
    return ids
