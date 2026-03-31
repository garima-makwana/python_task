"""f=open("d1.txt","w")
f.write("Hello Garima")
f.write("Welcome to python file handling.\n")
f.write("Learning is fun!\n")
f.close()"""

"""f=open("d1.txt","w")
f.write("New Content only.\n ")
f.close()"""

"""f=open("d1.txt","a")
f.write("This line is added at the end.\n")
f.close()"""

f=open("d1.txt","w")
lines=["Python Programming"
"File Handling\n"
"Error Handling\n"
"Exception Handling\n"
]
f.writelines(lines)
f.close()