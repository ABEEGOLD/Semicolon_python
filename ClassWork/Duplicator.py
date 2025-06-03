
# brute force technique

def uniqueCharacters(str):
    
  
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False;

        return True;


# Driver 
str = "GeeksforGeeks";

if(uniqueCharacters(str)):
    print("The String ", str," has all unique characters");
else:
    print("The String ", str, " has duplicate characters");

