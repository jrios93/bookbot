from collections import Counter

def count_words(text):
    return len(text.split())

def count_character(text):
    text = text.lower()
    character_count = {}

    for character in text:
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def sort_list(character_count):
    sort_list = sorted([{"character": char, "count": count} for char, count in character_count.items()],
    key=lambda x: x["count"],
    reverse=True
    )

    return sort_list
    





        


 



    