with open('bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()

    print(f'--- Begin of  {f.name} ---')

    def numberOfWords(file_contents):
        words = file_contents.split()
        return len(words)
    print(f'{numberOfWords(file_contents)} words found in the document')

    print()
    
    def counting_letters(file_contents):
        char_count = {}
        
        for char in file_contents.lower():
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
        return char_count

    char_count = counting_letters(file_contents)
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print('--- End report ---')
   
    
#print(file_contents)

