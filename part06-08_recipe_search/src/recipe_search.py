# Write your solution here
def search_by_name(filename: str, word: str):
    recipes = []
    result = []
    with open(f"{filename}") as recipes_file:
        for line in recipes_file:
            line = line.replace("\n", "")
            for char in line:
                if char.isupper():
                    recipes.append(line)
                    break
    
    for dish in recipes:
        if word.lower() in dish.lower():
            result.append(dish)

    return result

def closest_value(input_list: list, input_value:int):
    newlist = []
    for i in input_list:
        newlist.append(int(i) - input_value)
    lstt = [abs(ele) for ele in newlist]

    return int(input_list[lstt.index(min(lstt))])

def search_by_time(filename: str, prep_time: int):
    recipes = {}
    result = []
    name = ''
    mins = []
    with open(f"{filename}") as recipes_file:
        for line in recipes_file:
            line = line.replace("\n", "")
            for char in line:
                if char.isupper():
                    recipes[line] = ''
                    name = line
                    break
            if line.isdigit():
                recipes[name] = int(line)
                mins.append(line)
    closerMin = []
    for i in mins:
        if int(i) <= prep_time:
            closerMin.append(int(i))
    for min in closerMin:
        for dish, time in recipes.items():
            if time <= min:
                result.append(f"{dish}, preparation time {time} min")
    return list(set(result)) 

def search_by_ingredient(filename: str, ingredient: str):
    recipes = {}
    result = []
    with open(f"{filename}") as recipes_file:
        name = ''
        for line in recipes_file:
            line = line.replace("\n", "")
            contains_uppercase = False

            for char in line:
                if char.isupper():
                    recipes[line] = []
                    name = line
                    contains_uppercase = True
                    break
            
            if line == '':
                continue
            elif contains_uppercase:
                continue
            else:
                recipes[name].append(line)
    for dish, ingredientList in recipes.items():
        if ingredient in ingredientList:
            result.append(f"{dish}, preparation time {ingredientList[0]} min")

    return result

if __name__ == "__main__":
    found_recipes = search_by_time("recipes2.txt", 10)
    for recipe in found_recipes:
        print(recipe)
