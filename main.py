from Quote_Game import QuotesQuizGame

score = 0
game = QuotesQuizGame()
is_playing = True


def print_quote(quote):
    print('\n')
    print("*--------------------------------------------------*")
    print(quote)
    print("*--------------------------------------------------*")
    print('\n')


def print_hint(author, author_bio, hint):
    if hint == 3:
        author_bio = game.get_author_bio(author_bio)
        return f"The author was born on {author_bio['author_born_date']} {author_bio['author_born_location']}"
    elif hint == 2:
        return f"The first character in the first name of the author is {game.author_name_hint(author)['first_name']}"
    elif hint == 1:
        return f"The first character in the last name of the author is {game.author_name_hint(author)['last_name']}"


while is_playing:
    hints = 3
    quote = game.get_quote()
    if quote == None:
        print("You have finished the game! Thank You for playing :)")
        break
    quote_txt = quote["quote_text"]
    author = quote["author"]
    author_bio = quote["author_bio"]

    print_quote(quote_txt)
    user_guess = input("Who do you think, wrote the above line? : ")
    guess = 1
    while user_guess != author and hints > 0:
        hint_text = print_hint(author, author_bio, hints)
        user_guess = input(hint_text + " : ")
        hints -= 1
        guess += 1
    if user_guess == author:
        print(f"You got it right in {guess} guess!")
    else:
        print(f"Sorry! you ran out of hints! The correct ans was {author}")

    keep_playing = input("Do you want to keep playing? (Y/N) : ").lower()

    if keep_playing == 'n':
        is_playing = False
