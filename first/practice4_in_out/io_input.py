# 用户输入内容 
def reverse(text):
    return text[::-1]

def is_palindrom(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrom(something):
    print("Yes, it is a palindrome")
else:
    print("No,it is not a palindrome")
    