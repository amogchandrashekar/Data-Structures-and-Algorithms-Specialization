# python3


def read_input():
    """
    Helper function to read input from the user
    """
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    """
    Helper function to print output
    """
    print(' '.join(map(str, output)))


class RabinKarp:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.p_length = len(pattern)
        self.compute = len(text) - len(pattern) + 1
        self.hash_table = list()
        self.answer = list()

    def get_hash(self, text_string):
        """
        Returns hash value computed for the input string
        """
        return sum([ord(letter) for letter in text_string])

    def precompute_hash(self):
        """
        Function to compute hash values to all the substrings(of the length pattern) in the string
        """
        self.hash_table = [self.get_hash(self.text[:self.p_length])]
        for index in range(1, self.compute):
            self.hash_table.append(self.hash_table[index - 1] - ord(self.text[index - 1]) + ord(self.text[index + self.p_length - 1]))

    def hash_substring(self):
        """
        Main function to find indices at which substring is found in the string
        """
        pattern_hash = self.get_hash(self.pattern)
        self.precompute_hash()
        for index in range(0, self.compute):
            if self.hash_table[index] == pattern_hash and self.text[index : index + self.p_length] == self.pattern:
                self.answer.append(index)
        return print_occurrences(self.answer)


if __name__ == '__main__':
    pattern, text = input().rstrip(), input().rstrip()
    rk = RabinKarp(pattern, text)
    rk.hash_substring()

