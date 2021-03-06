import os

# METHODS
# Text decoration
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

# Menu?
def menu(ops):
	msgMenu = txtDec('- MENU -', 'bold', 'yellow')
	print(f"{10*' '}{msgMenu}")
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

# Create a new HTML file
def initHtml(name, dire):
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

# Get the position of a tag with the id
def getPos(arc, slc):
	doc = open(arc, 'r')
	docContent = doc.readlines()
	endHead = False
	i = 0
	for pos,line in enumerate(docContent):
		if docContent[pos-1] == "</head>\n":
			endHead = True
		if endHead and "<" in line and ">" in line:
			indent = line.count('	')
			line.strip()
			if "/" in line and line[line.index(">")-1] == "/":
				if indent == 0:
					i = int(i+1)
				else:
					i = round(i+0.1, 1)
			elif "/" not in line:
				if indent == 0:
					i = int(i+1)
				else:
					i = round(i+0.1, 1)
		if i == slc:
			return pos
	return False

# Add tags for a HTML document
def addHtml(tag, arc, slc=0, atr=''):
	self_close = ("area","base","br","col","command","embed","hr","img","input",
		"keygen","link","menuitem","meta","param","source","track","wbr")
	
	if "#" in tag:
		tag = tag.split('#')[0]
	if "." in tag:
		tag = tag.split('.')[0]

	if slc == 0:
		doc = open(arc, 'a')
		if tag in self_close:
			doc.write(f"<{tag}{atr}/>\n")
		else:
			doc.write(f"<{tag}{atr}>\n")
			doc.write(f"</{tag}>\n")
		doc.close()
	else:
		doc = open(arc, 'r')
		docContent = doc.readlines()
		pos = getPos(arc, slc)
		indent = docContent[pos].count('	') + 1
		n = pos+1
		for line in docContent[n:]:
			if line.count('	') <= docContent[pos].count('	'):
				if tag in self_close:
					docContent.insert(n,f"{indent*'	'}<{tag}{atr}/>\n")
				else:
					docContent.insert(n, f"{indent*'	'}<{tag}{atr}>\n")
					docContent.insert(n+1, f"{indent*'	'}</{tag}>\n")
				break
			else:
				n+=1
		doc = open(arc, 'w')
		doc.writelines(docContent)
		doc.close()

# Add tags before other tag
def beforeHtml(arc, slc, tags):
	self_close = ("area","base","br","col","command","embed","hr","img","input",
		"keygen","link","menuitem","meta","param","source","track","wbr")

	doc = open(arc, 'r')
	docContent = doc.readlines()
	pos = getPos(arc, slc)
	indent = docContent[pos].count('	')
	n = 0
	for tag in tags:
		atr = getAtr(tag)
		if "#" in tag:
			tag = tag.split('#')[0]
		if "." in tag:
			tag = tag.split('.')[0]
		pos += n
		if tag in self_close:
			docContent.insert(pos,f"{indent*'	'}<{tag}{atr}/>\n")
			n+=1
		else:
			docContent.insert(pos, f"{indent*'	'}<{tag}{atr}>\n")
			docContent.insert(pos+1, f"{indent*'	'}</{tag}>\n")
			n+=2
	doc = open(arc, 'w')
	doc.writelines(docContent)
	doc.close()

# Remove a tag
def rmHtml(arq, sl):
	doc = open(arq, 'r')
	docContent = doc.readlines()
	pos = getPos(arq, sl)
	tag = docContent[pos].strip()
	if "/" in tag:
		docContent.pop(pos)
	else:
		indent = docContent[pos].count('	')
		close_tag = "</" + tag[tag.index("<")+1:]
		for i,t in enumerate(docContent):
			if i > pos and t.strip() == close_tag and t.count('	') == indent:
				docContent.pop(i)
				break
		docContent.pop(pos)
	doc = open(arc, 'w')
	doc.writelines(docContent)
	doc.close()

