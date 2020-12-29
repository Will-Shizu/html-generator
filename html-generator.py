# Methods
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
			if op > len(allProf) or op <= 0:
				print("Invalid profile!")
			else:
				print("Deu certo mlk")
		except:
			op = op.lower()
			if op == "p":
				print("Create a new profile:")
				n = str(input("Name: "))
				addProf(n)
			else:
				print("Invalid profile!")

# Main code
print(f"{8*'-='} HTML GENERATOR {8*'=-'}")
print()
userSelect()
