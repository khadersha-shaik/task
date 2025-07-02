print("\n \n \n ===========================task_1=============================== \n\n\n")

try:
    txt=open("sample.txt ","r" )
    print("Reading file content:")
    ln=0
    for line in txt:
        ln+=1
        print(f"Line {ln}: {line}")

    txt=open("error.txt ","r" )
    print("Reading file content:")
    ln=0
    for line in txt:
        ln+=1
        print(f"Line {ln}: {line}")
        
except Exception as e :
    print(e)
    



print("\n \n \n ========================================================== \n\n\n")


print("\n \n \n ==============================task_2======================== \n\n\n")

try:
    file_name="output.txt"
    txt=open(file_name,"w")
    
    line = input("Enter text to write to file :")
    txt.write(line+"\n")
    txt.close()
    print(f"data sucessfully written to {file_name}")
    txt=open(file_name,"a")
    line = input("Enter text to append to file :")
    txt.write(line)
    print("data sucessfully appended.")
    print(f"final content of {file_name}")
    txt=open(file_name,"r")
    lines=txt.readlines()
    for line in lines:
        print(line)
    
except Exception as e:
    print(e)
