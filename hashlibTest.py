import hashlib

message = "Hi Nss67"

hashed = hashlib.sha256()
hashed.update(message.encode())

message_hashed = hashed.hexdigest()

print(message_hashed)
