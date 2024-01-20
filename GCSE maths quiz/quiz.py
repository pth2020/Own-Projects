from data import question_bank 
from data import answers
import re
import sys
print("GCSE maths quiz\n")
#Setions and topics available for GCSE maths quiz
#key = section and list of topics = values
section_topic = {
   'number':['percentages','fractions','decimals','standard_form','compound_interest'],
   'algebra':['simplify_expressions','substitution','solve_equations','expand_and_factorise','linear_sequences']
}

user_answers = [] #populated as user answers questions
section_chosen = ''
topic_chosen = ''

#functions to excecute menu_choices
def show_quiz_options():
    #user provided with a list of sections (number/algebra) and topics to select from to do the quiz
    print("\nSections and Topics to choose from...\n")
    for i in range(len(section_topic)):
        dict_list_keys = list(section_topic.keys()) #store keys of section_topic dict into a list
        dict_list_values = list(section_topic.values()) #store values of section_topic dict inot a list
        print("Section: ",dict_list_keys[i],f"({i+1})") #traverse through list to print keys
        print("Topics:")
        for j in range(len(dict_list_values[i])):
            print("\t\t ",dict_list_values[i][j],f"({j+1})") # prints out all topics under each section
    
    #user prompted to choose section topic and sub-topic
    try:
        sec_num = int(input("\nEnter section number: "))
        topic_num = int(input("Enter topic number: "))
        #if out of range number is entered for either or both section and/or topic, exception is raised
        if sec_num < 0 or sec_num > len(section_topic) or topic_num < 0 or topic_num > 5:
            raise Exception("Incorrect input")
    except ValueError:
       print("========================")
       print("Non numeric input found!")
       print("Enter numbers 1 - 4")
       print("========================")
    else:
        global section_chosen 
        section_chosen = dict_list_keys[sec_num-1]
        global topic_chosen 
        topic_chosen = dict_list_values[sec_num-1][topic_num-1]
        print("\n********************************************")
        print(f"QUIZ - [{section_chosen}] : [{topic_chosen}]")
        print("*********************************************")
        #call start_quiz() to begin quiz - pass user's selection (section & topic) as parameters
        start_quiz(dict_list_keys[sec_num-1],dict_list_values[sec_num-1][topic_num-1]) 
        
            
def start_quiz(sec,top):
    #multiple choices list
    choices = ['a)','b)','c)','d)']
    section = sec #passing user's selection for section
    topic = top #passing user's selection for topic
    #traverse through question bank (imported) as per user's section and topic choices
    for i in range(len(question_bank[section][topic])):
        dict = question_bank[section][topic][str(i+1)]
        dict_keys_list = list(dict.keys())
        dict_values_list = list(dict.values())
        print()
        print(f"Q{i+1}.",dict_keys_list[0])
        for j in range(len(dict_values_list[0])):
            print(choices[j],dict_values_list[0][j],end="  ") #to print multiple choices{ a), b), c) and d) } in one line
                        
        print("\n")
        ans = input("Your answer (a,b,c or d): ").lower()
        #restricting user to enter alphabets a - d, anything else system exits 
        if not re.match("^[a-d]",ans):
            print("Error! Only letters a - d allowed!")
            sys.exit()
        else:
            #storing user's answers in user_answer list
            user_answers.append(ans)
    
def show_result():
    user_correct_answers_counter = 0
    correct_answers = [] #populated with factual answers from imported dictionary, answers
    for i in range(5):    
        #importing correct answers from data.py and storing them in list 
        #example: answers[number_percentages_Q1] 
        correct_answers.append(answers[section_chosen+"_"+topic_chosen+"_"+"Q"+str(i+1)]) 
    
    for num in range(len(correct_answers)):    
        try:
            #comparing user's answers with correct answers to score user's performance            
            if correct_answers[num] == user_answers[num]:
                user_correct_answers_counter += 1
        except(IndexError):
            print("*******************")
            print("Attempt another quiz")
            print("********************\n")
            return # exits function

    #score (out of 5 and as percentage)
    print("\n***********************")       
    print(f"Result: {user_correct_answers_counter} out of 5")
    print(f"{user_correct_answers_counter/5*100}%")

    if user_correct_answers_counter == 5:
        print("You have smashed it!")
    elif user_correct_answers_counter == 4:
        print("Well done!")
    elif user_correct_answers_counter == 3:
        print("Good result")
    elif user_correct_answers_counter == 2 or user_correct_answers_counter == 1:
        print(f"Work on areas of difficulty in {topic_chosen}")
    else:
        print(f"You need to revise {topic_chosen} entirely.")
   
    print("\n***********************")    

    #reset correct_answer[] and user_answers[]
    correct_answers.clear()
    user_answers.clear()

        
#provide user with a list of options
menu_choice = 0
while menu_choice != 3:
   print()
   print("1. Start quiz")
   print("2. Show result")
   print("3. Exit")

   try:
       menu_choice = int(input("Menu Choice (1-3): "))
   except:
       print("========================")
       print("Non numeric input found!")
       print("Enter numbers 1 - 3")
       print("========================")
       continue   
   
   #Excecute user's choice
   if menu_choice == 1:
       show_quiz_options()
   elif menu_choice == 2:
      show_result()
   elif menu_choice == 3:
       print("Exiting quiz")
   else:
       print("\nInvalid input, please enter an integer between 1 and 3")
       
print("\n")
