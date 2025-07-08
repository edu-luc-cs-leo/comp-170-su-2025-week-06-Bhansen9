
def load_to_list(filepath: str)-> list[float]:
    #first step check if there is data inslide the file path
    temp_list = None
    if filepath is not None and len(filepath) > 0:
        #next open the file using the open function and setting it to the reading mode
        with open("data/temperatures.txt", "r") as file:
            #take the data found in the file and turn it into floats going through every line and strip removes uneeded spaces
            temp_list = [float(line.strip())for line in file]
    # returns values weather it is empty or not
    return temp_list
# print(load_to_list("data/temperatures.txt"))

def descriptive_statistics(source_data: list[float])-> None:
    #checks if data is empty or not
    if source_data is not None and len(source_data) > 0:
#finds the amount of data collected
        print(f"There are {len(source_data)} values in the data source")
        #rounds the number with the round function as a float then takes the sum of all the tempertures divided by the amount of data collected and ,2 makes the round function round the final number by 2 decimal points
        print(f"The average is {round(sum(source_data)/len(source_data), 2)}")
        #finds the max from the data and the min from the data
        print(f"The highest value is {max(source_data)} and the smallest is {min(source_data)}")
    else:
        #prints that the data was empty if it was
        print("Data source set was Empty")

# temp_list = load_to_list("data/temperatures.txt")
# descriptive_statistics(temp_list)

def apply_markup(filepath:str)-> None:
    if filepath is not None and len(filepath) > 0:
        with open(filepath ,"r") as file:
            for line in file:
                appiled_outcome = []
                i = 0
                while i < len(line):
                    if line[i] == ".":
                        i += 1
                        if i < len(line):
                            appiled_outcome.append(line[i].upper())
                    elif line[i] == "_":
                        i += 1
                        if i < len(line):
                            appiled_outcome.append(' '.join(line[i]))
                    else:
                        appiled_outcome.append(line[i])
                    i += 1
                print(''.join(appiled_outcome),end = '')
apply_markup("data/markup.txt")

















#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

