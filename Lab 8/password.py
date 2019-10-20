name = input("Please input your username:")
testPass = input("Please enter a password:")
validSymbols = "!","@","#","$","%","^","&","*","(",")","_","+","[","]","{","}"
if testPass.find(name) != -1:
  print("Please enter a password that does not contain your name.")
elif testPass.find("password") != -1:
  print("Please enter a password that does not contain 'password'.")
elif testPass.find("pass") != -1:
  print("Please enter a password that does not contain 'password'.")
elif testPass.find("word") != -1:
  print("Please enter a password that does not contain 'password'.")
elif len(testPass) < 8:
  print("Passwords must contain more than 8 characters.")
elif not any(x.isupper() for x in testPass):
  print("Password must contain at least one capital letter.")
elif not any(x.isdigit() for x in testPass):
  print("Password must contain at least one number.")
elif not any(x in validSymbols for x in testPass):
  print("Passwords must contain at least one symbol.")
else:
  print("Password entered is valid.")
import hashlib, binascii, os
salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
pwdhash = hashlib.pbkdf2_hmac('sha512', testPass.encode('utf-8'),salt, 100000)
pwdhash = binascii.hexlify(pwdhash)
stored_password = (salt + pwdhash).decode('ascii')
print("Hashed password:",stored_password)
checkPass = input("Please re-enter password to verify:")
salt = stored_password[:64]
stored_password = stored_password[64:]
pwdhash = hashlib.pbkdf2_hmac('sha512',checkPass.encode('utf-8'),salt.encode('ascii'),100000)
pwdhash = binascii.hexlify(pwdhash).decode('ascii')
if pwdhash == stored_password:
  print("Password verified.")
else:
  print("Passwords do not match.")
