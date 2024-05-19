# Rock-Paper-Scissors solution for freeCodeCamp Machine Learning with Python certification

def player(prev_play, opponent_history=[], opponent_plays={}, games=5):
    strategy = {'P': 'S', 'R': 'P', 'S': 'R'}

    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    prediction = 'S'

    if len(opponent_history) >= games:
        last_games = "".join(opponent_history[-games:])
        opponent_plays[last_games] = opponent_plays.get(last_games, 0) + 1

        combinations = ["".join(opponent_history[-(games - 1):] + [rps]) for rps in ["R", "P", "S"]]

        sequence_counts = {sequence: opponent_plays[sequence] for sequence in combinations if
                           sequence in opponent_plays}

        if sequence_counts:
            most_common_sequence = max(sequence_counts, key=sequence_counts.get)
            prediction = most_common_sequence[-1:]

    return strategy[prediction]
