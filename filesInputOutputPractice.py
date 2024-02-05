s="Happy,to learn the things and be a Devops Engineer."
with open("test.txt","w") as f:
    f.write(s)

#With is a Context manager.When we use open() method the 1st parameter is a Name of file with extension,and it has a mode called as write(w),append(a),read(r).

f1=open("test.txt","r")
rs=f1.readline()
print(rs)

f1=open("test.txt","a")
f1.write(".yes done")
#mostly,in a file three operations occurs "read","write" and "append". 