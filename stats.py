def count_number_of_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    character_count = {}
    characters = list(text.lower())
    for character in characters:
        if character not in character_count:
            character_count[character] = 1
        else: 
            character_count[character] += 1
    return character_count

def sort_dictionary(all_characters):
    def sort_on(items):
        return items["character number"]
    
    dictionary_list = []
    for character in all_characters:
        character_entry = {"character name" : character, "character number" : all_characters[character]}
        dictionary_list.append(character_entry)
    
    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list
