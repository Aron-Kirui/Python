def create_file():
    try:
       
        with open("my_file.txt", "w") as file:
            
            file.write("Python is a versatile language.\n")
            file.write("12345\n")
            file.write("Another line with some numbers: 98765\n")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation completed.")


def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An error occurred:", e)


def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Appending line 1.\n")
            file.write("Appending line 2.\n")
            file.write("Appending line 3.\n")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File appending completed.")


# Main function to execute the tasks
def main():
    create_file()
    read_file()
    append_file()


if __name__ == "__main__":
    main()
