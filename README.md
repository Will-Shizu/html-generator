## Select language:
 - [English](#english)
 - [Português](#português)

---

### English
# Python HTML generator
 This is a simple Python script for generate HTML documents with simple lines of comands.

## Requirements
For run this script you just need to [**download the `htmlG.py`**](#download) archive and run it with [**Python**](https://www.python.org/) v3.0 or higher.

### Download:

**Linux:**
For download only the html.G file you can run this comand in the linux terminal:
`wget https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py`

**Other systems:**
If you don't have `wget` comand in your terminal you can just download this page in your browser:

[Go to page =>](https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py)

## Comands

Comand | What it does
--- | ---
[Any HTML tag-name (Ex: body, main, div...)](#html-tag) | **Create** a tag.
[slc](#slc) | **Select** a item, the selected item will be the mother of the next tags added.
[uslc](#uslc) | **Unselect**, set the selected item to default (0).
[bfr](#bfr) | Add tags **before** other tag.
[rm](#rm) | **Remove** a tag.
[--exit](#--exit) | **Exit** the script.

## Examples
### HTML tag
Add tags is simple, you just need to put the name of the tag in the comand line, let's see how add a `<body>` tag.

**Syntax:** `body`

**Result**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
</body>
```

**Ps.:** The `<!DOCTYPE>`,`<html>` and `<head>` tags are automaticaly generated when you create a new html with the script.

**Output:**
```
-> [document-name].html
1-body
```

### slc
In the last example we put a `<body>` tag in the document, now let's give some childs to it.
**Syntax:** `slc 1, div#main`

**Result**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
	<div id='main'>
	</div>
</body>
```

**Output:**
```
-> [document-name].html
1-body
   1.1-div id='main'
```

**Ps.:** Until the selection is changed all tags added will be its children.

### uslc
To return the selection to default you can just select the item 0 or use the `uslc` comand.

**Syntax**: `uslc`

### bfr
The default position to add add a tag in this script is below the last-child tag, so we need a comand to add tags before other tag, that's what this comand does.

**Syntax:** `bfr 1.1 header main.block`

**Result**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
	<header>
	</header>
	<main class='block'>
	</main>
	<div id='main'>
	</div>
</body>
```

**Output:**
```
-> [document-name].html
1-body
   1.1-header
   1.2-main class='block'
   1.3-div id='main'
```

**Ps.:** In this comand all the tags need to be declared in the same comand line without being separated by a comma.

## rm
This comand remove a tag by its id in the list

**Syntax:** `rm 1.1`

**Result**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
	<main class='block'>
	</main>
	<div id='main'>
	</div>
</body>
```

**Output:**
```
-> [document-name].html
1-body
   1.1-main class='block'
   1.2-div id='main'
```

## --exit
Well, this comand just leave the script, if the document is new it close the `<html>` tag too.

**Syntax:** `exit`

**Result**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
	<main class='block'>
	</main>
	<div id='main'>
	</div>
</body>
</html>
```

**Output:**
```
bye :)
```

## Id and Class
For add id or/and class to a tag just put '#id_name' or/and ".class_name" with the declaration of the tag.

**Syntax:** `div#id.class`

**Result:**
```
<div id="id" class="class">
</div>
```

You NEED to put first the id and then the class if you want both of then.