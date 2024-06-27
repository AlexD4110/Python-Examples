def divisor(x):             
    def dividend(y):            
        return y/x      
    return dividend # return the function        

divide = divisor(2) # divide is now a function  
print(divide(10)) # 5.0                             

            
            
            
divide = divisor(20)  # divide is now a function
print(divide(100)) # 5.0\
# The function divisor returns the function dividend.
                        
            
            
divide = divisor(50) # divide is now a function
print(divide(80))