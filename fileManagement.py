import os


def create_file(file_name):
    if os.path.exists(file_name):
        print(f"Error: File '{file_name}' already exists.")
    else:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"Error: File '{file_name}' does not exist.")


def list_files(directory="."):
    files = os.listdir(directory)
    if len(files) == 0:
        print("No files in the current directory.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)


def create_directory(directory_name):
    if os.path.exists(directory_name):
        print(f"Error: Directory '{directory_name}' already exists.")
    else:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")


def delete_directory(directory_name):
    if os.path.exists(directory_name):
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted successfully.")
    else:
        print(f"Error: Directory '{directory_name}' does not exist.")


def change_directory(directory_name):
    if os.path.exists(directory_name) and os.path.isdir(directory_name):
        os.chdir(directory_name)
        print(f"Changed directory to '{directory_name}'.")
    else:
        print(f"Error: Directory '{directory_name}' does not exist.")


def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            print(f"--- Content of '{file_name}' ---")
            print(file.read())
    else:
        print(f"Error: File '{file_name}' does not exist.")


def write_file(file_name):
    if os.path.exists(file_name):
        print(f"File '{file_name}' already exists. Do you want to update it? (Y/N)")
        choice = input().upper()
        if choice == 'Y':
            with open(file_name, 'a') as file:
                print(f"Enter the content to append to '{file_name}' (press Ctrl+D to save):")
                while True:
                    try:
                        line = input()
                        file.write(line + "\n")
                    except EOFError:
                        break
                print(f"File '{file_name}' updated successfully.")
    else:
        with open(file_name, 'w') as file:
            print(f"Enter the content for '{file_name}' (press Ctrl+D to save):")
            while True:
                try:
                    line = input()
                    file.write(line + "\n")
                except EOFError:
                    break
            print(f"File '{file_name}' created and written successfully.")


def update_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            existing_content = file.read()

        print(f"--- Existing Content of '{file_name}' ---")
        print(existing_content)

        with open(file_name, 'w') as file:
            print(f"Enter the updated content for '{file_name}' (press Ctrl+D to save):")
            while True:
                try:
                    line = input()
                    file.write(line + "\n")
                except EOFError:
                    break
            print(f"File '{file_name}' updated successfully.")
    else:
        print(f"Error: File '{file_name}' does not exist.")


# Main program
current_directory = "."

while True:
    print("\n------ File Simulation System ------")
    print("1. Create File")
    print("2. Delete File")
    print("3. List Files")
    print("4. Create Directory")
    print("5. Delete Directory")
    print("6. Change Directory")
    print("7. Read File")
    print("8. Write File")
    print("9. Update File")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        file_name = input("Enter the file name: ")
        create_file(os.path.join(current_directory, file_name))
    elif choice == '2':
        file_name = input("Enter the file name: ")
        delete_file(os.path.join(current_directory, file_name))
    elif choice == '3':
        list_files(current_directory)
    elif choice == '4':
        directory_name = input("Enter the directory name: ")
        create_directory(os.path.join(current_directory, directory_name))
    elif choice == '5':
        directory_name = input("Enter the directory name: ")
        delete_directory(os.path.join(current_directory, directory_name))
    elif choice == '6':
        directory_name = input("Enter the directory name: ")
        change_directory(os.path.join(current_directory, directory_name))
        current_directory = os.getcwd()
    elif choice == '7':
        file_name = input("Enter the file name: ")
        read_file(os.path.join(current_directory, file_name))
    elif choice == '8':
        file_name = input("Enter the file name: ")
        write_file(os.path.join(current_directory, file_name))
    elif choice == '9':
        file_name = input("Enter the file name: ")
        update_file(os.path.join(current_directory, file_name))
    elif choice == '10':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting File Simulation System.")
