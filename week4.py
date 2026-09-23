'''
1. deliverable: 10 averages for each ID
2. 1 final average (weighted or normal) of each bacterial strain per event
3. uncertianty - std of point 1 

1 file - 1 sub sample
'''

import os #library to create files etc.
import math #library for math expressions

bacterial_id={
    "211":"E. coli WT", 
    "-211":"E. coli mutant", 
    "321":"Bacillus subtilis WT", 
    "-321":"Bacillus subtilis mutant", 
    "2212":"Pseudomonas aeruginosa WT", 
    "-2212":"Pseudomonas aeruginosa antibiotic-resistant", 
    "3122":"Streptococcus pneumoniae", 
    "-3122":"Capsule-deficient streptococcus pneumoniae", 
    "3312":"Mycobacterium tuberculosis", 
    "-3312":"Drug-resistant mycobacterium tuberculosis", 
    "3334":"Salmonella enterica", 
    "-3334":"Salmonella mutant"
}     #dictionary of all existing bacterial id


def count_bacteria(bacterial_id): #main function
    try:

        file_exists=False #variable to check of user's file exist
        while file_exists==False: #loop is running if user enters incorrect file name
            try: #accounts for error of wrong file name
                file_name=input("Enter the pathway to the file you want to work with:\n") #asks user for a pathway to open the file
                event_count=0 #initates the event count
                event_has_bacteria=False #variable to track validity of an event
                count={bacterial_id[name]:0 for name in bacterial_id} #creates a dictionary using dictionary comprehension (iterates over dict with bacterial names)
                #key is name of bacteria and the initial value is 0
                with open (file_name, "r") as file: #opens the file for reading
                    for line in file: #iterates over each line
                        values=line.split() #splits the line in to separate values 
                    
                        if len(values)==2: #if it is a header
                            if event_has_bacteria: #ifprevious event contains data 
                                event_count+=1 #increases event count
                                event_has_bacteria=False #resets the tracking variable
                        elif len(values)==4 and values[3] in bacterial_id: #if it is a data line and bacterias id is present in my list
                            count[bacterial_id[values[3]]]+=1 #increases the number of this specific strain
                            event_has_bacteria=True #indicates that there is bacteria in this event
                    if event_has_bacteria: #checks the last event
                        event_count+=1 #if there was bacteria in last event, counts the event
                    file_exists=True #allows to exit the loop
            except FileNotFoundError:
                print("This file doesn't exist!") #warns user
                file_exists=False #continues the loop
            except:
                print("Couldn't open the file!")


        print(f"Event count: {event_count}") #prints the event count
        if event_count==0: #handles possible divisom by 0
            print("There are no events. Can't count the bacteria.")
            for i in count: #iterates over dict with numbers of bacteria
                average = count[i]/event_count #calculates average and uncertainty for each specie
                print(f"Bacteria: {i} Average per event: {average} ± {uncertainty}") #prints the result for user
    except:
        print("Something went wrong :(")

count_bacteria(bacterial_id) #runs the function