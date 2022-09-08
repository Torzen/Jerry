import hashlib

def encript(a):
    string = str(a)
    encoded = string.encode()
    hash = hashlib.sha256(encoded)
    hashed = hash.hexdigest()
    return hashed

if __name__ == "__main__":
    print(encript('Bishal is great'))
