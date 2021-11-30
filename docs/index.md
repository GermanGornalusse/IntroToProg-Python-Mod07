# Assignment Module 07: Files and Exceptions
## How to Do Pickling and Exception Handling in Python
#### IT FDN 110 A Au21: Foundations of Programming: Python

##### Germán Gornalusse
##### Sunday November 28, 2021


[GitHubURL] (https://github.com/GermanGornalusse/IntroToProg-Python-Mod07)  
[GitHub Web] (https://germangornalusse.github.io/IntroToProg-Python-Mod07/)



## Introduction
In this paper, I will show you two useful concepts in Python programming language. In the first one, I will show you how to write and read files in binary format, a concept called “pickling”. In the second concept, I will demonstrate with an example how to do structured error handling; you will be using try-except block of code. For each section, I included useful websites and appropriate demos. Finally, you will upload both files (PDF, Word and Python scripts) into a GitHub repository and post a GitHub Web page.
For simplicity, I will assume you will be using Windows operating system.

## Step 1.  Create a subfolder in your C: Drive\_PythonClass
The following instructions will allow you to create this subfolder in your hard drive:  
**C:/_PythonClass/Assignment07**  

a) Left double click on “_PythonClass” folder (to open it)   
b) Right click> New > Folder  
c) Name the folder as Assignment 07_Yourlastname  
I am showing you how the final path to this folder will look like (**Figure 1**):  


![Figure 1](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Pathway%20to%20folder%20Assignment%2007.png)   
####  Figure 1. Path to the folder where you will save your Assignment 07. I used my first and last name (“German Gornalusse”) as an example to personalize my subfolder.



## Step 2. Create a new Project in PyCharm
You will create a new project in PyCharm that uses the _PythonClass\Assignment07_last name folder as its location. I assume you will have installed PyCharm on your C:\ drive or on your desktop.   
a) Double click the icon “PyCharm Community Edition 2021.2.3”. Mine shows up on my desktop.   
b) Select: File> New Project   
c) In location type C:\_PythonClass\Assignment07 to select the file subfolder wherein you will save your project. Alternatively, you can browse the destination folder by selecting the “open folder” symbol at the end of “Location” and manually by browsing and selecting the final folder. [See yellow arrow, on Figure 2]   
d) Select “New environment using Virtualenv” option. And “Create a main.py” welcome script option. [See orange arrow, Figure 2]. Make sure the Base interpreter is set “Python 3.10” (or the latest version you installed in your computer).   
e) Select “Create” (lower right corner of your screen). [Figure 2]   


![Figure 2](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/672c6850a2248f7c9f547b965f53d968b4093b20/docs/How%20to%20Create%20a%20New%20Project%20in%20PyCharm.png)  
Figure 2 How to create a new project in C:\_PythonClass\Assignment 07 subfolder using the IDE PyCharm 


To do that:   
a) File> Open   
b) Select Assignment 07 subfolder   
c) Select either “This window” or “New Window”.  Notice how, on the left-hand side, the “Assignment 07” subfolder shows up. In Figure 3 I am illustrating this example.    

![Figure 3](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Picture3.png)   
Figure 3. PyCharm window showing current folder where your Python scripts for the Assignment07 will be saved

## Step 3. Create two Python Scripts  in the Project Folder: “Assignment07”: Assignment 07_Pickling and Assignment 07_Error_Handling.

a) Right click (Context menu) Assignment 07 folder   
b) File> New> Python File > Assignment 07_Pickling   
c) File> New> Python File > Assignment 07_Error_Handling   
You will start writing the header and comments, as indicated in the Figure 3 above. And then, you add the code shown in the demos below.   

## Step 4. How to do Pickling in Python
I included a list of websites and videos that I think they are useful so you can learn how to do pickling in Python:   
•	https://www.datacamp.com/community/tutorials/pickle-python-tutorial (external website)   
I included this website because I have used Datacamp in the past to learn R programming and I really like how the instructions are stated.

•	https://www.youtube.com/watch?v=D2e3_mPhQw0.  I chose this website because I only wanted to focus on dictionaries and not in other objects.   
•	https://www.youtube.com/watch?v=Xc8Ss9JG2Pw I liked that this video incorporates the pickling multiple objects and handling error (try/except module), which we will cover in the next section.   
```
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
```   

The steps that are described in the script explain how to pickle a dictionary file.   

1)  Start importing pickle package in Python   
2)  In this simple script, you will be pickling a simple dictionary that contains names and telephone numbers. You start declaring the dictionary in the Data section of the script.   
3)  Also, in the Data section, you also declare the name of the file you will be writing data to. I added the “dat” extension but you could have not added any extension.   
4)  In the Processing section, we define a function “write_data_to_file”, which takes as parameters the file_name (new “pickled”, binary file) and dic_of_data (file to be picked, in this case a dictionary).   
5) To open the file for writing, simply use the open() function. The first argument should be the name of your file you will be writing to (new “pickled” file). The second argument is “wb”. The w means that you will  be writing to the file, and b refers to binary mode. This means that the data will be written in the form of byte objects.
6) Once the file is opened for writing, you can use pickle.dump(), which takes two arguments: the object you want to pickle (dic_of_data) and the file to which the object has to be saved (outputfile).    
7)  In the Presentation (Input/Output) section, you will call the write_data_to_file function and define the arguments file_name (new pickled file) and dic_of_data (original dictionary that will be pickled).    
8) You will verify that a a new file named Telephonebook.data  should have appeared in the same directory as your Python script. The file should be in the same folder as your script when you used the correct, relative file path. (Figure 4).   

