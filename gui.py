import tkinter as tk
from tkinter import messagebox, simpledialog
from vote_manager import VoteManager


class VotingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Voting System')
        self.geometry('350x300')
        self.vote_manager = VoteManager()

        # Initialize with an empty value, which doesn't match any radio button value
        self.selected_candidate = tk.StringVar(value="none")

        self.create_widgets()
        self.update_vote_count_labels()

    def create_widgets(self):
        """Creates widgets for the application."""
        tk.Label(self, text='Voting App', font=('Helvetica', 16)).pack(pady=10)

        # Radio buttons for candidate selection
        tk.Radiobutton(self, text="John", variable=self.selected_candidate, value="John").pack(pady=5)
        tk.Radiobutton(self, text="Jane", variable=self.selected_candidate, value="Jane").pack(pady=5)

        # Button to initiate voting
        tk.Button(self, text='Vote', command=self.prompt_id).pack(pady=10)
        tk.Button(self, text='Exit', command=self.exit_app).pack(pady=10)

        # Labels to display the vote counts
        self.john_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.john_vote_label.pack()
        self.jane_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.jane_vote_label.pack()
        self.total_vote_label = tk.Label(self, text='', font=('Helvetica', 12))
        self.total_vote_label.pack()

    def prompt_id(self):
        """ Prompts for voter ID and processes the vote if a candidate is selected and ID is valid. """
        if self.selected_candidate.get() and self.selected_candidate.get() != "none":
            voter_id = simpledialog.askinteger("Voter ID", "Enter your 4-digit Voter ID:")
            if voter_id and len(str(voter_id)) == 4:
                if not self.vote_manager.check_id(voter_id):
                    self.vote(voter_id)
                else:
                    messagebox.showerror("Error", "Already voted")
            else:
                messagebox.showerror("Error", "Invalid ID. Must be a 4-digit number.")
        else:
            messagebox.showerror("Error", "Please select a candidate.")

    def vote(self, voter_id):
        """Records vote for the selected candidate if the candidate is valid."""
        candidate = self.selected_candidate.get()
        if self.vote_manager.add_vote(voter_id, candidate):
            messagebox.showinfo("Success", "Vote recorded!")
            self.update_vote_count_labels()
        else:
            messagebox.showerror("Error", "Invalid candidate or duplicate ID.")

    def update_vote_count_labels(self):
        """Updates the labels with the current vote counts."""
        votes = self.vote_manager.votes
        self.john_vote_label.config(text=f"John: {votes.get('John', 0)} votes")
        self.jane_vote_label.config(text=f"Jane: {votes.get('Jane', 0)} votes")
        self.total_vote_label.config(text=f"Total: {sum(votes.values())} votes")

    def exit_app(self):
        """Exits the application."""
        self.destroy()


def main():
    app = VotingApp()
    app.mainloop()


if __name__ == "__main__":
    main()
