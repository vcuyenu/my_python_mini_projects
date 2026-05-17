def checker(word):
    
    length_ok = len(word)>= 8
    has_upper = any(ch.isupper() for ch in word)
    has_lower = any(ch.islower() for ch in word)
    has_digit = any(ch.isdigit() for ch in word)
    has_symbol = any(not ch.isalnum() and not ch.isspace() for ch in word)
    score = length_ok + has_upper + has_lower + has_digit + has_symbol
    
    if score == 5: strength = "strong"
    elif score >=3: strength = "medium"
    else: strength = "weak"
    
    rules = {
    " At least 8 characters  " : length_ok,
     " At least one upper case letter" :  has_upper,
     " At least one lowercade letter" : has_lower,
     " At lesst one number" : has_digit,
     " At least one symbol": has_symbol
    }
    
    for rule, passed in rules.items():
        if not passed:
            print(rule)
            
    return strength

print('''         ENTER A STRONG PASSWORD:
    - At least 8 charcters
    - Must contain upper and lower case
    - Must contain a symbol
    - Must contain a number
''')

stren = ""
while stren !=  "strong":
    password = input("    Enter a password: ")
    stren = checker(password)
    if stren != "strong":
        print(stren, ", not strong enough :-( ")
        
        
confirm = input("    Confirm password: ")
while confirm != password:
   confirm = input("    Re-enter password: ")

print("    Your new password is " , confirm)

    
    



