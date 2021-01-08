## Select language:
 - [English](#english)
 - [Português](#português)

---

### English
# Python HTML generator
 This is a simple Python script for generate HTML documents with simple lines of comands.

## Requirements
For run this script you just need to **download the "htmlG.py"** archive and execute it with [**Python**](https://www.python.org/) v3.0 or higher.

### Download:

**Linux:**

For download only the "htmlG.py" file run this comand in the linux terminal:

`wget https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py`

**Other systems:**

If you don't have `wget` comand in your terminal you can download [this page](https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py) in your browser. 

## Comands

Comand | What it does
--- | ---
[Any HTML tag-name (Ex: body)](#html-tag) | **Create** a tag.
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

---
### slc
In the last example we put a `<body>` tag in the document, now let's give a child to it.
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

---
### uslc
To return the selection to default you can select the item 0 or use the `uslc` comand.

**Syntax**: `uslc`

---
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

---
### rm
This comand remove a tag by its number in the list

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

---
### --exit
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

---
### Id and Class
For add id and/or class to a tag just put '#id_name' and/or ".class_name" in the declaration of the tag.

**Syntax:** `div#id.class`

**Result:**
```
<div id="id" class="class">
</div>
```

You **NEED** to put first the id and then the class if you want both of then.

---
### Português
# Gerador de HTMl em Python
 Esse é um script Python simples para gerar documentos HTML com poucas linhas de comando.

## Requisitos
Para rodar esse script você só precisa **baixar o arquivo "htmlG.py"** e executa-lo com [**Python**](https://www.python.org/) v3.0 ou maior.

### Download:

**Linux:**

Para baixar apenas o arquivo "htmlG.py" execute esse comando no terminal linux:

`wget https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py`

**Outros sistemas:**

Se você não tem o comando `wget` no seu terminal você pode baixar [essa página](https://raw.githubusercontent.com/Will-shizu/html-generator/main/htmlG.py) no seu navegador. 


## Comands

Comando | O que ele faz
--- | ---
[Qualquer tag HTML (Ex: body)](#tag-html) | **Cria** uma tag.
[slc](#slc-*pt*) | **Seleciona** um item, o item selecionado vai se tornar a mãe das próximas tags adicionadas.
[uslc](#uslc) | **Remove a seleção**, retorna o item selecionado para o padrão (0).
[bfr](#bfr) | Adiciona tags **antes** de outra tag.
[rm](#rm) | **Remove** uma tag.
[--exit](#--exit) | **Sai** do script.

## Examples

### Tag HTML 
Adicionar tags é simples, você só precia inserir o nome da tag na linha de comando, vamos ver como se adiciona a tag `<body>`.
 
**Syntax:** `body`

**Resultado**
```
<!DOCTYPE html>
<html>
<head>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
</body>
```

**Obs.:** As tags `<!DOCTYPE>`,`<html>` e `<head>` são automaticamente geradas quando você cria um novo html com esse script.

**Output:**
```
-> [document-name].html
1-body
```

---
### slc (*pt*)
No ultimo exemplo nós inserimos uma tag `<body>` no documento, agora vamos dar a ela uma tag child.
**Syntax:** `slc 1, div#main`

**Resultado**
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

**Obs.:** Até a seleção mudar, todas as tags adicionadas serão suas filhas.

---
### uslc
Para retornar a seleção para o padrão você pode selecionar o item 0 ou usar o comando `uslc`.

**Syntax**: `uslc`

---
### bfr
A posição padrão para adicionar uma tag nesse script é abaixo da ultima tag filha, então nós precisamos de um comando para adicionar tags antes de outra tag, é isso que esse comando faz.

**Syntax:** `bfr 1.1 header main.block`

**Resultado**
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

**Obs.:** Nesse comando todas as tags precisam ser declarados na mesma linha de comando sem serem separadas por vírgula.

---
### rm
Esse comando remove uma tag pela seu número na lista.

**Syntax:** `rm 1.1`

**Resultado**
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

---
### --exit
Bem, nesse comando apenas sai do script, se o documento é novo ele fecha a tag `<html>` também.

**Syntax:** `exit`

**Resultado**
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
---
### Id e Classes
Para adicionar id e/ou classe em uma tag só coloque '#nome_id' e/ou ".nome_classe" na declaração da tag.

**Syntax:** `div#id.class`

**Resultado:**
```
<div id="id" class="class">
</div>
```

Você **PRECISA** colocar primeiro o id e depois a classe se você quiser ambos.