l=24
print("value of l is:",l)


#With def function
def magic():
    m="hero"
    n=23
   # z=m+n
print(magic())


#To resolve these types of error we can use: try-catch-finally block
def manage(m,n):
    print("Love all")
    try:
        z=m+n
    except TypeError:
        print("Type Error occured")
    else:
        print(z,"addition of m and n is possible")
manage(23,"Heap")

a=45
b=15
try:
    m=a/b
except ZeroDivisionError:
    print("zero division value is not working")
except NameError:
    print("Name Error occured")
finally:
    print("divion done")

try:
    a=int(input("Enter each values:"))
except Exception as ex: #This except is a generic approach
    print("error occured called as"+ex+":",a) 
    #Here the error occured called as valueError.To resolve these error we use try-except block.
else:
    print("its working,proceed")


    
