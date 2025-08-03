def fact_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fact_iter(counter*product, counter+1, max_count)

def factorial(n):
    return fact_iter(1,1,n)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(factorial(50))
print(fact(50))
