import hashlib

def encript(a):
    string = str(a)
    encoded = string.encode()
    hash = hashlib.sha256(encoded)
    hashed = hash.hexdigest()
    return hashed

if __name__ == "__main__":
    string="we-fix-it"
    encoded=string.encode()
    result = hashlib.sha256(encoded)
    print("String : ", end ="")
    print(string)
    print("Hash Value : ", end ="")
    print(result)
    print("Hexadecimal equivalent: ",result.hexdigest())
    print("Digest Size : ", end ="")
    print(result.digest_size)
    print("Block Size : ", end ="")
    print(result.block_size)
