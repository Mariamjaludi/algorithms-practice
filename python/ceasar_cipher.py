def ceasarCipherEncryptor(string, key):
    newKey = key % 26
    ans = []
    for l in string:
        uniVal = ord(l) + newKey
        if uniVal <= 122:
            ans.append(chr(uniVal))
        else:
            ans.append(chr(96 + uniVal%122))
    return ''.join(ans)            
