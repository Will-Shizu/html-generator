# HTML Generator
 - [English](#english)
 - [Português](#português)

## English 
 A Python script to generate HTML documents.

### Comands
 - Any HTML tag name: create an HTML tag.
 - `Select` or `slc`: Selects an element, the next tags after that command will be children of the selected tag.
 - `Unselect` or `uslc`: Unselect the tag.
 - `--exit`: Exit the script.

When you create a new HTML document the head tag is automatically generated:
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>
```
### Examples:
**Syntax:** `body`
**Output:**
```
-> [document name].hmtl
1-body
```
**Result:**
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>

<body>
</body>
```

**Syntax:** `select 1, main, footer`
**Output:**
```
-> [document name].hmtl
1-body
   1.1-main
   1.2-footer
```
**Result:**
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>

<body>
	<main>
	</main>
	<footer>
	</footer>
</body>
```

**Syntax:** `slc 1, header, uslc, script`
**Output:**
```
-> [document name].hmtl
1-body
   1.1-header
   1.2-main
   1.3-footer
2-script
```
**Result:**
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>

<body>
	<header>
	</header>
	<main>
	</main>
	<footer>
	</footer>
</body>
<script>
</script>
```

**Syntax:** `--exit`
**Output:**
```
Bye
```
**Result:**
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>

<body>
	<header>
	</header>
	<main>
	</main>
	<footer>
	</footer>
</body>
<script>
</script>
</html>
```

## Português
 Um script em python para gerar documentos HTML.
### Comandos
 - Nome de qualquer tag HTML: cria uma tag HTML.
 - `Select` ou `slc`: Seleciona um elemento, as próximas tags depois desse comando serão filhas da tag selecionada.
 - `Unselect` or `uslc`: Tira a seleção de uma tag.
 - `--exit`: Sai do script.

Quando você cria um novo documento HTML a tag head é gerada automaticamente:
```
<!DOCTYPE html>
<html lang=[chosen by the user]>
<head>
	<meta charset=[chosen by the user]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[user name]>
	<title>[chosen by the user]</title>
</head>
```
### Exemplos:
**Syntax:** `body`
**Output:**
```
-> [nome do documento].hmtl
1-body
```
**Resultado:**
```
<!DOCTYPE html>
<html lang=[escolhido pelo usuário]>
<head>
	<meta charset=[escolhido pelo usuário]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[nome do usuário]>
	<title>[escolhido pelo usuário]</title>
</head>

<body>
</body>
```

**Syntax:** `select 1, main, footer`
**Output:**
```
-> [nome do documento].hmtl
1-body
   1.1-main
   1.2-footer
```
**Resultado:**
```
<!DOCTYPE html>
<html lang=[escolhido pelo usuário]>
<head>
	<meta charset=[escolhido pelo usuário]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[nome do usuário]>
	<title>[escolhido pelo usuário]</title>
</head>

<body>
	<main>
	</main>
	<footer>
	</footer>
</body>
```

**Syntax:** `slc 1, header, uslc, script`
**Output:**
```
-> [nome do documento].hmtl
1-body
   1.1-header
   1.2-main
   1.3-footer
2-script
```
**Resultado:**
```
<!DOCTYPE html>
<html lang=[escolhido pelo usuário]>
<head>
	<meta charset=[escolhido pelo usuário]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[nome do usuário]>
	<title>[escolhido pelo usuário]</title>
</head>

<body>
	<header>
	</header>
	<main>
	</main>
	<footer>
	</footer>
</body>
<script>
</script>
```

**Syntax:** `--exit`
**Output:**
```
Bye
```
**Resultado:**
```
<!DOCTYPE html>
<html lang=[escolhido pelo usuário]>
<head>
	<meta charset=[escolhido pelo usuário]>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="author" content=[nome do usuário]>
	<title>[escolhido pelo usuário]</title>
</head>

<body>
	<header>
	</header>
	<main>
	</main>
	<footer>
	</footer>
</body>
<script>
</script>
</html>
```

