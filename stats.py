def get_word_count_from_string(input_string):
    word_list = input_string.split()
    return len(word_list)

def get_character_count_from_string(input_string):
    count_dictionary = {}
    for char in input_string:
        if char.isalpha():
            lowercase_char = char.lower()
            if lowercase_char in count_dictionary:
                count_dictionary[lowercase_char] += 1
            else:
                count_dictionary[lowercase_char] = 1
    return count_dictionary

def get_char_list_from_dict(input_dict):
    return_list = []
    for char in input_dict:
        return_list.append({"name": char, "count": input_dict[char]})
    return return_list

def get_count(char_count_dict):
    return char_count_dict["count"]

def get_characters_by_frequency(input_string):
    count_dict = get_character_count_from_string(input_string)
    count_list = get_char_list_from_dict(count_dict)
    count_list.sort(reverse=True, key=get_count)
    return count_list

def format_char_count_report(unformatted_report):
    report = ""
    for count_dict in unformatted_report:
        report += f"{count_dict["name"]}: {count_dict["count"]}\n"
    report = report[:-1]
    return report

def get_character_frequency_report(input_string):
    unformatted_report = get_characters_by_frequency(input_string)
    return format_char_count_report(unformatted_report)