from textwrap import dedent

# steps
# print welcome message
# read template
# find all the diferents nouns inside {}, store them in a dictionaty with order. AKA nouns
# for each element in the noun dictonary, ask for user imput and store as a value.
# populate the template with the user input. Using .format(list of values)
# display completed script on terminal
# create a new file
# write the compled script on the new file

def showWelcome():
    welcome_msg = """
    //////////////////////////////////////////
    ////                                  ////
    ////     Welcome to Madlib Game !!!   ////
    ////                                  ////
    //////////////////////////////////////////

    Instructions:
    Please introduce the nouns solicited, the program will let you know when you are done, then the result will be display to you. 
    
    Enjoy!
    """
    print(welcome_msg)

if __name__ == "__main__":
    showWelcome()