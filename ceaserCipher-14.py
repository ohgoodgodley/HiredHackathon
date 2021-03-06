#14: CaesarCipher(str,num) takes the str parameter and perform a Caesar 
#Cipher #shift on it using the num parameter as the shifting number. A 
#Caesar Cipher works by shifting each letter in the string N places down in 
#the alphabet (in this case N will be num). Punctuation, spaces, and 
#capitalization should remain intact. For example if the string is "Caesar 
#Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

def main():
	test_string = "Caesar Cipher!"
	cipher_shift = 2
	encoded_str = c_cipher(test_string, cipher_shift)
	print(encoded_str)

def c_cipher(in_string, num):
	out_string = ""
	#for each character in the instring check if it is an upper or lower case letter
	#against the unicode number
	for character in in_string:
		if ((ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122)):
			#if a letter shift the charater by the cipher number and add to output
			new_character = chr(ord(character) + num)
			out_string += new_character
		else:
			#if not add the existing non letter unicode character
			out_string += character
	return(out_string)

if __name__ == "__main__": main()