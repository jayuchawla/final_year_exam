
# Online Python - IDE, Editor, Compiler, Interpreter

def mean(x):
    s = 0
    for i in x:
        s = s + i
    return (s/len(x))
    
def mul_sums(x,y):
    mean_x, mean_y = mean(x),mean(y)
    diff_x = [i - mean_x for i in x]
    diff_y = [i - mean_y for i in y]
    
    s1 = 0
    for i in range(len(diff_y)):
        s1 = s1 + diff_x[i]*diff_y[i]
        
    s2 = 0 
    for i in diff_x:
        s2 = s2 + i**2
    
    b1 = s1/s2
    b0 = mean_y - mean_x*b1
    return b0,b1
    
print(mul_sums([10,9,2,15,10,16,11,16],[95,80,10,50,45,98,38,93]))