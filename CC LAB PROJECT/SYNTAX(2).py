import re
output_file_name = 'CFG_output.txt'
file = open('LexifyClassParts.txt','r')
file = file.read()
string = file
DataType = ["rizz", "num", "dec", "calm", "DT"]
Keyword = ["iostream","insert","for", "key", "if", "switch", "case", "ret", "while", "print", "cout"]
Relational = ["Relational_Operator"]
const = ["st_const","deci_const", "digit_const"]
Arithmetic=["ADDSUB_operator"]
loops = ["aslongas","since","act"]
incre = ["++", "--"]
Iden=["Identifier"]
Equals = ["equals"]
Punctuators = ["(", ")", "{", "}", "!", "|",","]


def parseTree(value):
    if value in Arithmetic:
        return "Arithmetic OP"
    if value in Punctuators:
        return value
    if value in loops:
        return value
    if value in DataType:
        return "DataType"
    if value in Relational:
        return "Relational Op"
    if value in incre:
        return "Incre Op"
    if value in Keyword:
        return value
    if value in Iden:
        return "ID"
    if value in Equals:
        return "equals"
    if value in const:
        return value
    if (value == "-"):
        return "Terminator"
    else:
        return "Error"
stri = string.split();
print(stri)
print('\n')
cfg = []
for char in stri:
    cfg.append(parseTree(char))
print(cfg)
with open(output_file_name, 'w') as output_file:
    output_file.write('\n'.join(cfg))

print(f"CFGs saved to {output_file_name}")
