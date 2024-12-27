import hashlib

data = input("Enter a data to generate hash value : ")
hash_object = hashlib.md5(data.encode())
hash_hex = hash_object.hexdigest()

print(f"MD5 hash : {hash_hex}")

data2 = input("Enter the second data : ")
hash_object2 = hashlib.md5(data2.encode())
hash_hex2 = hash_object2.hexdigest()

if hash_hex == hash_hex2:
    print("The inputs are both the same")
    print("The data has been verified !")
else:
    print("The value does not match with the first one")