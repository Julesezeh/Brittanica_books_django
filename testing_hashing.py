import bcrypt 

password1  = "jamesst.patrick"
password1 = password1.encode("utf-8")
password2 = bcrypt.hashpw(password1,salt=bcrypt.gensalt())

print(password2)