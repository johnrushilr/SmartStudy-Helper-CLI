from storage import add_new, get_all, find_by_id, delete_note
from ai_module import make_summary, create_questions

def show_menu():
    print("\n--- Study Helper CLI ---")
    print("1. Add note")
    print("2. View notes")
    print("3. Summarize note")
    print("4. Generate questions")
    print("5. Delete note")
    print("6. Exit")


def add_note():
    title = input("Title: ")
    content = input("Content: ")

    if title == "" or content == "":
        print("Empty input, try again.")
        return

    add_new(title, content)
    print("Note saved.")


def view_notes():
    notes = get_all()

    if len(notes) == 0:
        print("No notes yet.")
        return

    for n in notes:
        print(f"\nID: {n['id']}")
        print("Title:", n['title'])


def summarize():
    try:
        nid = int(input("Enter note id: "))
    except:
        print("Invalid input.")
        return

    note = find_by_id(nid)

    if note is None:
        print("Note not found.")
        return

    result = make_summary(note["content"])

    print("\nSummary:")
    print(result)


def generate_q():
    try:
        nid = int(input("Enter note id: "))
    except:
        print("Invalid input.")
        return

    note = find_by_id(nid)

    if note is None:
        print("Note not found.")
        return

    qs = create_questions(note["content"])

    if len(qs) == 0:
        print("Not enough content to make questions.")
        return

    print("\nQuestions:")
    for i, q in enumerate(qs):
        print(f"{i+1}. {q}")


def remove_note():
    try:
        nid = int(input("Enter id to delete: "))
    except:
        print("Invalid input.")
        return

    delete_note(nid)
    print("Deleted if id existed.")


def main():
    while True:
        show_menu()
        choice = input("Choice: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            summarize()

        elif choice == "4":
            generate_q()

        elif choice == "5":
            remove_note()

        elif choice == "6":
            print("bye")
            break

        else:
            print("Wrong option.")


if __name__ == "__main__":
    main()