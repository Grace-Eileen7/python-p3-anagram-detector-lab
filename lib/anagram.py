# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the original word in lowercase for consistent comparison
        self.word = word.lower()

    def match(self, words):
        matches = []
        sorted_word = sorted(self.word)

        for candidate in words:
            # Convert candidate to lowercase for case-insensitive comparison
            candidate_lower = candidate.lower()

            # Skip identical words
            if candidate_lower == self.word:
                continue

            # Check if letters match
            if sorted(candidate_lower) == sorted_word:
                matches.append(candidate)

        return matches
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
# Output: ['inlets']
