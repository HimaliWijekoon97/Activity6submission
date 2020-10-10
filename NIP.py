
# Driver Code 
  
# number of inputs given  
n = 4;  
y = [[0 for i in range(10)]  
        for j in range(10)];  
x = [ 5, 6, 9, 11 ];  
  
# y[][] is used for divided difference  
# table where y[][0] is used for input  
y[0][0] = 12;  
y[1][0] = 13;  
y[2][0] = 14;  
y[3][0] = 16;  
  
# calculating divided difference table  
y=dividedDiffTable(x, y, n);  
  
# displaying divided difference table  
printDiffTable(y, n);  
  
# value to be interpolated  
value = 7;  
  
# printing the value  
print("\nValue at", value, "is", 
        round(applyFormula(value, x, y, n), 2)) 
  
# This code is contributed by mits 

