#Write a function triplets that takes a number ‘n’ as argument and returns a list of triplets
#such that sum of first two elements of the triplet equals the third element using
#numbers below n. Please note that (a,b, c) and (b, a, c) represent same triplet.

def triplets(n): 
    return [ (a,c-a,c) for c in range(2,n) for a in range(1,c//2+1) ]
print(triplets(10))    
