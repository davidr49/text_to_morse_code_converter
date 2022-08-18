from ascii import ascii

key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', "'"]

value = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "- ", "..-", "...-", ".--", "-..-", "-.--", "--..", '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '.----.']

morse_code = {key[i]: value[i] for i in range(len(key))}


def translate():
    phrase_to_translate = list(input('Please write a word or sentence to translate into morse code: ').lower())
    translation = []
    for character in phrase_to_translate:
        for keys in morse_code:
            if character == keys:
                translation.append(f'{morse_code[keys]}/')
                final_translation = (" ".join(translation))
    print(f"Thanks! Here's your message in morse code: \n{final_translation}")


print(ascii)
print('Welcome to the Morse Code Converter!')

programme_on = True

while programme_on:
    translate()
    repeat = input('Would you like to translate another message? Type "yes" or "no"')
    if repeat == 'no':
        print('Thanks for using the Morse Code Converter. Have a nice day!')
        programme_on = False
