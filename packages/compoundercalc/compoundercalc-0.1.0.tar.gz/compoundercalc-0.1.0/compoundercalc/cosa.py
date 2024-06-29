import os

def remove_trailing_whitespace(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line.rstrip() + '\n')

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                remove_trailing_whitespace(file_path)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    directory = input("Enter the directory to process: ")
    process_directory(directory)
    print("Trailing whitespace removed from all Python files.")
