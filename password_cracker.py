import hashlib

def crack_sha1_hash(hash, use_salts = False):

    with open("top-10000-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file]
    
    if use_salts:
        # Load salts from the file
        with open("known-salts.txt", "r") as file:
            salts = [line.strip() for line in file]
    else:
        # If not using salts, just use an empty list
        salts = [""]

    # Check each password and each salt combination
    for password in passwords:
        for salt in salts:
            # Prepare the salted passwords
            salted_password_prepend = salt + password
            salted_password_append = password + salt
            
            # Hash the salted passwords
            hashed_password_prepend = hashlib.sha1(salted_password_prepend.encode()).hexdigest()
            hashed_password_append = hashlib.sha1(salted_password_append.encode()).hexdigest()
            
            # Check if either hashed salted password matches the input hash
            if hashed_password_prepend == hash or hashed_password_append == hash:
                return password

    return "PASSWORD NOT IN DATABASE"