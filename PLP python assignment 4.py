def main():
    filename = input("Enter the filename to read: ")
    try:
        
        with open(filename, "r") as file:
            content = file.readlines()

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
        return
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

    modified_content = [line.upper() for line in content]

    
    new_filename = "modified_" + filename
    try:
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)
        print(f"✅ Modified file written successfully as '{new_filename}'")
    except Exception as e:
        print(f"❌ Error writing file: {e}")
if __name__ == "__main__":
    main()
