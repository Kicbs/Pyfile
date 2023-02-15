def decrypt_caesar(ciphertext):
    #tries all key
    plaintext_candidates = []
    # Try all possible keys from 1 to 26
    for key in range(1, 27):
        plaintext = ""
        # Shift each character of the ciphertext by the key value
        for char in ciphertext:
            if char.isalpha():
                shift = ord(char) - key
                if char.isupper():
                    if shift > ord('Z'):
                        shift -= 26
                    elif shift < ord('A'):
                        shift += 26
                elif char.islower():
                    if shift > ord('z'):
                        shift -= 26
                    elif shift < ord('a'):
                        shift += 26
                plaintext += chr(shift)
            else:
                plaintext += char
        # Add the plaintext to the list of candidates
        plaintext_candidates.append(plaintext)
    return plaintext_candidates

ciphertext = "cnkxk oy znk zxgot"
# Call the function and get the list of plaintext candidates
plaintext_candidates = decrypt_caesar(ciphertext)
# Print the candidates along with the key used
for i, candidate in enumerate(plaintext_candidates):
    print("Candidate plaintext for key" ,i+1, candidate)
