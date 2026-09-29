#importing necessary libraries

import numpy as np 
import statistics 
from pathlib import Path

#dictionary of all existing bacterial id
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
    }     

#calculates the average amount of bacteria per strain in a subsample

def average_in_subsample(event_count, bacteria_count): 
    average={} #an empty dict to store results
    if event_count==0: #handles possible division by 0
            print("There are no events. Can't count the bacteria.")
            return
    for name in bacteria_count: #iterates over dict with total count of each bacteria strain to calculate the average
        average[name]=bacteria_count[name]/event_count 
    return average 

#a function to calculate if wild-type and mutant strains differ significantly, takes as arguments list of subsample averages and number of events

def find_symmetry(final_avg_lists, events): 
    diff={} #empty dict for differences
    unc={} #empty dict for uncertainties
    
    #iterates over list of bacterial IDs, skipping the mutants and saving the names of wild-type in two variables:
    #one for wt and one for mutant (with minus in front)
    
    for id in bacterial_id: 
        if id.startswith("-"):
            continue
        wt=bacterial_id[id]
        mt=bacterial_id["-" + id]

        
        diff_subsample=[]
        for w, m in zip(final_avg_lists[wt], final_avg_lists[mt]): #saves the subsample averages of wt and mutants into different variables
            diff_subsample.append(w-m) #calculates the difference and adds it to the list
        diff[id]=np.average(diff_subsample, weights=events) #finds the average over all subsamples
        unc[id]=statistics.stdev(diff_subsample) #finds the uncertainty
    return diff, unc #returns the results
        

def count_bacteria_in_subsample(bacterial_id, file_name): #counts bacteria in a subsample
        try: #accounts for error of wrong file name
            event_count=0 #initialises the event count
            event_has_bacteria=False #variable to track validity of an event
            bacteria_count={bacterial_id[name]:0 for name in bacterial_id} #creates a dictionary using dictionary comprehension (iterates over dict with bacterial names)
            #key is name of bacteria and the initial value is 0
            with open (file_name, "r") as file: #opens the file for reading
                print(f"Processing file: {file_name.name}!")
                for line in file: #iterates over each line
                    values=line.split() #splits the line into separate values 
                    
                    if len(values)==2: #if it is a header
                        if event_has_bacteria: #if previous event contains data 
                            event_count+=1 #increases event count
                            event_has_bacteria=False #resets the tracking variable
                    elif len(values)==4 and values[3] in bacterial_id: #if it is a data line and bacterium's ID is present in my list
                        bacteria_count[bacterial_id[values[3]]]+=1 #increases the number of this specific strain
                        event_has_bacteria=True #indicates that there is bacteria in this event
                if event_has_bacteria: #checks the last event
                    event_count+=1 #if there was bacteria in last event, counts the event
                return average_in_subsample(event_count, bacteria_count), event_count #returns a dict of averages per strain + event count
        except FileNotFoundError:
            print("This file doesn't exist!") #warns user
        except:
            print("Couldn't open the file!")

def get_files(): #a function to save files from user
    files_list=[]
    folder=Path(input("Enter the name of folder with your data files:\n").strip()) #asks user for a folder with files
    
    
    if not folder.is_dir(): #warns user if folder isn't found
        print("Folder not found!")
        return []
    
    print("Thank you, your input was received!\n")
    for f in folder.iterdir(): #iterates over files in folder
        if f.is_file() and f.name.startswith("output-Set") and f.name.endswith(".txt"): #checks if file complies with the requirements
            files_list.append(f) #adds file to list
    return files_list
    
def main():
    final_avg_list={} #creates an empty dictionary 
    files_list=get_files() #saves the files user provided in a list
    
    if len(files_list)<2: #checks if there are enough files to run the program
        print("Need at least 2 files!")
        return

    for bacteria in bacterial_id:
        final_avg_list[bacterial_id[bacteria]]=[] #adds to dict bacterial names as keys and an empty list as values


    try:
        events=[]
        for subsample in files_list: #iterates over all files
            results, event_count =count_bacteria_in_subsample(bacterial_id, subsample) #saves in a variable the dict of averages from subsamples
            events.append(event_count)

            for name, avg in results.items(): #iterates over received dict and saves keys and values to separate variables
                final_avg_list[name].append(avg) #saves the averages in a dictionary using bacteria's name as key and average as value
    except:
        print("Something went wrong with calculating averages!")
        return
    total_events=sum(events)
    final_averages={}

    print("Calculating the weighted average count per strain now...\n")
    for name, averages in final_avg_list.items(): #iterates over the list of subsample averages per bacterial strain
        weighted_avg=np.average(averages, weights=events) #calculates the weighted average using event count in subsample as weight
        std=statistics.stdev(averages) #calculates uncertainty as std of subsample averages
        final_averages[name]=weighted_avg, std #saves results in a dict using bacterial name as key

    print("All done!\n")
    print("==========================================")
    print("RESULTS")
    print("==========================================\n")

    print(f"Total events analysed: {total_events}\n")

    
    for name, value in final_averages.items():    
        print(name)
        total_count=round(value[0]*total_events)
        print(f"Total count: {total_count}")
        print(f"Weighted Average: {round(value[0],7)} ± {round(value[1],7)}\n")

    print("==========================================")
    print("SYMMETRY AND ASYMMETRY REPORT")
    print("==========================================\n")
    print("Here are the differences between wild type and mutant of each bacterial strain:")
    differences, uncertainties =find_symmetry(final_avg_list, events)
    for i in differences:
        print(f"{bacterial_id[i]} and {bacterial_id['-' + i]}: {round(differences[i], 7)} ± {round(uncertainties[i], 7)}")
        if abs(differences[i])>uncertainties[i]*3:
            print(f"{bacterial_id[i]} and {bacterial_id['-' + i]} counts differ significantly (more than 3 std)!\n")
        else:
            print(f"{bacterial_id[i]} and {bacterial_id['-' + i]} count difference is within 3 std. The strains don't differ significantly!\n")
    

main()
