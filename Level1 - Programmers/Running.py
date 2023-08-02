def solution(players, callings):
    rate = {player: i for i, player in enumerate(players)}

    for c in callings:
        idx = rate[c]
        rate[c] -= 1
        rate[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players