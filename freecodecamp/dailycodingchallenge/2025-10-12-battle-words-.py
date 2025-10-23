

def count_words(words):
    words_values = []
    for word in words:
        word_value = 0
        for letter in word:
            letter_val = ord(letter)
            if (letter_val > 96):
                word_value += letter_val -96
            else:
                word_value += (letter_val -64)*2
        
        words_values.append(word_value)
    return words_values


def battle(our_team, opponent):
    msg_win = "We win"
    msg_lose = "We lose"
    msg_draw = "Draw"

    team_you = 0
    
    our_team_words_values = count_words(our_team.split())

    team_them = 0
    opponent_words_values = count_words(opponent.split())

    battle_winner = 0
    for i in range(len(our_team_words_values)):
        battle = our_team_words_values[i] - opponent_words_values[i]
        if (battle > 0 ):
            battle_winner += 1
        elif (battle < 0):
            battle_winner -= 1

    if (battle_winner < 0):
        return msg_lose
    elif (battle_winner > 0):
        return msg_win
    else:
        return msg_draw


if __name__ == "__main__":
    print(battle("hello world", "hello word"))
    print(battle("lorem ipsum", "kitty ipsum"))


