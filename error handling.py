# File Read & Write Challenge + Error Handling Lab

def main():
    # Ask user for input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified version to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()