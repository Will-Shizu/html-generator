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
			di = str(input("Choose directory"))
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
			cs = ln[5:].strip()
	content.append(f'<html lang="{lang}">\n')
	content.append(f'<head>\n')
	content.append(f'{tab}<meta charset="{cs}">\n')
	content.append(f'{tab}<meta name="viewport" content="width=device-width, initial-scale=1.0"\n')
	content.append(f'{tab}<meta name="author" content="{user}">\n')
	content.append(f'{tab}<title>{title}</title>\n')
	content.append("</head>")
	doc = open(f"{di}/{docName}.html", 'w')
	doc.writelines(content)

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
				return True
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
	if exit:
		break

ghtml(user)