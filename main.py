
"""

"""


import logging
import random_numbers_module

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Game:
    answer: int
    first_random_number: int
    second_random_number: int
    number_one: int
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.list_of_statistic: list = []
        
        

    def greeting(self)-> None:
        user_choice_practis_or_exam = input(f"Welcome {name.capitalize()} to practice multiplication tables,\nPlease enter 1 to practice or 2 to exam:")
        while True:
            if user_choice_practis_or_exam == '1':
                logging.info(f'User {name} choice practis')
                Practice(self.name).practice()
                break
            elif user_choice_practis_or_exam == '2':
                logging.info(f'User {name} choice exam')
                Exam(self.name).exam()
                break
            else:
                user_choice_practis_or_exam = input("Enter 1 to practice or 2 to exam:")
            
    
    def random_number(self)-> int:
        self.random_number_form_1_to_9 = random_numbers_module.random_number()
        return self.random_number_form_1_to_9
    
    
    def print_result(self)-> None:
        print(f"Correct answers is: {self.list_of_statistic.count(1)} of {len(self.list_of_statistic)}")

    def add_statistic_to_list(self)-> None:
        if self.user_answer == self.answer:
            self.list_of_statistic.append(1)
        else:
            self.list_of_statistic.append(0)
    
    def pass_or_fail(self)-> None:
        if self.list_of_statistic.count(1) >= 7:
            print(f'Congratulation {name},\nexam is: PASSED')
        else:
            print(f'Sorry {name}, keep practice.\nExam is: FAIL')
    

    def user_input_error_handling_exam(self)-> None:
        while True:
                try:
                    self.user_answer = int(input(f'{self.first_random_number} * {self.second_random_number} = '))
                    if self.user_answer != '':
                        break
                except ValueError:
                    print('You answer is empty or not a number')
    
    def user_input_error_handling_practis(self)-> None:
        while True:    
                try:
                    self.user_answer = int(input(f"{self.number_one} * {self.random_number_form_1_to_9 } = "))
                    if self.user_answer != '':
                        break
                except ValueError:
                    print('You answer is empty or not a number')
    
    def user_continue_or_exit(self)-> None:
        while True:    
            self.continue_or_exit = input('If you want to continue pactice, enter 1\nIf you are ready for the exam, enter 2\nTo exit press any button...')
            if self.continue_or_exit == "1":
                Practice(self.name).practice()
                break
            elif self.continue_or_exit == "2":
                Exam(self.name).exam()
                break
            else:
                break

    def input_number_multiplication_choice_practice(self)-> None:
        while True:
            try:  
                self.number_one = int(input(f'WELCOME {name.upper()} TO PRACTIS:\nPlease enter number(1 - 9) to practice the multiplication table: '))
                if self.number_one in range(1,9):
                    break
            except ValueError:
                print('Enter correct nuber from 1 to 9 to practice the multiplication table!!!')
    
    def input_tasks_nuber_practis(self)-> None:
        while True:
            try:
                self.time_of_practis = int(input(f"Ok, how many task's do you need to practis multiplication table from {self.number_one}? "))
                if int(self.time_of_practis) in range(1,30):
                    break
                else:
                    print("Choice is not correct, maximum tasks are 30")  
            except ValueError:
                print('Please enter task number from 1 to 30')
                



class Practice(Game):
        
    def practice(self)-> None:
        self.input_number_multiplication_choice_practice()
        self.input_tasks_nuber_practis()

        i = 0  
        while i < self.time_of_practis:
            self.random_number()
            self.answer = self.number_one * self.random_number_form_1_to_9    
            self.user_input_error_handling_practis()
            self.add_statistic_to_list()
            i = i + 1
    
        self.print_result()
        self.user_continue_or_exit()
      
        
class Exam(Game):
    def exam(self)-> None:
        print(f'Welcome {name} to exam,\nGOODLUCK!!!')
        i = 0  
        while i < 10:
            self.random_number()
            self.first_random_number = self.random_number_form_1_to_9
            self.random_number()
            self.second_random_number = self.random_number_form_1_to_9
            self.answer = self.first_random_number * self.second_random_number
            self.user_input_error_handling_exam()
            self.add_statistic_to_list()
            i = i + 1
        self.print_result()
        self.pass_or_fail()
        logging.info('Exam function is DONE!!!')



def user_name_input()-> str:
    name = input("Welcome to multiplication table trainer\nPlease enter your name:\n")
    if name == '':
        name = 'user'
    return name

name = user_name_input()
logging.info(f"{name} has logged in successfully !!")
start = Game(name)
start.greeting()


