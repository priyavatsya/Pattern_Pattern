# Function to demonstrate printing pattern 
def pypart(n): 
      
    # outer loop to handle number of rows 
    # n in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ",end="") 
       
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
pypart(n) 


# Python 3.x code to demonstrate star pattern 
  
# Function to demonstrate printing pattern of numbers 
def contnum(n): 
      
    # initializing starting number  
    num = 1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # not re assigning num 
        # num = 1 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing number 
            print(num, end=" ") 
          
            # incrementing number at each column 
            num = num + 1
      
        # ending line after each row 
        print("\r") 
  
n = 5
  
# sending 5 as argument 
# calling Function 
contnum(n)

# Python code 3.x to demonstrate star pattern 
  
# Function to demonstrate printing pattern of alphabets 
def  contalpha(n): 
      
    # initializing value corresponding to 'A'  
    # ASCII value 
    num = 65
  
    # outer loop to handle number of rows 
-   for i in range(0, n): 
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # explicitely converting to char 
            ch = chr(num) 
          
            # printing char value  
            print(ch, end=" ") 
          
            # incrementing at each column 
            num = num +1
      
      
        # ending line after each row 
        print("\r") 
  
# Driver code 
n = 5
contalpha(n) 
