import random
import time


def display_title():
    '''
        Displays game title to user. 

        Parameters: None
        Return Value: None
    '''
    pass


def display_menu():
    '''
        Displays numbered options so that the user knows what types of questions are available.
        Options should include: Addition, Subtraction, Multiplication, Integer Division, Exponents, and Modulo. 

        YOU SHOULD NOT BE TAKING INPUT FROM THE USER IN THIS FUNCTION

        Parameters: None
        Return Value: None    
    '''
    pass


def display_seperator():
    '''
        Displays a line of symbols to seperate menu from input section.
        Example: --------------------------
        Hint: try multiplying a string by an integer... ('x' * 5)

        Parameters: None
        Return Value: None    
    '''
    pass


def menu_select():
    '''
        Allows the user to select one of the options from the menu by entering the corresponding number.
        Should also make the user re-select if their number is not one of the menu options.
        Note: For simplicity we can assume the user will not input a non-integer value. 

        Parameters: None
        Return Value: The user's selected option as an integer value.
    '''
    return

def generate_question(type):
    '''
        Generates 2 random numbers then based on the type of question,
        generates question using those numbers as a string and the answer as an integer.
        (You may want a 3rd random number with a smaller range (i.e. 1-10) that can be used for some of the harder question types)

        Hint: multiple values/variables can be returned from one function using a single return statement and seperating values with commas
            Ex: return x,y
        
        THIS FUNCTION SHOULD JUST RETURN THE QUESTION, NOT PRINT IT

        Parameters: type - the type of question to be generated (addition, multiplication...) as an integer value.
        Return Values:
                        - A randomly generated math question as a string (using the correct operator).
                        - The answer to the above math question as an integer.
    '''
    return

def answer_select(question, answer):
    '''
        Displays the given math question and allows the user to input an answer.
        Checks if the answer is correct and lets the user know, if wrong also display the correct answer.

        Parameters: 
                        question - A math question as a string.
                        answer   - The answer to the provided math question as an integer. 
        Return Value: A boolean value representing if the user got the question correct (True for correct, False for wrong). 
    '''
    
def main():
    display_title()
    display_menu()
    display_seperator()
    question_type = menu_select()
    question,answer = generate_question(question_type)
    correct = answer_select(question,answer)

    # BONUS: Have the program ask if the user wants another question, then do so if requested.
    # BONUS-BONUS: Implement a scoring system so the user gains/loses points for correct/incorrect questions.
    # BONUS THE THIRD: Implement a timing system so that for correct answers, the user gets more points the faster they answer.
    
    '''
    # Example usage of time library:
    # Calculates the time taken to provide input by taking the difference between the current time before and after the input function was run. 
    import time

    start = time.time()
    input("input something: ")
    end = time.time()
    print(f"Time elapsed: {end-start}")
    '''

# You may want to disable the main call to run each function individually for testing.
main()