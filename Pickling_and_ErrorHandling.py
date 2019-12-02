# ------------------------------------------------- #
# Title:
# Description:
# ChangeLog: (Who, When, What)
# BLee,12.1.2019,Created Script
# ------------------------------------------------- #

# Data --------------------------------------------- #
import pickle

strData = 'Employee ID,Name,Salary\n1,Russell Wilson,50000\n2,Pete Carroll,60000\n3,Chris Carson,40000'
strFileName = 'SeahawksSalary.txt'
strFileNamePickled = 'SeahawksSalaryPickled.txt'

# Processing --------------------------------------- #
# 1 Save data
def save_data(file_name, data):
    openfile = open(file_name, 'w')
    openfile.write(data + '\n')
    openfile.close()

# 2 Read data
def read_data(file_name):
    try:
        openfile = open(file_name, 'r')
        data = openfile.read()
        openfile.close()
        return data
    except Exception as e:
        print("There was a non-specific error!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')

# 3 Add more data
def add_more_data(file_name, data):
    openfile = open(file_name, 'a')
    openfile.write(data + '\n')
    openfile.close()

# 4 Pickle Store
def pickle_store(file_name, data):
    openfile = open(file_name, 'wb')  # Append and set to byte
    pickle.dump(data, openfile)
    openfile.close()

# 5 Pickle Read
def pickle_read(file_name):
     try:
        openfile = open(file_name, 'rb')
        openfiledata = pickle.load(openfile)  # Read and set to byte
        openfile.close()
        return openfiledata
     except FileNotFoundError as e:
         print("Text file must exist before running this script!")
         print("Built-In Python error info: ")
         print(e, e.__doc__, type(e), sep='\n')
     except Exception as e:
         print("There was a non-specific error!")
         print("Built-In Python error info: ")
         print(e, e.__doc__, type(e), sep='\n')

# Presentation ------------------------------------- #

# save_data(strFileName, strData)
# print(read_data(strFileName))

pickle_store(strFileNamePickled, strData)
print(pickle_read(strFileNamePickled))