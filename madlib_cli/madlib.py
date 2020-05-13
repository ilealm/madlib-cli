from textwrap import dedent

# steps
# print welcome message: done
# read template: done
# find all the diferents nouns inside {}, store them in a dictionaty with order. AKA nouns
# for each element in the noun dictonary, ask for user imput and store as a value.
# populate the template with the user input. Using .format(list of values)
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# display completed script on terminal
# create a new file
# write the compled script on the new file




def find_nouns(content):
    try:
        nouns_list = []
        start = content.find('{')
        end = content.find('}')
        while start > -1: 
            noun = content[start+1:end]             
            nouns_list.append(noun)
            start = content.find('{',end)
            end = content.find('}',start)     
            noun = content[start+1:end]            
            if start < 0: break       
            
        return nouns_list
    except Exception as e:
        print("Error trying to find the nouns on the file.", e)


def read_file(path_file_to_read):
    try:
        with open(path_file_to_read,'r') as my_file:
                contents = my_file.read()
        return contents
    except:
        print('Error on reading the file')
    
    

def do_game(path_file_to_read):
    try:
        content = read_file(path_file_to_read)
        nouns = find_nouns(content)
        print('the nouns are', nouns)
    except:
        print("Error on doing the game.")
    


def show_welcome():
    welcome_msg = """
    //////////////////////////////////////////
    ////                                  ////
    ////     Welcome to Madlib Game !!!   ////
    ////                                  ////
    //////////////////////////////////////////

    Instructions:
    Please introduce the nouns solicited, the program will let you know when you are done, then the result will be display to you and saved to a file. 
    
    Enjoy!
    """
    print(welcome_msg)

if __name__ == "__main__":
    path_file_to_read = "assets/script_one.txt"
    # show_welcome()
    do_game(path_file_to_read)