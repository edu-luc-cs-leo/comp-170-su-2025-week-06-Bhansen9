
def load_to_list(filepath: str)-> list[float]:
    temp_list = None
    if filepath is not None and len(filepath) > 0:
        with open("data/temperatures.txt", "r") as file:
            temp_list = [float(line.strip())for line in file]
    return temp_list
# print(load_to_list("data/temperatures.txt"))

def descriptive_statistics(source_data: list[float])-> None:
    if source_data is not None and len(source_data) > 0:

        print(f"There are {len(source_data)} values in the data source")
        print(f"The average is {round(sum(source_data)/len(source_data), 2)}")
        print(f"The highest value is {max(source_data)} and the smallest is {min(source_data)}")
    else:
        print("Data source set was Empty")

# temp_list = load_to_list("data/temperatures.txt")
# descriptive_statistics(temp_list)


















#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

