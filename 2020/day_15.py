# https://adventofcode.com/2020/day/15


from collections import deque


def play(numbers, end_turn):
    memory = {}
    for turn, n in enumerate(numbers, start=1):
        memory[n] = deque([turn], maxlen=2)
    last_num = numbers[-1]
    for turn in range(turn+1, end_turn+1):
        last_seen = memory[last_num]
        if len(last_seen) == 1:
            last_num = 0
        else:
            last_num = last_seen[1] - last_seen[0]
        if last_num in memory:
            memory[last_num].append(turn)
        else:
            memory[last_num] = deque([turn], maxlen=2)
    print(f"Output for {numbers} on turn {turn} = {last_num}.",
          f"The memory has length {len(memory)}.")
    return last_num


assert play((0, 3, 6), 2020) == 436
assert play((1, 3, 2), 2020) == 1
assert play((2, 1, 3), 2020) == 10
assert play((1, 2, 3), 2020) == 27
assert play((2, 3, 1), 2020) == 78
assert play((3, 2, 1), 2020) == 438
assert play((3, 1, 2), 2020) == 1836

assert play((0, 3, 6), 30000000) == 175594
assert play((1, 3, 2), 30000000) == 2578
assert play((2, 1, 3), 30000000) == 3544142
assert play((1, 2, 3), 30000000) == 261214
assert play((2, 3, 1), 30000000) == 6895259
assert play((3, 2, 1), 30000000) == 18
assert play((3, 1, 2), 30000000) == 362


with open("day_15_input.txt") as file:
    challenge_input = [int(x) for x in file.read().strip().split(",")]
print(play(challenge_input, 2020))  # 240
print(play(challenge_input, 30000000))  # 505
