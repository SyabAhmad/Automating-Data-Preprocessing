# automating Data preprocessing with python
import pandas as pd
from sklearn.preprocessing import normalize
numericColumns = []
stringColumns = []
namesOfColumnsWantsToConvert = []
noString = False

def line():
    print("*========*========*========*========*")

try:
    data = pd.read_csv("dataSet/dataset.csv", delimiter=",")
    print("Task 01# Data read: Successfull")
    line()
except FileNotFoundError:
    print("File Not FOund Error")
    print("Task 01# Data read: Un-Successfull")
    line()
except pd.errors.EmptyDataError:
    print("There is no data in the dataset")
    print("Task 01# Data read: Un-Successfull")
    line()
except pd.errors.ParserError:
    print("Error while parsing the file")
    print("Task 01# Data read: Un-Successfull")
    line()


def checkingForNumericalValue():
    print("Checking the values")
    try:
        numericColumns.clear()
        stringColumns.clear()
        for col in data.columns:
            if pd.api.types.is_numeric_dtype(data[col]):
                return numericColumns.append(col)
            else:
                return stringColumns.append(col)

    except pd.errors:
        print("Error Occured: ", pd.errors)

    return data

# displaying both the vlues (String, and Numeric)
def displayingColumns(stringColumns, numericColumns):
    print("Numeric Columns: ", numericColumns)
    print("String Columns: ", stringColumns)
    print("Task 02#: Successfull")
    line()
    return data


# checking for cetagorical values
def checkForCetagoricalValues():
    cols = data.select_dtypes(include=object)
    for col in cols:
        if cols[col].unique() < 5:
            print("Task 03#: Checking for categorical values : Successfull")
            line()
            return True
        else:
            print("Task 03#: Checking for categorical values : Successfull")
            line()
            return False
    return data


# Checking for string values
def checkForStringValues():
    if stringColumns.count(0):
        print("No more String Values")
    else:
        print("Still have String values")
        noString = True
    return data



def doingOneHotEncoding(data):
    forEncoding = []
    print("Type names of the columns exact Spelling:")
    print("Data Columns are: ", data.columns)

    value2 = input("Should be comma separeted: ")
    forEncoding.extend(value2.strip().split(","))
    if value2!="":
        # one hot encoding process goes here
        for col in forEncoding:
            try:
                # data = pd.get_dummies(data, columns=[col], inplace=True)
                dummies = pd.get_dummies(data[col], prefix=col)
                print("Dummies Columns: ", dummies)
                data = pd.concat([data, dummies], axis=1)
                data.drop(col, axis=1, inplace=True)
                print("Converted successfully: ", data.head(5))
                print("Converted successfully")
                print("Now converting to numerical from booleans")
                try:
                    for dum in dummies.columns:
                        data[dum] = data[dum].astype(int)
                    # data["gender_female"] = data["gender_female"].astype(int)
                except pd.errors:
                    print(pd.errors)
                print("Conversion Done")
                print("Converted successfully: ", data.head(5))
                checkingForNumericalValue()
            except pd.errors:
                print("Error occrd: ", pd.errors)
    else:
        line()
        print("No Columns selected")
        mainMethod()
        line()

    return data


def removalOfColumn(namesOfColumnsWantsToConvert):
    line()
    print("to remove some columns ('columns Name') (multiple names would be comma separated)")
    value1 = input("Answer here: ")
    if value1!="":
        namesOfColumnsWantsToConvert.extend(value1.strip().split(","))
        columns_to_remove = namesOfColumnsWantsToConvert
        data.drop(columns=columns_to_remove, inplace=True)
        print("Column Removed Sucessfully")
    else:
        print("No Column Selected")
    line()
    return data



def checkForNullValues():
    print("Sum of total Null values: ", data.isnull().sum())
    return data

def fillNullValues():
    print(data.fillna(0, inplace=True))
    return data


def normalizeData():
    line()
    normalizeColumns = []
    print("Which columns do you want to normalize: ")
    answer = input("Answer Here: ")
    normalizeColumns.extend(answer.strip().split(","))
    if answer != "":
        try:
            data[normalizeColumns] = data[normalizeColumns].apply(pd.to_numeric)
            data[normalizeColumns] = normalize(data[normalizeColumns])
            print("Normalizaiton for the columns Done")
        except pd.errors.NullFrequencyError:
            print("The Data may contain NaN values or try again")
        finally:
            print("The Data may contain NaN values or try again")
            normalizeData()
    else:
        print("No Columns selected")
        mainMethod()
    return data

def mainMethod(data):
    line()
    print("The Following operations could be done:")
    print("1) Display Dataset")
    print("2) SHape of Data")
    print("3) Describe Data")
    print("4) Information of Data")
    print("5) Show Columns Names")
    print("6) Check for Null Values")
    print("7) Fill null values with Mean")
    print("8) Manage categorical Values (One oHot Encoding)")
    print("9) Check for String Values (if any)")
    print("10) Drop duplicate Values (if any)")
    print("11) Remove Column")
    print("12) Check for feature Selection (not yet implemented)")
    print("13) Normalization")
    print("14) Handle Imbalanced Data")
    print("15) Export Data set")
    line()
    choice = input("Answer here (1,2,3...): ")
    if choice == "1":
        line()
        print("All Data", data.head(5))
        mainMethod(data)
    elif choice == "2":
        line()
        print("Null Values Phase")
        print(data.shape)
        mainMethod(data)
    elif choice == "3":
        line()
        print("Filling Null values Phase")
        print(data.describe())
        mainMethod(data)
    elif choice == "4":
        line()
        print("Categorical Phase")
        print(data.info)
        mainMethod(data)
    elif choice == "5":
        line()
        print("String Values Phase")
        print(data.columns)
        mainMethod(data)
    elif choice == "6":
        line()
        data = checkForNullValues()
        mainMethod(data)
    elif choice == "7":
        line()
        data = fillNullValues()
        mainMethod(data)
    elif choice == "8":
        line()
        data = doingOneHotEncoding(data)
        print("features selection Phase")
        mainMethod(data)
    elif choice == "9":
        line()
        print("Normalization Phase")
        data = checkForStringValues()
        mainMethod(data)
    elif choice == "10":
        line()
        print("Dropping Values")
        mainMethod(data)
    elif choice == "11":
        line()
        print("removing Phase")
        data = removalOfColumn(namesOfColumnsWantsToConvert)
        mainMethod(data)
    elif choice == "12":
        line()
        print("Checking for features selection")
        mainMethod(data)
    elif choice == "13":
        line()
        data = normalizeData()
        mainMethod(data)
    elif choice == "14":
        line()
        print("Handle imbalance data")
        mainMethod(data)
    elif choice == "15":
        line()
        print("exporting Phase")
        data.to_csv("Final_Data.csv", index=False)
        mainMethod(data)
    else:
        line()
        print("You chose nothing...")
        mainMethod()

    return data



mainMethod(data)

