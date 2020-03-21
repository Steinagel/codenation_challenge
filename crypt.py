import json
from hashlib import sha1

file = "answer.json"

def decrypt(file=file):
    data = {}

    with open(file, 'r') as f:
        data = json.load(f)

    encryp_text = data["cifrado"]
    nth         = data["numero_casas"]
    decryp_text = "".join([_decript_char(l,nth)  for l in encryp_text])

    data.update({"decifrado": decryp_text})

    with open(file, 'w') as f:
        json.dump(data, f)

    return decryp_text

def encrypt(txt, file=file):
    data = {}

    with open(file, 'r') as f:
        data = json.load(f)

    txt = txt.lower()

    data.update({
                "resumo_criptografico": 
                    sha1(txt.encode()).hexdigest()
                })

    with open(file, 'w') as f:
        json.dump(data, f)

    return True

def _decript_char(char, step):
    step = step if ord(char.lower()) - step >= ord('a') \
                    else step+26
    return chr(ord(char.lower()) - step ) if char.isalpha() else char.lower()

if __name__=='__main__':
    decryp_text = decrypt()

    if encrypt(decryp_text):
        print("success")