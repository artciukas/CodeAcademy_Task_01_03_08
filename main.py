
"""
Ideti dar viena klase su praktika ir examinu
Moduliai(random skaciams) - Done
Loginimas i faila.
Venv ir Git
"""


import logging
import random_numbers_module

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Game:
    list_of_statistic = []
    def __init__(self, name) -> None:
        self.name = name

    def greeting(self):
        user_choice_practis_or_exam = input(f"Welcome {name} to practice multiplication tables,\nPlease choice practis(1) or exam(2):")
        while True:
            if user_choice_practis_or_exam == '1':
               
                logging.info(f'User {name} choice practis')
                Practis.practice(self)
                break
            elif user_choice_practis_or_exam == '2':
                logging.info(f'User {name} choice exam')
                Exam.exam(self)
                break
            else:
                user_choice_practis_or_exam = input("Please choice write practis(1) or exam(2):")
            
    
    def first_random_number(self):
        self.first_random_number_form_1_to_9 = random_numbers_module.first_random_number()
        return self.first_random_number_form_1_to_9
    
    def second_random_number(self):
        self.second_random_number_form_1_to_9 = random_numbers_module.second_random_number()
        return self.second_random_number_form_1_to_9
    
    def print_result(self):
        print(f"Correct answers is: {self.list_of_statistic.count(1)} of {len(self.list_of_statistic)}")



    
class Practis(Game):
    def practice(self):
        
        while True:
            try:  
                number_one = int(input(f'{name.upper()},TO PRACTIS:\nPlease enter number to practice the multiplication table: '))
                if number_one in range(1,9):
                    break
            except ValueError:
                print('Sorry, to enter need enter from 1 to 9')

        while True:
            try:
                time_of_practis = int(input(f"Ok, how many task'do you need? "))
                if int(time_of_practis) in range(1,30):
                    
                    break  
            except ValueError:
                print('Number not a string')

        i = 0  
        while i < time_of_practis:
            self.first_random_number()
            self.answer = number_one * self.first_random_number_form_1_to_9
                
            while True:    
                try:
                    self.user_answer = int(input(f"{number_one} * {self.first_random_number_form_1_to_9 } = "))
                    if self.user_answer != '':
                        break
                except ValueError:
                    print('You answer is empty,\nEnter answer')


            if self.user_answer == self.answer:
                self.list_of_statistic.append(1)
            else:
                self.list_of_statistic.append(0)
            i = i + 1
    

        self.print_result()
      
        
class Exam(Game):
    def exam(self):
        print(f'Welcome {name} to exam\nGOODLUCK!!!')
        i = 0  
        while i < 10:
            self.first_random_number()
            self.second_random_number()
            answer = self.first_random_number_form_1_to_9 * self.second_random_number_form_1_to_9

            while True:
                try:
                    user_answer = int(input(f'{self.first_random_number_form_1_to_9} * {self.second_random_number_form_1_to_9} = '))
                    if user_answer != '':
                        break
                except ValueError:
                    print('Please use only nubers to correct input data')
            if user_answer == answer:
                self.list_of_statistic.append(1)
            else:
                self.list_of_statistic.append(0)
            i = i + 1
        self.print_result()
        logging.info('Exam function is DONE!!!')
        

name = input("Enter Your Name:\n")
if name == '':
    name = 'user'
logging.info(f"{name} has logged in successfully !!")
start = Game(name)
tolog = start.greeting()


