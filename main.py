with open('input_file.txt', 'r') as input_file:
    with open('output_file.txt', 'w') as output_file:
        input_content = input_file.read()
        
        output_content = ' '.join(input_content.lower().split('.')).capitalize() + '! :)'

        output_file.writelines([output_content])