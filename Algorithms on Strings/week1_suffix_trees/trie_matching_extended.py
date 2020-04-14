"""
Input Format.
	The first line of the input contains a string Text, the second line contains an integer n,
	each of the following n lines contains a pattern from Patterns = {p 1 , . . . , p n }.
Constraints.
 	1 ≤ |Text| ≤ 10 000; 1 ≤ n ≤ 5 000; 1 ≤ |p i | ≤ 100 for all 1 ≤ i ≤ n; all strings contain only
	symbols A, C, G, T; it can be the case that p i is a prefix of p j for some i, j.
Output Format.
 	All starting positions in Text where a string from Patterns appears as a substring in
	increasing order (assuming that Text is a 0-based array of symbols). If more than one pattern
	appears starting at position i, output i once.

Sample 1.

Input:
	AAA
	1
	AA
Output:
	01
Explanation:
	The pattern AA appears at positions 0 and 1. Note that these two occurrences of the pattern overlap.
"""

# python3
import sys
from collections import defaultdict


def create_trie(patterns):
	"""
	Create trie from the patterns
	"""
	trie = defaultdict(dict)
	counter = 0
	for pattern in patterns:
		current_node, old_index = 0, 0
		pattern += "$"
		for letter in pattern:
			if letter in trie[current_node]:
				current_node = trie[current_node][letter]
			else:
				counter += 1
				trie[current_node][letter] = counter
				current_node = counter
	return trie


def solve(text, patterns):
	"""
	Create trie, check if text spans across the trie and find matches
	"""
	result = set()
	trie = create_trie(patterns)

	def prefix_trie_matching(text, i):
		index, counter_index = 0, 0
		symbol = text[index]
		current_branch = trie[0]
		while True:
			if "$" in current_branch:
				result.add(i) # Comes here when the pattern is read due to defaultdict
			if symbol in current_branch:
				counter_index = trie[counter_index][symbol]
				current_branch = trie[counter_index]
				index += 1
				if index < len(text):
					symbol = text[index]
				else:
					symbol = "|" # if length of text < length of substring, it should return false
			else:
				return

	for index in range(len(text)):
		prefix_trie_matching(text[index:], index)

	return list(result)


if __name__ == "__main__":
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]
	# text = "AAA"
	# patterns = ["AA"]
	ans = solve (text, patterns)
	sys.stdout.write (' '.join (map (str, ans)) + '\n')