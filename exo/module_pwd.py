def is_password_secure(password, required_score):
    special_chars = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
    score = 0

    for char in password:
        if char.isalpha():
            score += 1
        elif char.isdigit():
            score += 0.5
        elif char in special_chars:
            score += 3

    if len(password) < 8:
        score -= 10

    return score >= required_score

if __name__ == "__main__":
    pwd = input("Enter a password: ")
    print(is_password_secure(pwd, 10))