from data_storage import load_votes, append_session_results, load_ids

class VoteManager:
    def __init__(self):
        self.votes = load_votes()
        self.voter_ids = load_ids()  # Load IDs to track who has voted.

    def check_id(self, voter_id: int) -> bool:
        """Check if the voter ID has already voted."""
        return voter_id in self.voter_ids

    def add_vote(self, voter_id: int, candidate: str) -> bool:
        """Add a vote to a specified candidate if the ID is new."""
        if self.check_id(voter_id):
            return False
        if candidate in self.votes:
            self.votes[candidate] += 1
            self.voter_ids.add(voter_id)
            append_session_results(self.votes, voter_id)  # Append with ID
            return True
        return False
