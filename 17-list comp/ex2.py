#Accept a string from the user and convert every word into upper case

str=input("Enter a string:")
print([ ch.upper() for ch in str.split() ])