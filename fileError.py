try:
	file=open(input("Enter the name of the file: "))
	print(file.read(),"\n")
except FileNotFoundError:
	print("File Not Found")

