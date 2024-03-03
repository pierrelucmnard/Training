def lasso_letter(letter,shift_amount):
    lettreASCII = ord(letter.lower())
    #lettreASCII += shift_amount
    a_ascii = ord('a')
    alphabet_size = 26
    true_letter_code = a_ascii+(((lettreASCII - a_ascii)+shift_amount)%alphabet_size)

    return chr(true_letter_code)

def lasso_word(word, shift_amount):
        
        decoded_word = ""

        for letter in word:
            decoded_letter = lasso_letter(letter,shift_amount)
            decoded_word += decoded_letter
        
        return decoded_word

#print(lasso_word( "Ncevy", 13 ) )
#print(lasso_word( "gpvsui", 25 ) )
#print(lasso_word( "ugflgkg", -18 ) + lasso_word("wjmmf", -1))
print(lasso_letter("p",-2))
