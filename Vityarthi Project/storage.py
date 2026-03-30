import json
import os

file_name = "data.json"

def load_notes():
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_notes(data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)


def add_new(title, content):
    notes = load_notes()

    new_id = 1
    if len(notes) > 0:
        new_id = notes[-1]["id"] + 1

    notes.append({
        "id": new_id,
        "title": title,
        "content": content
    })

    save_notes(notes)


def get_all():
    return load_notes()


def find_by_id(nid):
    notes = load_notes()

    for n in notes:
        if n["id"] == nid:
            return n

    return None


def delete_note(nid):
    notes = load_notes()
    updated = []

    for n in notes:
        if n["id"] != nid:
            updated.append(n)

    save_notes(updated)