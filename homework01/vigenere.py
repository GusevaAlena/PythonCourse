def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    plaintext = list(plaintext)
    keyword = list(keyword)
    text_arr = list()
    key_arr = list()
    for k in keyword:
        if len(plaintext) > len(keyword):
            keyword.append(k)
            if len(keyword) == len(plaintext):
                break
        elif len(plaintext) < len(keyword):
            keyword.pop(-1)
            if len(keyword) == len(plaintext):
                break
        elif len(plaintext) == len(keyword):
            break
    for t in plaintext:
        t_code = ord(t)
        text_arr.append(t_code)
    for k in keyword:
        k_code = ord(k)
        key_arr.append(k_code)
    for i in range(0, len(plaintext)):
        if ord('A') <= (text_arr[i]) <= ord('Z'):
            diff = text_arr[i] - ord('A')
            shift = key_arr[i] - ord('A')
            t_code = (diff + shift) % 26 + ord('A')
        elif ord('a') <= (text_arr[i]) <= ord('z'):
            diff = text_arr[i] - ord('a')
            shift = key_arr[i] - ord('a')
            t_code = (diff + shift) % 26 + ord('a')
        elif ord(" ") == text_arr[i]:
            t_code = text_arr[i]
        ciphertext += chr(t_code)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    ciphertext = list(ciphertext)
    keyword = list(keyword)
    text_arr = list()
    key_arr = list()
    for k in keyword:
        if len(ciphertext) > len(keyword):
            keyword.append(k)
            if len(keyword) == len(ciphertext):
                break
        elif len(ciphertext) < len(keyword):
            keyword.pop(-1)
            if len(keyword) == len(ciphertext):
                break
        elif len(ciphertext) == len(keyword):
            break
    for t in ciphertext:
        t_code = ord(t)
        text_arr.append(t_code)
    for k in keyword:
        k_code = ord(k)
        key_arr.append(k_code)
    for i in range(0, len(ciphertext)):
        if ord('A') <= (text_arr[i]) <= ord('Z'):
            diff = text_arr[i] - ord('A')
            shift = key_arr[i] - ord('A')
            t_code = (diff - shift) % 26 + ord('A')
        elif ord('a') <= (text_arr[i]) <= ord('z'):
            diff = text_arr[i] - ord('a')
            shift = key_arr[i] - ord('a')
            t_code = (diff - shift) % 26 + ord('a')
        elif ord(" ") == text_arr[i]:
            t_code = text_arr[i]
        plaintext += chr(t_code)
    return plaintext