def read_fsa_table(filename_list):
    all_fsa_table=[]
    all_fsa_char=[]
    for x in filename_list:
        file=open(x,"r")
        lines=file.readlines()
        file.close()
        lines=[ x.replace("\n","").split('\t') for x in lines]
        characters={ x[1] for x in lines}
        all_fsa_table.append(lines)
        all_fsa_char.append(characters)
    return all_fsa_table,all_fsa_char

def read_input(filename):
    file=open(filename)
    data=file.readline()
    file.close()
    return data.split()

def fsm_in_parallel(all_lines,all_characters,input_list,e_states ,s_state):
    lis=[]
    seprators={"=","+",'minus',"*","&","!","|"}
    keywords=['num','dec','calm','rizz','bin','girlboss','loop','fosho','dawg','con','gaslight','non','sike','bussin','slay','boujee','drip,''purr','depression','basic','also','or','reverse','levels','cap','facts','exclude','chill','salty','ghost','yap','twocents','base','rent-free','vibe','woke','plus','minus','mul','divmod','smallerthan','largerthan','equalsset','girlboss','slay']
    fsa_acceptance=[]
    for j in input_list:
        print("Processing String: ",j)
        input_lexeme_list=list(j)
        current_states=s_state
        fsa_acceptance=[ True for x in range(len(all_lines))]
        seprator_flag=False
        for index,char in enumerate(input_lexeme_list):
            if seprator_flag:
                seprator_flag=False
            if char in seprators:
                try:
                    if input_lexeme_list[index+1] in seprators:
                        print(f" ------  Seperator: {char}{input_lexeme_list[index+1]} ------ ")
                        seprator_flag=True
                        lis.append(f"{char}{input_lexeme_list[index+1]}")
                        break
                    else:
                        print(" ------ Seperator:",char,"  ------ ")
                        lis.append(char)
                        seprator_flag=True
                        break
                except:
                    print(" ------ Seperator:",char,"  ------ ")
                    seprator_flag=True
                    lis.append(char)
                    break

            for fsa in range(len(all_lines)):

                if char not in all_characters[fsa] :
                    fsa_acceptance[fsa]=False

                if fsa_acceptance[fsa]==False:
                    continue
                print(f"{fsa+1} current state: ",current_states[fsa])
                print("input processing: ",char)
                next_states=set()
                for current_state in current_states[fsa]:

                    for y in all_lines[fsa]:

                        if(y[0]==current_state and y[1]==char):
                            next_states.add(y[2])

                print("next states: ", next_states,"\n...")
                current_states[fsa]=next_states
        if seprator_flag==True:
            continue
        for i in range(len(all_lines)):
            if fsa_acceptance[i]==False:
                print("-----")
            else:
                isAccepted=False
                for x in current_states[i]:
                    if x in e_states[i]:
                        isAccepted=True

                        break
                if i==0 and isAccepted:
                    if j in keywords:
                        print("----- Keyword! string accepted! ------")
                        lis.append("k")
                    else:
                        print(f" ------ {i+1}  It is an identifer ------ ")
                        lis.append("i")
                    continue

                print("------")
    return lis


files=["identifier.txt","integer.txt"]
all_lines,all_characters=read_fsa_table(files)
input_list=read_input("input.txt")
end_states=[["1"],["1"]]
start_states=[{"0"},{"0"}]

data=fsm_in_parallel(all_lines,all_characters,input_list,end_states,start_states)

input=""
for x in data:
    if (x=="i" or x=="+"):
        input=input+x
input=input+"$"
print(input)
# input = "ii$" #$ is end of input,,
i=0
charc = input[i] # we will start with first charcter
rval = True # This is global flag to check whether parsing was succeed
# we are declaring input as global, so that it is accessable to all functions

# This function will match input charatcer with Grammar Charatcer
def match(var): # here charc point to the charcter, that need to be matched
    global i
    global input
    global charc
    global rval
    if(var == input[i] and var != "$"):
        # if the character is matched with string character, but it should not be the end character
         i=i+1  # You need to go to next character
         charc =  input[i]
         rval = True
         return rval #Its Fine Go Ahead,,as no error is their
    else:
        #print("\n There is an Error in the input string")
        rval = False
        return rval  # It means their is an Error, You need to quite

def E(): #This function implemnts E non-terminal
    global i
    global input
    global charc
    global rval
    if( charc == "i"):
        rval = match("i")
        if rval and charc !="$": #It means its True and we are not at end of input
            rval = E_bar()  # Then proceed further in parsing
        else:
            return rval
    else:
        return False
    return rval

def E_bar():
    global i
    global input
    global charc
    global rval
    if( charc == "+"):
        rval = match("+")
        #rval = match("i")
        if rval: # then match next i
            rval = match("i")
            if rval and charc != "$": # we are not at end of input
                rval = E_bar()
            else:
                return rval
        else:
            return rval # return rvale

    else:
        rval = False
        return rval # simply return to previous function in recusrrion
    return rval

if __name__ == "__main__": # This is the main Function
    #global rval
    rval = E()
    if( rval): # we reached end of parsing, and still rval is True
        print("\n Parsing Succeed")
        print("\n End---")