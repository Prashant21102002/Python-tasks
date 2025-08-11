# Take user input and write to output.txt
user_input = input("Enter text to write to the file: ")
with open('output.txt', 'w') as f:
    f.write(user_input + '\n')
    print("Data successfully written to output.txt.")
# Append additional data
additional_input = input("Enter additional text to append: ")
with open('output.txt', 'a') as f:
    f.write(additional_input + '\n')
    print("Data successfully appended.")
# Read and display the final content
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as f:
    for line in f:
        print(line, end='')  # end='' to avoid double newlines