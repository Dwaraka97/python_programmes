import csv


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year of publication: "))
    library['Title'] = title
    library['Author'] = author
    library['Year'] = year
    with open("library.csv", 'a') as library_file:
        writer = csv.DictWriter(library_file, fieldnames=["Title", "Author", "Year"])
        writer.writeheader()
        writer.writerow(library)


def list_books():
    with open("library.csv", 'r') as read_file:
        reader = csv.DictReader(read_file)
        for line in reader:
            print(f"{line['Title']} is written by {line['Author']} published in {line['Year']}")


def search_book():
    book = input("Enter the book Title you want to search: ")
    with open("library.csv", 'r') as read_file:
        reader = csv.DictReader(read_file)
        for line in reader:
            if line['Title'].lower() == book.strip().lower():
                print(f"{line['Title'].lower()} is written by {line['Author']} published in {line['Year']}")
                break
        else:
            print(f"The book {book} is not available in the library!")


library = {}
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        list_books()
    elif selected_option == "s":
        search_book()
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")
    selected_option = input(menu_prompt).strip().lower()
