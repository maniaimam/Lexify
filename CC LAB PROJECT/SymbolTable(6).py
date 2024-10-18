import re
from beautifultable import BeautifulTable

mySymbolTable = BeautifulTable()
tokens = []
symbolTable = []


class Token:
    lineNo = 0
    valuePart = '-'
    classPart = '-'


class SymbolTable:
    scope = 0
    classPart = '-'
    valuePart = '-'

    def __init__(self, scope, classPart, valuePart):
        self.scope = scope
        self.classPart = classPart
        self.valuePart = valuePart


class LexicalAnalyser:
    def __init__(self):
        wordBreakers = [' ', ',', '(', '{', '[', ']', '}', ')', ';', '=', '+', '-', '*', ':', '>', '<', '\'', '\"', '.',
                        '!', '|', ]
        code = open('L0.txt', 'r')
        lineNo = 1
        while True:
            i = 0
            fileLine = code.readline()
            if not fileLine:
                break
            length = 1 if len(fileLine) == 1 else len(fileLine) - 1
            word = ""
            while i < length:
                if fileLine[i] in wordBreakers:
                    wordBreaker = fileLine[i]
                    if len(word) <= 1:
                        if (i + 1 < length) and ((fileLine[i] == "plus" and fileLine[i + 1] == "plus")
                                                 or (fileLine[i] == "minus" and fileLine[i + 1] == "minus")
                                                 or (fileLine[i] == "=" and fileLine[i + 1] == "=")
                                                 or ((
                                                             fileLine[i] == "mul"
                                                             or fileLine[i] == "div"
                                                             or fileLine[i] == "plus"
                                                             or fileLine[i] == "minus"
                                                     )
                                                     and fileLine[i + 1] == "equals"
                                                 )
                        ):
                            wordBreakers += fileLine[i + 1]
                            i += 1
                    if word != "":
                        self.createToken(word, lineNo)
                    self.createToken(wordBreaker, lineNo)
                    word = ""
                else:
                    word += fileLine[i]
                i += 1
            lineNo += 1

    def createToken(self, word, lineNo):
        hasError = False
        PN_Datatypes = "dec|num|calm|rizz|bin|girlboss|depression"
        PN_ADDSUBOperators = "plus|minus"
        PN_UnaryOperators = "inc|dec"
        PN_DIVMULOperators = "mul|div|mod"
        PN_RelationalOperators = "smallerthan|largerthan|notequal|equalequal"
        PN_LogicalOperators = "and|or"
        PN_AssignOperators = "plusequals|minusequals|divequals|modequals"
        PN_EqualsOperator = "="
        PN_Punctuators = ["(", "{", "[", ")", "}", "]", ",", "-", "|", "!", ""]
        PN_Identifiers = "^[A-Z]+[a-zA-Z0-9$@#]*_"

        token = Token()
        if word in PN_Datatypes:
            token.classPart = "DT"
        elif word in PN_Punctuators:
            token.classPart = word
        elif word in PN_UnaryOperators:
            token.classPart = "INCDEC"
        elif word in PN_AssignOperators:
            token.classPart = "AO"
        elif word in PN_ADDSUBOperators:
            token.classPart = "ADDSUB"
        elif word in PN_DIVMULOperators:
            token.classPart = "DIVMOD"
        elif word in PN_RelationalOperators:
            token.classPart = "RO"
        elif re.search(PN_Identifiers, word):
            token.classPart = "ID"
        elif self.isValidConstant(word, lineNo):
            token.classPart = "const"
        elif word == " ":
            return
        token.lineNo = lineNo
        token.valuePart = word
        tokens.append(token)

    def isValidConstant(self, word, lineNo):
        digit_const = r"^[+-]?\d+$"
        deci_const = r"^[+-]?\d+(\.\d+)?$"
        ascii_const = r"^(\\.|[ ^\\'])'$"
        st_const = r'^"(\\.|[ ^\\"])*"$'
        if re.match(digit_const, word):
            return True
        elif re.match(deci_const, word):
            return True
        elif re.match(ascii_const, word):
            return True
        elif re.match(st_const, word):
            return True
        else:
            return False


if __name__ == "__main__":
    analyser = LexicalAnalyser()
    print("\t\t\t\t\t****************************************************************")
    print("\t\t\t\t\t\t\t\tSYMBOL TABLE")
    print("\t\t\t\t\t****************************************************************\n")
    mySymbolTable.append_column("Scope", [])
    mySymbolTable.append_column("Type", [])
    mySymbolTable.append_column("ID", [])
    scope = 0
    type = ""

    for val in tokens:

        if val.valuePart == "{":
            scope += 1
        if val.classPart == "DT":
            type = val.valuePart
        if val.classPart == "ID" and type != "":
            table = SymbolTable(scope, val.valuePart, type)
            type = ""
            symbolTable.append(table)
        if val.valuePart == "}":
            scope -= 1
        if scope < 0:
            scope = 0
    for item in symbolTable:
        mySymbolTable.append_row([item.scope, item.valuePart, item.classPart])
print(mySymbolTable)



