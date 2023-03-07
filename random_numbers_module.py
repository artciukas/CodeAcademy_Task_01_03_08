import random




def first_random_number():
    first_random_number_form_1_to_9 = random.randint(1,9)
    return first_random_number_form_1_to_9
    
def second_random_number():
    second_random_number_form_1_to_9 = random.randint(1,9)
    return second_random_number_form_1_to_9


if __name__ == "__main__":
    print('Test')
    print(f'Testing code: {first_random_number()}')