![Figure 4a](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/BinaryFile%20Assignment%2007.PNG)
![Figure 4b](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Capture%20of%20binary%20file%20read%20with%20Notepad.PNG)
 Figure 4. Top panel: PyCharm window showing the binary file “TelephoneBook.data”. Notice the special characters showing how the code got “obscured”, but not totally encrypted. Also, notice that the location of this file. Bottom panel: binary file when opened with text editor Notepad.   
Below, I describe the  steps to how to unpickle a binary file into a new dictionary file.   

1) In the processing section, you will create the function “read_data_from_file” to unpickle the binary file. The function takes as parameter the “pickled” binary file we created in the previous step.
2) We use the open() function again, but now with 'rb' as second argument. The r stands for read mode and the b stands for binary mode, since  you'll be reading a binary file. Assign this to a new object “readfile”.
3) Next, use pickle.load(), with readfile as argument, and assign it to a new dictionary “ new_telephone_dic”. Again, you'll need to close the file at the end.
4) In the Presentation (I/O) section, you will read the data from the file into a new dictionary object.
To do that, simply call the function “read_data_from_file” and use as argument the binary file TelephoneBook.data you created in the previous section. Print this statement. 
5) Confirm that the new object is a dictionary using the command type().
Figure 5, below, verifies that this IO worked successfully.

 
![Figure 5](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Verification%20in%20PyCharm%20on%20Pickling.PNG)
Figure 5. PyCharm console window verifies that the “unpickling” of the binary file into a new dictionary file occurred successfully. Please notice the new dictionary elements and how type() statement confirm that it is a dictionary object: <class ‘dic’>   
In the following Figure 6 below, I illustrate how the assignment 07 worked properly once it is ran on OS command shell:
 
![Figure 6](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Capture%20CMD%20command%20to%20verify%20pickling%20works.PNG)
Figure 6. Assignment 07_Pickling ran on OS command shell

## Step 5. Structure Error Handling in Python
Before trying out the demo, please visit these websites:   
•	https://www.geeksforgeeks.org/python-exception-handling/    This website is a hub that contains many useful links in the bottom, wherein they explained separate exceptions like EOFError. The explanations are super clear.   
•	https://www.techbeamers.com/use-try-except-python/ Ideal for beginners.    
•	https://www.programiz.com/python-programming/exception-handling  I liked how the flow of error handling is explained in this website (what comes first, what is skipped, etc.)   
•	https://www.w3schools.com/python/python_try_except.asp I liked the simplicity of the explanations of the W3chools and the fact that you can try it out in any computer (even if you don’t have Python actually installed).    
```
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
```
When there are mistakes in your code, Python raises a runtime exception.  In this demo “Assignment 07_Error_Handling”, we will practice.    
First, you will learn what happens when your file is absent so Python cannot access it.   
a)  Write a try: statement. You will try to read the file “German’s file.text”, assign it to the object file_data and print it out. Because this file is missing, Python will internally raise an error of the type: FileNotFound.   
b) Because this exception occurs, the code in the try’s suite terminates and then the code in the try’s except suite runs. The code is indented under the “except” clause and only executes if the “FileNotFoundError” exception is raised. The Figure 7 below shows what happens when you run this code in Pycharm.   
 
![Figure 7](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Capture%20Except%20FileNotFoundError.PNG)
Figure 7. The new version of the code produces a much friendlier message thanks to the “try” and “except” block that triggers the FileNotFound built-in class.   
Now, you will create a folder in Assignment 07 with this name: “German’s file.txt” and you will run the code again.      
In this case, the line #16 of your code “except Exception as err” will be triggered.  Unlike the “non-specific” catch-all statement “except:”, this one arranges for the exception object to be assigned to the “err” variable and prints it out (line #17), as shown in Figure 8 below:      

![Figure 8](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Capture%20Except%20as%20object.PNG)
Figure 8. The catch-all exception handler can assign the error to a variable that can be printed out   
The last statement finally executes the command no matter how error handling happened in the try:except block of code.   
In the following Figure 9 below, I illustrate how the assignment 07_Error Handling worked properly once it is ran on OS command shell:   

![Figure 9](https://github.com/GermanGornalusse/IntroToProg-Python-Mod07/blob/main/docs/Capture%20of%20CMD%20while%20running%20Error%20Handling.PNG)   
Figure 9. Assigment_07 Error Handling ran under the command line OS shell

## Summary
In this paper, you were introduced to two useful Python features: pickling and error handling using try:except blocks. Pickling” is the process whereby a Python object (list, dic, etc.) is converted into a byte stream (0s and 1s), and “unpickling” is the inverse operation. The idea is that this binary-coded character stream  contains all the information necessary to reconstruct the object in another python script. The main advantage of pickling/unpickling is it allows to transfer files of reduced size from a server to another. In the second part of this paper, I illustrated how the try:except block can be used to spot errors in the script. You will also learn how to assign a non-specific exception as an error and how to use it.

