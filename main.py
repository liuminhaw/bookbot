def count_words(content):
    return len(content.split())

def count_characters(content):
    counts = {}
    for c in content:
        if not c.isalpha():
            continue

        c_lower = c.lower()
        if c_lower in counts:
            counts[c_lower] += 1
        else:
            counts[c_lower] = 1

    return counts

def comp_counts(item): 
    return item['counts']


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    records = []
    for k, v in count_characters(file_contents).items():
        records.append({'letter':k, 'counts':v})
    records.sort(reverse=True, key=comp_counts)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(file_contents)} words found in the document')
    print()
    for item in records:
        print(f"The '{item['letter']}' character was found {item['counts']} times")
    print('--- End report ---')

