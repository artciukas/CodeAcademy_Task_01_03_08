import random


def random_number():
    random_number_form_1_to_9 = random.randint(1,9)
    return random_number_form_1_to_9




if __name__ == "__main__":
    print('Test')
    print(f'Testing code: {random_number()}')

