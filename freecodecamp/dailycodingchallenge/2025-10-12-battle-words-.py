

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

'''Battle of Words

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

    The given sentences will always contain the same number of words.
    Words are separated by a single space and will only contain letters.
    The value of each word is the sum of its letters.
    Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
    A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
    Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
    A word wins if its value is greater than the opposing word's value.
    The team with more winning words is the winner.

Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
'''

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


'''
1. battle("hello world", "hello word") should return "We win".
2. battle("Hello world", "hello world") should return "We win".
3. battle("lorem ipsum", "kitty ipsum") should return "We lose".
4. battle("hello world", "world hello") should return "Draw".
5. battle("git checkout", "git switch") should return "We win".
6. battle("Cheeseburger with fries", "Cheeseburger with Fries") should return "We lose".
7. battle("We must never surrender", "Our team must win") should return "Draw".
'''