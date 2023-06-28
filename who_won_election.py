# Who Won the Election - Codewars 6kyu

"""
There are no given candidates. An elector can vote for anyone. Each ballot contains only one name and represents one vote for this name. A name is an arbitrary string, e.g. "A", "B", or "XJDHD". There are no spoiled ballots.

The ballot-box is represented by an unsorted list of names. Each entry in the list corresponds to one vote for this name. You do not know the names in advance (because there are no candidates).

A name wins the election if it gets more than n / 2 votes (n = number of all votes, i.e. the size of the given list).

Examples
# 3 votes for "A", 2 votes for "B"  -->  "A" wins the election
["A", "A", "A", "B", "B"]  -->  "A"

# 2 votes for "A", 2 votes for "B"  -->  no winner
["A", "A", "B", "B"]  -->  None / nil / null

"""

# My Solution

def get_winner(ballots):
    # dict to hold vote count for each candidate
    votes = {}
    # Loop to increment count for each candidate
    for ballot in ballots:
        votes[ballot] = 1 + votes.setdefault(ballot, 0)
    # Find the candidate with the highest number of votes
    winner = max(votes, key=votes.get)
    # Check to see if the number of votes for the winner is the majority, if not - return None
    return winner if votes[winner] > len(ballots)/2 else None

# Solution Using Set and Count

def getWinner(b):
    for c in set(b):
        if b.count(c) * 2 > len(b):
            return c