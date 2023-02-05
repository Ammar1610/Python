class Palindrome():
    def reverse(self,str):
        return(str[::-1])
    def isPalindrome(self,str):
        if(str==str[::-1]):
            return(True)
        else:
            return(False)   
P = Palindrome()
string = input("enter your string:")
print(P.reverse(string))
print(P.isPalindrome(string))