# ----------------------------------------------------------------------------------- #
# Title: Module 07 Files and Exceptions
# Description: Demo for Error Handling
#              Example of how to handle FileNotFoundError error
#              Example of how the Catch-All Exception handler gives useful information
# ChangeLog: (Who, When, What)
# Dev: GGornalusse,11.30.2021,Created  Script
# ----------------------------------------------------------------------------------- #

try:
    with open("German's file.txt") as gg:
        file_data = gg.read()
    print(file_data)
except FileNotFoundError:
    print("The data file you are trying to read is missing.")
except Exception as err:
    print('Some other error occurred.', str(err))
finally:
    print("Hope you learned error handling!")
