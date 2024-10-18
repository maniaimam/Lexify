import re

PN_Keywords = "yap|dawg|sike|also|cap|facts|salty|base|func|con|bussin|purr|or|ghost|rent-free|girlboss|loop|gaslight|slay|iostream|reverse|main|chill|non|twocents|levels|fosho|case"
PN_Datatypes = "dec|num|calm|rizz|bin|girlboss|depression"
PN_ADDSUBOperators = "plus|minus"
PN_UnaryOperators = "inc|dec"
PN_DIVMULOperators = "mul|div|mod"
PN_RelationalOperators = "smallerthan|largerthan|notequal|equalequal"
PN_LogicalOperators = "and|or"
PN_AssignOperators = "plusequals|minusequals|divequals|modequals"
PN_EqualsOperator = "equals"
PN_Identifiers = "^[A-Z]+[a-zA-Z0-9$@#]*_"
tokenset = []


def tokenize():
    myfile = open("Lexify.txt", "r")
    count = 0
    patt = "##*"
    Output = open('LexifyOutput.txt', 'w')
    for inputline in myfile:
        if (re.search(patt, inputline)):
            continue
        else:

            Output.write(inputline)
    Output.close()
    Output = open('LexifyOutput.txt', 'r')
    while True:

        count = count + 1
        line = Output.readline()
        if not line:
            break

        WB = [' ', ',', '(', '{', '[', ']', '}', ')', ';', '=', '+', '-', '*', ':', '>', '<', '\'', '\"', '.', '!', '|']
        i = 0
        wordHolder = ""
        tokens = []
        while (i < len(line) - 1):

            if line[i] in WB:
                # print(line[i] , line[i]=='=', not opHolder , wordHolder)
                if re.search(PN_Keywords, wordHolder):
                    tokens.append([wordHolder, wordHolder, count])
                elif re.search(PN_Identifiers, wordHolder):
                    tokens.append(['Identifier', wordHolder, count])
                elif re.search(PN_ADDSUBOperators, wordHolder):
                    tokens.append(['ADDSUB Operator', wordHolder, count])
                elif re.search(PN_UnaryOperators, wordHolder):
                    tokens.append(['Unary Operator', wordHolder, count])
                elif re.search(PN_DIVMULOperators, wordHolder):
                    tokens.append(['DIVMUL Operator', wordHolder, count])
                elif re.search(PN_RelationalOperators, wordHolder):
                    tokens.append(['Relational Operator', wordHolder, count])
                elif re.search(PN_LogicalOperators, wordHolder):
                    tokens.append(['Logical Operator', wordHolder, count])
                elif re.search(PN_AssignOperators, wordHolder):
                    tokens.append(['Assign Operator', wordHolder, count])
                elif re.search(PN_EqualsOperator, wordHolder):
                    tokens.append(['Equals Operator', wordHolder, count])
                elif re.search(PN_Datatypes, wordHolder):
                    tokens.append(['DT', wordHolder, count])

                if line[i] != ' ':
                    if line[i] == '=':
                        tokens.append(['AssignOP', line[i]])
                    if line[i] != '"' and line[i] != "'":
                        # Punctuator
                        tokens.append([line[i], line[i], count])

                wordHolder = ""

            else:
                # do nothing if the wordholder is empty and the first value is an integer
                # check for integer value and not add it into the wordholder
                if line[i] >= '0' and line[i] <= '9' and not wordHolder:
                    k = 1
                else:
                    wordHolder += line[i]

                    # to check if any string const is being read
            if i < len(line) and line[i] == '"' or line[i] == "'":
                tempStr = line[i]
                val = line[i]
                i += 1
                found = False
                while (i < len(line)):
                    if (line[i] == val):
                        tempStr += line[i]
                        found = True
                        break
                    tempStr += line[i]
                    i += 1
                if found:
                    tokens.append(['String_const', tempStr, count])
            # to check if any int/float const is being read
            if not wordHolder and i < len(line) and line[i] >= '0' and line[i] <= '9':
                isFloat = False
                tempVal = line[i]
                while ((i + 1 < len(line) and (line[i + 1] >= '0' and line[i + 1] <= '9')) or (
                        line[i + 1] == '.' and (i + 2 < len(line) and line[i + 2] >= '0' and line[i + 2] <= '9'))):
                    if line[i + 1] == '.':
                        isFloat = True
                    tempVal += line[i + 1]
                    i += 1
                if isFloat:
                    tokens.append(['Float_const', tempVal, count])
                else:
                    tokens.append(['int_const', tempVal, count])
            i += 1

        if wordHolder:
            if re.search(PN_Keywords, wordHolder):
                tokens.append([wordHolder, wordHolder, count])
            elif re.search(PN_Identifiers, wordHolder):
                tokens.append(['Identifier', wordHolder, count])
            elif re.search(PN_ADDSUBOperators, wordHolder):
                tokens.append(['ADDSUB Operator', wordHolder, count])
            elif re.search(PN_UnaryOperators, wordHolder):
                tokens.append(['Unary Operator', wordHolder, count])
            elif re.search(PN_DIVMULOperators, wordHolder):
                tokens.append(['DIVMUL Operator', wordHolder, count])
            elif re.search(PN_RelationalOperators, wordHolder):
                tokens.append(['Relational Operator', wordHolder, count])
            elif re.search(PN_LogicalOperators, wordHolder):
                tokens.append(['Logical Operator', wordHolder, count])
            elif re.search(PN_AssignOperators, wordHolder):
                tokens.append(['Assign Operator', wordHolder, count])
            elif re.search(PN_EqualsOperator, wordHolder):
                tokens.append(['Equals Operator', wordHolder, count])
            elif re.search(PN_Datatypes, wordHolder):
                tokens.append(['DT', wordHolder, count])
            else:
                print("Lexical Error @ line", count, " invalid ID")

        tokenset.append(tokens)
        print(tokens)
    Output.close()


print("\tTOKENIZE")
tokenize()
Output = open('TOKENS_output.txt', 'w')
for token in tokenset:
    Output.write("{token1}\n".format(token1=token))
Output.close()
tk = []
print("\nShow all Class Part")
PNClasspart = open('LexifyClassParts.txt','w')
for x in range(len(tokenset)):
    tk = (tokenset[x])
    x += 1
    for i in range(len(tk)):
        PNClasspart.write(tk[i][0] + "\n")