from textwrap import dedent

# steps
# print welcome message: done
# read template: done
# find all the diferents nouns inside {}, store them in a dictionaty with order. AKA nouns: done
# for each element in the noun dictonary, ask for user imput and store as a value.: DONE
# populate the template with the user input. DONE.
# display completed script on terminal DONE.
# create a new file: DONE
# write the compled script on the new file: DONE

def save_to_new_file(merged_content):
    try:
        path_file_to_save = "assets/parsed_file.txt"
        # TODO: overwite the file if exists
        with open(path_file_to_save, "a") as new_file:
            new_file.write(merged_content)
            new_file.write("\n")

        print("\nThe new file had been saved to the project.")
    except Exception as e:
        print('Error trying to save the content in a new file.', e)


def show_merged_content(merged_content):
    msg = """
    //////////////////////////////////////////
    ////                                  ////
    ////     This is your new file !!!    ////
    ////                                  ////
    //////////////////////////////////////////
    """
    print(msg)    
    print(merged_content)


def merge_file(content,nouns_list,answer_list):
    try:
        for i in range(len(nouns_list)):
            content = content.replace(("{" + nouns_list[i] + "}"), answer_list[i],1)
        
        return content

    except Exception as e:
        print('Error on merging the file.', e)


def ask_nouns(nouns_list):
    answer_list = []
    try:
        print('Now, enter your game words.... \n')
        i = 1
        total_nouns = len(nouns_list)
        for noun in nouns_list:
            print(str(i) + "/" + str(total_nouns),  "Please enter a:", noun)
            answer = input()
            answer_list.append(answer)
            i+=1

        print("\nThank you! now let's see your file!!!")
        
        return answer_list
    except Exception as e:
        print("Error on asking nouns to the user.", e)

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
    

def do_game(path_file_to_read):
    try:
        # content = "I the {Adjective} and {Noun} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective}"
        # answers = ['strong','chair','Ian','was','Emma','nice']
        
        show_welcome()
        content = read_file(path_file_to_read)        
        nouns = find_nouns(content)
        answers = ask_nouns(nouns)        
        merged_content = merge_file(content,nouns,answers)        
        show_merged_content(merged_content)
        save_to_new_file(merged_content)
    except:
        print("Error on doing the game.")
    


if __name__ == "__main__":    
    path_file_to_read = "assets/script_one.txt"    
    do_game(path_file_to_read)