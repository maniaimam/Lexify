# Token list
tokens = [
    ['!', '!', 1], ['purr', 'purr', 1], ['|', '|', 1], ['iostream', 'iostream', 1], ['|', '|', 1],
    ['DT', 'depression', 2], ['Identifier', 'Fibonacci_', 2], ['(', '(', 2], [')', ')', 2],
    ['{', '{', 3],
    ['DT', 'num', 4], ['Identifier', 'Num_', 4], ['Equals Operator', 'equals', 4], ['int_const', '0', 4], [',', ',', 4],
    ['Identifier', 'Num2_', 4], ['Equals Operator', 'equals', 4], ['int_const', '1', 4], [',', ',', 4],
    ['Identifier', 'Num$_', 4], ['Equals Operator', 'equals', 4], ['int_const', '0', 4], [',', ',', 4],
    ['Identifier', 'N_', 4], ['-', '-', 4],
    ['yap', 'yap', 5], ['String_const', '"Enter a positive number:"', 5], ['-', '-', 5],
    ['yap', 'yap', 6], ['String_const', '"Series"', 6], [',', ',', 6], ['Identifier', 'Num1_', 6], [',', ',', 6],
    ['Identifier', 'Num2_', 6], [',', ',', 6], ['String_const', '","', 6], ['-', '-', 6],
    ['Identifier', 'Num$_', 7], ['Equals Operator', 'equals', 7], ['Identifier', 'Num1_', 7], ['ADDSUB Operator', 'plus', 7],
    ['Identifier', 'Num2_', 7], ['-', '-', 7],
    [],
    ['fosho', 'fosho', 9], ['(', '(', 9], ['Identifier', 'Num_', 9], ['Relational Operator', 'smallerthan', 9],
    ['Identifier', 'N_', 9], [')', ')', 9],
    ['{', '{', 10],
    ['yap', 'yap', 11], ['Identifier', 'Num$_', 11],
    ['Identifier', 'Num1_', 12], ['Equals Operator', 'equals', 12], ['Identifier', 'Num2_', 12], ['-', '-', 12],
    ['Identifier', 'Num2_', 13], ['Equals Operator', 'equals', 13], ['Identifier', 'Num$_', 13], ['-', '-', 13],
    ['Identifier', 'Num$_', 14], ['Equals Operator', 'equals', 14], ['Identifier', 'Num1_', 14],
    ['ADDSUB Operator', 'plus', 14], ['Identifier', 'Num_', 14], ['-', '-', 14],
    ['}', '}', 15],
    ['}', '}', 16],
    ['DT', 'num', 17], ['Identifier', 'Key_', 17], ['(', '(', 17], [')', ')', 17],
    ['{', '{', 18],
    ['yap', 'yap', 19], ['String_const', '"Fibonacci"', 19], ['-', '-', 19],
    ['Identifier', 'Fibonacci_', 20], ['(', '(', 20], [')', ')', 20], ['-', '-', 20],
    ['ghost', 'ghost', 21], ['int_const', '0', 21], ['-', '-', 21],
    []
]

def generate_intermediate_code(tokens):
    # Initialize an empty list for intermediate code
    intermediate_code = []

    # Iterate through the tokens
    for token in tokens:
        # Check if the token list is not empty
        if token:
            # Extract relevant information from the token
            token_type = token[0]
            token_value = token[1]
            line_number = token[2]

            # Check for specific token types and generate intermediate code accordingly
            if token_type == 'Identifier':
                intermediate_code.append(f'{token_value} = {line_number}')
            elif token_type == 'ADDSUB Operator':
                intermediate_code.append(f'{token_value} = {line_number}')
            elif token_type == 'Relational Operator':
                intermediate_code.append(f'if {line_number}:')
            elif token_type == 'String_const':
                intermediate_code.append(f'print({token_value})')
            elif token_type == 'yap':
                intermediate_code.append(f'print({token_value})')
            elif token_type == '}':
                intermediate_code.append('}')

    # Return the generated intermediate code
    return intermediate_code
print("Intermediate Code Generated:")
# Call the function with your token list
result = generate_intermediate_code(tokens)

# Print the intermediate code
for line in result:
    print(line)


