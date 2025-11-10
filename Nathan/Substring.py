from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []

        word_counts = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0

            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len

                if word in word_counts:
                    current_counts[word] += 1
                    count += 1

                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                else:
                    current_counts.clear()
                    count = 0
                    left = right
        
        return result