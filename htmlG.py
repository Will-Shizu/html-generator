import os

# METHODS
def txtDec(txt, stl='none',cl='white'):
	#font style
	if stl == 'bold':
		s = 1
	elif stl == 'underline':
		s = 2
	else:
		s = 0 # <- none

	#font color
	if cl == 'black':
		c = 30
	elif cl == 'red':
		c = 31
	elif cl == 'green':
		c = 32
	elif cl == 'yellow':
		c = 33
	elif cl == 'blue':
		c = 34
	elif cl == 'purple':
		c = 35
	elif cl == 'cyan':
		c = 36
	else:
		c = 37 # <- white

	return f"\033[{s};{c}m{txt}\33[m"

def menu(ops):
	print(f"{10*' '}{txtDec('- MENU -', 'bold', 'yellow')}")
	print()
	for option in ops:
		print(option)
	while(True):
		print()
		op = str(input("Select option: ")).strip()
		try:
			op = int(op)
			if (op > 0) and (op <= len(ops)):
				return op
			else:
				print("Invalid option!")
		except:
			print("Invalid option!")

def initHtml(name, dire):
	if name[-5:] != ".html":
		name += ".html"
	head = ["<!DOCTYPE html>"]
	head.append("<html>")
	head.append("<head>")
	head.append("	<meta name='viewport' content='width=device-width, initial-scale=1'>")
	head.append("</head>")
	for pos in range(0, len(head)):
		head[pos]+="\n"
	doc = open(os.path.join(dire, name), 'w')
	doc.writelines(head)
	doc.close()

# MAIN CODE
# Seting requirements
fileDir = os.path.dirname(os.path.realpath(__file__))
dirCont = os.listdir(fileDir)
if "html" not in dirCont:
	os.mkdir(os.path.join(fileDir, "html"))

# Menu 
op = menu(["1-Create HTML", "2-Modify HTML", "3-Exit"]) # <= Menu options
print(30*'-')

if op == 1:
	docName = str(input("Document name: ")).strip()
	print()
	print("Leave in blank to save in the default diretory:")
	print(os.path.join(fileDir, "html"))
	print()
	docDir = str(input("Document diretory: ")).strip()
	if docDir == '':
		docDir = os.path.join(fileDir, "html")

	initHtml(docName, docDir)