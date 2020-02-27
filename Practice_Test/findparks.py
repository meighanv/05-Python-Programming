'''
Write a function find_parks that takes a list of dictionaries and a string that represents 
a state name. The state name may or may not be capitalized but should match regardless.

The list contains a collection of dictionaries that represent state parks. The dictionaries each
contain a state name, park name, and cost of camping at the park. The dictionary's keys are
"state", "park", and "cost". 

Example:  [{"state":"Texas","park":"Guadalupe","cost": 12.50},
            {"state":"Michigan","park":"Sterling","cost": 8.50},
            {"state":"Texas","park":"Pedernales","cost": 13.50}]

The state name may or may not be capitalized but should match 
regardless when compared to the state name being searched.
The function should iterate through the list of dictionaries and find all parks that reside
in the state name passed to the function and has a cost of less than 15 dollars. 
If a match is found, store the park name as a string in a python set. 

if the list or state name passed to the function is empty or None, return "INVALID_DATA"

The minimum cost for a state park is $8. Any park listed with cost lower than 8, the function should
return "INVALID_DATA"

if any key errors are encountered with the dictionary, the function should return the string "KEY_ERROR"

The function will return the set when the list is successfully iterated. Return an empty set 
if no parks are found.
'''


def find_parks(parkList, state):
    output = []
    if state=="" or state == None or parkList == []:
        return "INVALID_DATA"
    else:
        state = state.lower()
    try:
        for park in parkList:
            try:
                if park["cost"] < 8:
                    return "INVALID_DATA"
                elif park["state"].lower() == state:
                    if park["cost"] < 15:
                        output.append(park["park"])
                else:
                    pass
            except KeyError:
                return "KEY_ERROR"
    except TypeError:
        return "INVALID_DATA"

 
        

    return set(output)

# stateParks = []
# print(find_parks(None, "texas"))
