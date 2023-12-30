file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()

def wordcount(text):
    words = text.split()
    return len(words)

def lettercount(text):
    letters = {}
    for letter in file_contents.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_on(d):
    return d["num"]

def sorting_letter_count(letter_dict):
    sorted_list = []
    for char in letter_dict:
        sorted_list.append({"char": char, "num": letter_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def generate_report():
    print(f"-- Begin report of {file_path} --")
    print(f"{wordcount(file_contents)} words found in the document")
    print("")
    results = lettercount(file_contents)
    sorted_results = sorting_letter_count(results)
    for dict in sorted_results:
        if dict["char"].isalpha():
            print(f"The '{dict["char"]}' character was found {dict["num"]} times.")
    print("-- End report --")

generate_report()
