import game_data
import random
import art

# a func to pick a randon celebrate
def random_person():
    """return a random celebrate from the game data dictionary"""
    person = random.choice(list(game_data.data))
    return person

def print_info(name):
    """a print func of the info of the celeb """
    print(f'{name["name"]}, a {name["description"]}, from {name["country"]}.')


def who_has_more(num1, num2):
    if num1["follower_count"] > num2["follower_count"]:
        return "a"
    else:
        return "b"




# pick 2 random celebrate
def game():
    final_score = 0
    game_over = False

    while game_over == False:

    # pick 2 random celebrate
        person1 = random_person()
        person2 = random_person()
        print(art.logo)
        print("Compare A: ")
        print_info(person1)
        print(art.vs)
        print("Against B: ")
        print_info(person2)

        user_answer = input("Who has more followers? Type 'A' or 'B':").lower()
        right_answer = who_has_more(person1, person2)

        print("\n" * 20)

        if user_answer == right_answer:
            final_score+= 1
        else:
            print(f"Sorry, that's wrong. Final score: {final_score}")
            game_over = True


game()





