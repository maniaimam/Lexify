import re
print("\n\t\t\t\t\t****************************************************************")
print ("\t\t\t\t\t\t\t\tTYPE CHECKING")
print("\t\t\t\t\t****************************************************************\n")
inp = input("\n\nEnter your input: ")
dt = ["num", "calm", "rizz","dec"]
tok = []
tok = inp.split(" ")
print(tok, "\n")

def checkk(typee, value):
    if typee == "digit" and re.match("^[0-9]+$", value):
        return True
    elif typee == "st" and re.match('^"[\w]+"$', value):
        return True
    elif typee == "ascii" and re.match("^'[A-Za-z0-9]'$", value):
        return True
    else:
        return False

def main():
    error = False
    flag = True
    i = 0
    namee = ""
    tipe = ""
    while i < len(tok):
        if tok[i] in dt:
            flag = True

            while i < len(tok) and flag == True:
                if tok[i] in dt:
                    tipe = tok[i]
                    i += 1

                else:
                    print("ERROR: Datatype expected but got something else")
                    error = True
                    i += 1

                if re.match("^[A-Z]+[a-zA-Z0-9$@#]*_", tok[i]):
                    namee = tok[i]
                    i += 1

                else:
                    print("ERROR: Invalid Variable Name")
                    error = True
                    i += 1

                if tok[i] == "equals":
                    i += 1

                else:
                    print("ERROR: 'equals' expected but got something else")
                    error = True
                    i += 1

                if checkk(tipe, tok[i]):
                    tipe = ""
                    i += 1
                    print("No Error")

                else:
                    print("ERROR:", namee, "'s Datatype Mismatch")
                    error = True
                    i += 1

                if tok[i] == "-" or tok[i] == "":
                    i + 1
                    flag = False

                else:
                    print("ERROR:", namee, "'s Terminator missing")
                    error = True
                    i += 1

    else:
        i += 1

main()
