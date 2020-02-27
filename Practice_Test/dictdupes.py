"""
Write a function duplicate_Values(aDictionary) that takes a dictionary of 20 values in the range 1- 99,
and determines whether there are any duplicate values in the dictionary.

The function duplicate_Values(aDictionary) returns 1 if there are duplicate values and 0 otherwise

"""

def duplicateValues(aDictionary):
   """
   There are many ways to determine if there are duplicate values.
   1- One can create an array of 100 bits (initialized to '0') and set the bit to '1' at the index of the number
      in the dictionary. If the bit at that index is already '1' that means we have duplicate values.

   2- Another simple way is to sort the values of the dictionary then look if there are duplicate values

   """
   for i in range(20):
      value = aDictionary[i]
      for j in range(i+1,20):
         if aDictionary[j] == value:
            return 1
   return 0

# # dictionary1 has duplicate values: 53 and 69
# dictionary1 = {0:53, 1:76, 2:16, 3:17, 4:43, 5:30, 6:38, 7:26, 8:4, 9:53, 10:69, 11:80, 12:71, 13:12, 14:69, 15:7, 16:82, 17:84, 18:87, 19:15}
# # dictionary2 has NO duplicate values
# dictionary2 = {0:93, 1:76, 2:16, 3:17, 4:43, 5:30, 6:38, 7:26, 8:4, 9:53, 10:69, 11:80, 12:71, 13:12, 14:77, 15:7, 16:82, 17:84, 18:87, 19:15}

# # dictionary3 has NO duplicate values
# dictionary3 = {0:33, 1:49, 2:88, 3:9, 4:14, 5:89, 6:59, 7:32, 8:34, 9:41, 10:38, 11:35, 12:42, 13:15, 14:50, 15:20, 16:66, 17:77, 18:8, 19:4}

# # dictionary4 has NO duplicate values: 59 and 20
# dictionary4 = {0:59, 1:49, 2:88, 3:9, 4:14, 5:89, 6:59, 7:32, 8:34, 9:20, 10:38, 11:35, 12:42, 13:15, 14:50, 15:20, 16:66, 17:77, 18:8, 19:4}
# print(duplicateValues(dictionary1))
# print(duplicateValues(dictionary2))
# print(duplicateValues(dictionary3))
# print(duplicateValues(dictionary4))
