T = 10

for test_case in range(1, T + 1):
    n = int(input())
    string = input()
    long_string = input()
    answer = 0

    if string in long_string:
        answer = long_string.count(string)

    print("#{} {}".format(n, answer))