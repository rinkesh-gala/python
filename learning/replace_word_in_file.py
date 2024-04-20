#replace java with python in practice.txt file

with open("practice.txt","r+") as f:
    data=f.read()
    data_replace=data.replace("java","python")
    
with open("practice.txt","w") as f:
    f.write(data_replace)