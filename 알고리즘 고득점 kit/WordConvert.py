from collections import deque


def solution(begin, target, words):
    queue = deque()
    words_length = len(words)
    word_length = len(begin)

    def valid_to_convert(word, node_word):
        count_diff = 0
        for i in range(word_length):
            if word[i] != node_word[i]:
                count_diff += 1
        if count_diff == 1:
            return True
        else:
            return False

    def bfs():
        queue.append((begin, 0))

        if target not in words:
            return 0

        while queue:
            word, depth = queue.popleft()

            if word == target:
                return depth

            for node in words:
                if valid_to_convert(word, node):
                    queue.append((node, depth + 1))

    answer = bfs()

    return answer
