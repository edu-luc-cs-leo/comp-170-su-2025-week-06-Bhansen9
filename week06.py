
def load_to_list(filepath: str)-> list[float]:
    #first step check if there is data inslide the file path
    temp_list = "The data soure is empty"
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
    else:
        print("The data source was empty")




"""Looking into the solutions and comparing my code I see a few differences. I think the most notable is the difference between
 the 1st answer of the intersection. I think I got the first part of if foo == bar then it means there is an intersection.  
 However I did not set up a way to scan the string 1 letter at a time to return a very accurate response. For the only alphabet
   problem I believe mine is correct it is similar to the solution however it has some switched around values in the boolean 
   side that still lead to a correct answer. For the letters only I think I got correct as it is almost the same as the solutions.
     The only difference in this being the null checker. Mine assumes that it is letter only, however if it does not it returns 
     as None. The palindrome maker is very promising. It works well however it uses a little bit different logic than the 
     solutions. This is because it starts at the string at the end position and creates a reversed version of the string 
     and adds it to the first string to create the palindrome. After going through testing I think my Palindrome checker 
     is correct and uses very similar logic to the solutions. A few differences to mine is that it returns it as false if 
     there are any other symbols or numbers. It also makes the string all lower case to avoid mixing up with letters. 
     It also has two checkers both start at different ends and move to the middle checking every character and reporting 
     back to make sure they are equal. I think I did very well this week of homework and truly believe I was correct with
       most of my answers. I think going forward I need to include more comments and that is something I tried to do well in
         week 6,"""

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(load_to_list("data/teperatures.txt"))
print(load_to_list(None))




temp_list = load_to_list("data/temperatures.txt")
descriptive_statistics(temp_list)
descriptive_statistics(None)



apply_markup("data/markup.txt")
apply_markup(None)


