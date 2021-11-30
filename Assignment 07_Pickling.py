# --------------------------------------------------------------------------------------- #
# Title: Module 07 Files and Exceptions
# Description: Demo for Pickling
#              Write a binary data file from a dictionary
#              Read a binary data file into a new dictionary
#              Confirm that the new file is a dictionary type
# ChangeLog: (Who, When, What)
# Dev: GGornalusse,11.28.2021,Created Demo for Pickling
# --------------------------------------------------------------------------------------- #

import pickle   # To use pickle, first you import the pickle package into Python

# -- Data -- #
telephone_dic = {"German": "206-326-9111", "Mike": "345-222-3333", "Mary": "999-2222", "Peter": "210-111-1111", "Osito":"222-222-2222"}
file_name = "TelephoneBook.dat"

# -- Processing -- #
def write_data_to_file(file_name, dic_of_data):
    outputfile = open(file_name, "wb")
    pickle.dump(dic_of_data, outputfile)
    outputfile.close()

def read_data_from_file(file_name):
    readfile = open(file_name, "rb")
    new_telephone_dic = pickle.load(readfile)
    readfile.close()
    return new_telephone_dic

# -- Presentation (I/O) -- #

# Store the dictionary object into a binary file
write_data_to_file(file_name= "TelephoneBook.data", dic_of_data=telephone_dic)

# Read the data from the file into a new dictionary object, display the contents and confirm it's a dictionary
print(read_data_from_file(file_name="TelephoneBook.data"))
print(type(read_data_from_file(file_name="TelephoneBook.data")))

