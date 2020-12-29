# Methods
def addProf(name, clear=False):
	profContent = [f"prof= {name}"]
	if not clear:
		doc = open("data/profiles.conf", 'r')
		profContent.append(doc.readlines()).sort()
	doc = open("data/profiles.conf", 'w')
	doc.writelines(profContent)
	doc.close()

def userSelect():
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
	else:
		print("Select profile ('p' to create a new profile):")
		print()
		for i,p in enumerate(allProf):
			print(f"{i+1}. {p}")
		print()
		op = str(input("Option: "))
		try:
			op = int(op)
		except:
			try:
				op = str().lower()
				if op == "p":
					print("Create a new profile:")
					n = str(input("Name: "))
					addProf(n)
				else:
					print("Invalid profile!")
			except:
				print("Invalid profile!")

# Main code
print(f"{8*'-='} HTML GENERATOR {8*'=-'}")
print()
userSelect()
