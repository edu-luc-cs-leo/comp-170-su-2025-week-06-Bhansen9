
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


def apply_markup(filepath:str)-> None:
    # first step make sure the data is not empty
    if filepath is not None and len(filepath) > 0:
        # next open the filepath and access it through the read mode
        with open(filepath ,"r") as file:
            # declair the function to go through each line of the file
            for line in file:
                # for lines in the file remove uneeded spaces around the words and space the words so they can be acccesed in a list
                words = line.strip().split()
                # create a holding list for the applied words to be stored in
                applied_outcome = []
                # go into detail of the words in the file
                for word in words:
                    # uses the startswith function to determine which words should be tapered with
                    if word.startswith('.'):
                        # anylises the word by going to the 1st value in the string to skip the 0 value which would be either '.' or '_' then uppercases the remaining values in the string using the upper() funciton then adds them to the next applied_outcome list with the append function
                        applied_outcome.append(word[1:].upper())
                        # uses startswith to determine which strings in the words list has '_' first
                    elif word.startswith('_'):
                        # uses the join funtion to make a 'space' for every char in the string and starts at position 1 to skip the 0 position which would be '_' then appends them to the applied_outcome list uses the .join to make the outcome a single string
                        applied_outcome.append(' '.join(word[1:]))
                        # everything else that does not start with the special cases
                    else:
                        # addeds to the applied_outcome with the append function
                        applied_outcome.append(word)
                        # prints out the list but uses the need 'space' for each word that the strip() funciton did in the begining and uses .join to make the whole thing a single string
                print(' '.join(applied_outcome))


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

print(load_to_list("data/temperatures.txt"))
# list must be loaded into a list for the temps to be used as floats because if not the funciton will not be able to do caculations as it being a string
temp_list = load_to_list("data/temperatures.txt")
descriptive_statistics(temp_list)
apply_markup("data/markup.txt")