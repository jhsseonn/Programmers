def solution(s):
    brackets = []
    for i in range(len(s)):
        if s[i] == "(":
            brackets.append(s[i])
        else:
            if not brackets or brackets.pop() != "(":
                return False

    return len(brackets) == 0
