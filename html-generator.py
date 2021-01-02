# Document methods
def addProf(name, clear=False):
	if not clear:
		doc = open("data/profiles.conf", 'r')
		profContent = doc.readlines()
	else:
		profContent = []
	profContent.append(f"prof= {name}\n")
	if len(profContent) > 1:
		profContent.pop(0)
	profContent = sorted(profContent)
	profContent.insert(0, "# Your profile names are stored here\n\n")
	if "\n" in profContent:
		profContent.remove("\n")
	doc = open("data/profiles.conf", 'w')
	doc.writelines(profContent)
	doc.close()

def editTemp(user):
	lines = []
	doc = open(f"./data/all-profiles/{user}.conf", 'w')
	lang = str(input("Set a default language: ")).strip()
	lines.append(f'lang={lang}\n')
	cs = str(input("Set a default charset: ")).strip()
	lines.append(f'charset={cs}\n')
	doc.writelines(lines)
	doc.close()

def ghtml(user):
	tab = "	"
	docName = str(input("Document name: "))
	title = str(input("Title: "))
	di = "./html"
	print(f"Your file will be saved in {di}")
	while(True):
		asw = str(input("Want to choose a different directory? [y/n] ")).lower()
		if asw == 'y':
			di = str(input("Choose directory: "))
			break
		elif asw == 'n':
			break
		else:
			print("Invalid option!")
	content = ["<!DOCTYPE hmtl>\n"]
	uConf = open(f"./data/all-profiles/{user}.conf", 'r')
	confLns = uConf.readlines()
	for i, ln in enumerate(confLns):
		if ln[:5] == "lang=":
			lang = ln[5:].strip()
		if ln[:8] == "charset=":
			cs = ln[8:].strip()
	content.append(f'<html lang="{lang}">\n')
	content.append(f'<head>\n')
	content.append(f'{tab}<meta charset="{cs}">\n')
	content.append(f'{tab}<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
	content.append(f'{tab}<meta name="author" content="{user}">\n')
	content.append(f'{tab}<title>{title}</title>\n')
	content.append("</head>\n")
	doc = open(f"{di}/{docName}.html", 'w')
	doc.writelines(content)
	doc.close()
	print()
	print(f"{9*' '}{10*'-'} COMANDS {10*'-'}")
	print()
	print("How to use: https://github.com/will-shizu/html-generator")
	global pos
	pos = False
	con = True
	while(con):
		con = comands(pos, di, docName)
		if con != False:
			con = True
	doc = open(f"{di}/{docName}.html", 'a')
	doc.write("</html>")

def comands(pos,di,docName):
	print()
	doc = open(f"{di}/{docName}.html", 'r')
	content = doc.readlines()
	noClose = ("meta", "hr", "br", "area","base","col","embed","img","input","link","param","source","track","wbr")
	c = str(input("Your comand: ")).strip()
	if "," in c:
		i = 0
		c = c.split(",")
		for tg in c:
			tg = tg.strip()
			if tg == "--exit":
				print("Bye")
				return False
			elif tg == "unselect" or tg == "uslc":
				pos = False
			elif "select" in tg or "slc" in tg:
				slc = float(tg.split(" ")[1])
				endHead = content[content.index("</head>\n")+1:]
				for n,l in enumerate(endHead):
					if ("<" in l) and (">" in l):
						ind = l.count("	")
						if "/" in l:
							if l[l.index(">") - 1] == "/":
								print("This tag cannot have children!")
						else:
							tag = l[l.index("<")+1:l.index(">")]
							if ind == 0:
								i = int(i)
								i +=1
							else:
								i += 0.1
								i = round(i, 1)
							if i == slc:
								pos = n+2;
								break
				pos = pos + content.index("</head>\n")
			elif tg in noClose:
				if not pos:
					content.append(f"<{tg}/>\n")
				else:
					content.insert(pos, f"{(ind+1)*'	'}<{tg}/>\n")
					pos+=1
			else:
				if not pos:
					content.append(f"<{tg}>\n")
					content.append(f"</{tg}>\n")					
				else:
					content.insert(pos, f"{(ind+1)*'	'}</{tg}>\n")
					content.insert(pos, f"{(ind+1)*'	'}<{tg}>\n")
					pos+=2
	else:
		if c == "--exit":
			print("Bye")
			return False
		elif c == "unselect" or c == "uslc":
				pos = False
		elif "select" in c or "slc" in c:
			slc = float(c.split(" ")[1])
			endHead = content[content.index("</head>\n")+1:]
			i = 0
			for n,l in enumerate(endHead):
				if ("<" in l) and (">" in l):
					ind = l.count("	")
					if "/" in l:
						if l[l.index(">") - 1] == "/":
							print("This tag cannot have children!")
					else:
						tag = l[l.index("<")+1:l.index(">")]
						if ind == 0:
							i = int(i)
							i +=1
						else:
							i += 0.1
							i = round(i, 1)
						if i == slc:
							pos = n+2;
							break
		elif c in noClose:
			if not pos:
				content.append(f"<{c}/>\n")
			else:
				content.insert(pos, f"{(ind+1)*'	'}<{c}/>\n")
		else:
			if not pos:
				content.append(f"<{c}>\n")
				content.append(f"</{c}>\n")					
			else:
				content.insert(pos, f"{(ind+1)*'	'}</{c}>\n")
				content.insert(pos, f"{(ind+1)*'	'}<{c}>\n")
	doc = open(f"{di}/{docName}.html", 'w')
	doc.writelines(content)
	doc.close()
	listTags(di,docName, noClose)


def listTags(di,docName,noClose):
	print()
	print(f"-> {docName}.html")
	doc = open(f"{di}/{docName}.html", 'r')
	content = doc.readlines()
	endHead = content[content.index("</head>\n")+1:]
	i = 0
	for l in endHead:
		if ("<" in l) and (">" in l):
			ind = l.count("	")
			if "/" in l:
				if l[l.index(">") - 1] == "/":
					tag = l[l.index("<")+1:l.index(">")-1]
					if ind == 0:
						i = int(i)
						i +=1
					else:
						i += 0.1
						i = round(i, 1)
					print(f"{ind*'   '}{i}-{tag}")
			else:
				tag = l[l.index("<")+1:l.index(">")]
				if ind == 0:
					i = int(i)
					i +=1
				else:
					i += 0.1
					i = round(i, 1)
				print(f"{ind*'   '}{i}-{tag}")

# "Interface" methods
def userSelect():
	print()
	doc = open("data/profiles.conf", 'r')
	profiles = doc.readlines()
	doc.close()
	allProf = []
	for i,p in enumerate(profiles):
		if "prof=" in p:
			allProf.append(p[5:].strip())
	if len(allProf) == 0:
		print("Create a new profile:")
		n = str(input("Name: "))
		addProf(n, True)
		return False
	else:
		print("Select profile ('p' to create a new profile):")
		print()
		for i,p in enumerate(allProf):
			print(f"{i+1}. {p}")
		print()
		op = str(input("Option: "))
		try:
			op = int(op)
			if op > len(allProf) or op <= 0:
				print("Invalid profile!")
			else:
				return allProf[op-1]
		except:
			op = op.lower()
			if op == "p":
				print("Create a new profile:")
				n = str(input("Name: "))
				if n not in allProf:
					addProf(n)
				else:
					print("This profile already exist!")
			else:
				print("Invalid profile!")
			return False

def menu(user):
	print()
	print(f"{12*' '}{10*'-'} MENU {10*'-'}")
	print()
	try:
		doc = open(f"./data/all-profiles/{user}.conf", 'r')
		print("1. Create HTML")
		print("2. Edit template")
		print("3. Exit")
		print()
		op = str(input("Option: ")).strip()
		try:
			op = int(op)
			if op == 1:
				return True
			if op == 2:
				editTemp(user)
			if op == 3:
				return "quit"
			else:
				print("Invalid option!")
				return False
		except:
			print("Invalid option!")
			return False
	except:
		editTemp(user)
		print("The template was been created!")
		return False

# Main code
print(f"{9*'-='} HTML GENERATOR {9*'=-'}")
while(True):
	user = userSelect()
	if user:
		break

while(True):
	exit = menu(user)
	if exit or exit == "quit":
		break
if exit != "quit":
	ghtml(user)
else:
	print("Bye")