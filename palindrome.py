def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False