import random as r


def create_boy_name():
    '''
    Input: NA
    Output: boy_name (string)
    A function to generate a random boy name'''
    prefix = ["Bran","Bil","Jo","chr","Ma","All","Co","Bri","Dev","Dam","Der","Bo"]
    suffix = ["don","ly","sh","is","rk","en","ry","an","in","on","ek","b"]
    return r.choice(prefix) + r.choice(suffix)


def generate_boy_list():
    '''
    Input: NA
    Output: boy_list (list)
    A function for generating a list of 10 random boy names'''
    return [ create_boy_name() for boy in range(10)]


def create_girl_name():
    '''
    Input: NA
    Output: girl_name (string)
    A function to generate a random girl name'''
    prefix = ["A", "Em","Tay","Zo","Gw","Li","Will","Oliv","Ril","Ave","Gra","Qu"]
    suffix = ["va","ma","lor","ey","en","ly","ow","ia","ey","ry","ce","in"]
    return r.choice(prefix) + r.choice(suffix)


def generate_girl_list():
    '''
    Input: NA
    Output: girl_list (list)
    A function for generating a list of 10 random girl names'''
    return [create_girl_name() for girl in range(10)]


def matched_couples(boys,girls,list_len=10):
    '''Input: boys (list)
              girls (list)
              list_len (int)(optional)
       Output: couples (dict)
       A function for a random matching of boys and girls
       into couples{boy : girl, boy: girl, ...}'''
    index = 0
    boy_list = boys.copy()
    girl_list = girls.copy()
    couples = {}
    for num in range(list_len):
        girl = r.choice(girl_list)
        boy = r.choice(boy_list)
        couples[boy] = girl
        girl_list.remove(girl)
        boy_list.remove(boy)
    return couples


def see_guessing_results(guess_dict,answer_dict):
    '''
    Input: guess_dict (dict)
           answer_dict (dict)
    Output: right_answer (int)
    A function to let you know how many matches are right
    (not what matches were right) given a guess, and the answer'''
    right_answer = 0
    for a_key, a_value in answer_dict.items():
        for g_key, g_value in guess_dict.items():
            if a_key == g_key:
                if a_value == g_value:
                    right_answer += 1
    return right_answer


def first_guess(boys,girls):
    '''
    Input: boys (list)
           girls (list)
    Output: matched_couples (dict)
    A funtion for making the first guess, which is a completely random guess'''
    return matched_couples(boys,girls)


def simulating_random_guesses():
    best_match = 0
    best_match_attempt = 0
    match_attempts = 0

    for num in range(1000):
        boys = generate_boy_list()
        girls = generate_girl_list()
        couples = matched_couples(boys,girls)

        first = first_guess(boys,girls)
        match_attempts += 1
        first_res = see_guessing_results(first,couples);
        print(first_res)

        if first_res > best_match:
            best_match = first_res
            best_match_attempt = match_attempts
    print(f"\n\n ____RESULTS_____\nBest Match: {best_match}\nIteration: {best_match_attempt}")


def generate_second_guess(previous_guesses,boys,girls):
    '''Input: previous_guesses (dict)
              boys (list)
              girls (list)

       Output:guess (dict)
    A function to generate a guess using keeping the first 5 the same
    but randomizing the last 5'''
    new_guesses = {}
    half = 5
    for key, value in previous_guesses.items():
        if half != 0:
            new_guesses[key] = value
            half -= 1
        else:
            break;
    new_boy = boys.copy()
    new_girl = girls.copy()
    for boy in new_guesses.keys():
        new_boy.remove(boy)
    for girl in new_guesses.values():
        new_girl.remove(girl)

    while half != 5:
        pair_boy = r.choice(new_boy)
        pair_girl = r.choice(new_girl)
        for key, value in previous_guesses.items():
            if pair_boy == key:
                if pair_girl == value:
                    pair_girl = r.choice(new_girl)
        new_guesses[pair_boy] = pair_girl
        new_girl.remove(pair_girl)
        new_boy.remove(pair_boy)
        half += 1
    return new_guesses


#simulating_random_guesses()
'''\/\/\/ TESTING BELOW \/\/\/'''

boys = generate_boy_list()
girls = generate_girl_list()
couples = matched_couples(boys,girls)
print("ANSWER: ",couples)
match_attempts = 0
first = first_guess(boys,girls)
match_attempts += 1
print("\nFirst Guess: ", first)
first_res = see_guessing_results(first,couples);
print("\nResult: ",first_res)
second_guess = generate_second_guess(first,boys,girls)
match_attempts += 1
print("\nSecond Guess: ", second_guess)
second_res = see_guessing_results(second_guess,couples)
print("\nSecond Results: ",second_res)