# Get the class and the id of a tag
def getAtr(tag):
	atr = ''
	if '#' in tag and '.' in tag:
		atr = tag.split("#")[1]
		atr = atr.split(".")
		atr = f" id='{atr[0]}' class='{atr[1]}'"
	elif '#' in tag:
		atr = tag.split("#")[1]
		atr = f" id='{atr}'"
	elif '.' in tag:
		atr = tag.split('.')[1]
		atr = f" class='{atr}'"
	return atr

# Show the tags of a HTML
def listHtml(arc):
	doc = open(arc, 'r')
	docContent = doc.readlines()
	docName = os.path.basename(arc)
	endHead = False
	print(f"\n-> {docName}")
	i = 0
	for pos,line in enumerate(docContent):
		if docContent[pos-1] == "</head>\n":
			endHead = True
		if endHead and "<" in line and ">" in line:
			show = False
			indent = line.count('	')
			line.strip()
			if "/" in line and line[line.index(">")-1] == "/":
				showLine = line[line.index("<")+1:line.index("/")]
				if indent == 0:
					i = int(i+1)
				else:
					i = round(i+0.1, 1)
				show = True
			elif "/" not in line:
				showLine = line[line.index("<")+1:line.index(">")]
				if indent == 0:
					i = int(i+1)
				else:
					i = round(i+0.1, 1)
				show = True
			if show:
				print(f"{indent*'   '}{i}-{showLine}")

# All comands are here
def comands(arc, new=True):
	slc = 0
	docName = os.path.basename(arc)
	while(True):
		cmd = str(input("\nYour comand: ")).split(',')
		for c in cmd:
			c = c.strip()
			if c ==  "--exit":
				break
			elif c == "uslc":
				slc = 0
			elif "slc" in c:
				slc = float(c.split(' ')[1])
				exist = getPos(arc, slc)
				if not exist:
					print("This item not exist!")
					slc = 0
			elif "bfr" in c:
				c = c.split(' ')
				sl = float(c[1])
				tags = c[2:]
				exist = getPos(arc, sl)
				if not exist:
					print("This item not exist!")
				else:
					beforeHtml(arc, sl, tags)
			elif "rm" in c:
				c = c.split(' ')
				sl = float(c[1])
				exist = getPos(arc, sl)
				if not exist:
					print("This item not exist!")
				else:
					rmHtml(arc, sl)
			else:
				atr = getAtr(c)
				addHtml(c, arc, slc, atr)
		if c == "--exit":
			if new:
				doc = open(arc, 'a')
				doc.write("</html>")
				doc.close()
			print("Bye :)")
			break
		listHtml(arc)

# MAIN CODE
# Seting requirements
fileDir = os.path.dirname(os.path.realpath(__file__))
dirCont = os.listdir(fileDir)
if "html" not in dirCont:
	os.mkdir(os.path.join(fileDir, "html"))

# Menu 
op = menu(["1-Create HTML", "2-Modify HTML", "3-Exit"]) # <= Menu options

# Option 1: Create HTML
if op == 1:
	print(30*'-')
	docName = str(input("Document name: ")).strip()
	if docName[-5:] != ".html":
		docName += ".html"
	print()
	print("Leave it blank for save in the default diretory:")
	print(os.path.join(fileDir, "html"))
	print()
	while(True):
		docDir = str(input("Document diretory: ")).strip()
		if docDir == '':
			docDir = os.path.join(fileDir, "html")
			break
		elif os.path.exists(docDir) and os.path.isdir(docDir):
			break
		else:
			print("Invalid diretory!")
	initHtml(docName, docDir)
	arc = os.path.join(docDir, docName)
	# Comands
	comands(arc)

# Option 2: Edit HTML
if op == 2:
	print(30*'-')
	while(True):
		docDir = str(input("Document diretory: ")).strip()
		try:
			open(docDir, 'r')
			break
		except:
			print("Invalid diretory!")
	# Comands
	listHtml(docDir)
	comands(docDir, False)

# Option 3: Exit
if op == 3:
	print("Bye :)")