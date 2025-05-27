# 9
def word_frequency_counter(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# 10
def character_counter(text):
    freq = {}
    for char in text:
        if char == ' ':
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# 11
def student_gradebook():
    records = {}
    while True:
        name = input("Enter name to add students. Enter 'stop' to terminate: ")
        if name.lower() == 'stop':
            break
        score = int(input(f"Enter grades for {name}: "))
        records[name] = score
    query = input("Query student name: ")
    print(records.get(query, "Not found"))