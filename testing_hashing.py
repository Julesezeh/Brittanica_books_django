import bcrypt

pass1  = "Johnson_slime"

pass2  = bcrypt.hashpw(pass1.encode("utf-8"), salt=bcrypt.gensalt())

print(pass2)