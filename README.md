🧱 Atajos Emmet para HTML
<!-- Estructura básica
! → Plantilla HTML5 básica.

html
Copiar
Editar
! <!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Document</title>
  </head>
  <body>
  </body>
</html>
The Linux Code

! html:5 → Estructura HTML5 completa.​
FreeCodeCamp

!Jerarquía y relaciones
nav>ul>li → Anidación de elementos.

html
Copiar
Editar
<nav>
  <ul>
    <li></li>
  </ul>
</nav>
! section>p+p+p → Elementos hermanos.

html
Copiar
Editar
<section>
  <p></p>
  <p></p>
  <p></p>
</section>
The Linux Code
+1
FreeCodeCamp
+1

! section>header>h1^footer → Subir un nivel en la jerarquía.

html
Copiar
Editar
<section>
  <header>
    <h1></h1>
  </header>
  <footer></footer>
</section>
! section>(header>nav>ul>li)+footer>p → Agrupación de elementos.

html
Copiar
Editar
<section>
  <header>
    <nav>
      <ul>
        <li></li>
      </ul>
    </nav>
  </header>
  <footer>
    <p></p>
  </footer>
</section>
Multiplicación y numeración
! ul>li*3 → Lista con 3 elementos.

html
Copiar
Editar
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>
carolinehe.github.io
+1
FreeCodeCamp
+1

! ul>li.item$*3 → Numeración automática.

html
Copiar
Editar
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
</ul>
! ul>li.item$$*3 → Numeración con ceros a la izquierda.

html
Copiar
Editar
<ul>
  <li class="item01"></li>
  <li class="item02"></li>
  <li class="item03"></li>
</ul>
IDs y clases
! div#main.container → Elemento con ID y clase.

html
Copiar
Editar
<div id="main" class="container"></div>
! ul.menu>li.menu__item+li#id_item+li.menu__item#id_2 → Combinación de clases e IDs.

html
Copiar
Editar
<ul class="menu">
  <li class="menu__item"></li>
  <li id="id_item"></li>
  <li class="menu__item" id="id_2"></li>
</ul>
Atributos y contenido de texto
! input[type="text"] → Elemento con atributo específico.

html
Copiar
Editar
<input type="text" />
! div[data-attr="test"] → Atributo personalizado.

html
Copiar
Editar
<div data-attr="test"></div>
! p{Lorem ipsum} → Contenido de texto.

html
Copiar
Editar
<p>Lorem ipsum</p>
Elementos comunes
! a:link → Enlace estándar.

html
Copiar
Editar
<a href="http://"></a>
! a:mail → Enlace de correo.

html
Copiar
Editar
<a href="mailto:"></a>
! img → Imagen.

html
Copiar
Editar
<img src="" alt="" />
! form:post → Formulario con método POST.

html
Copiar
Editar
<form action="" method="post"></form>
! input:password → Campo de contraseña.

html
Copiar
Editar
<input type="password" name="" id="" />
carolinehe.github.io
+2
The Linux Code
+2
FreeCodeCamp
+2

link:css → Enlace a hoja de estilos.

html
Copiar
Editar
<link rel="stylesheet" href="style.css" />
meta:vp → Meta viewport para diseño responsivo.

html
Copiar
Editar
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
🎨 Atajos Emmet para CSS
Visualización y posicionamiento
d:b → display: block;

d:f → display: flex;

pos:r → position: relative;

fl:l → float: left;

cl:b → clear: both;

z:10 → z-index: 10;

Margen y relleno
m10 → margin: 10px;

p20 → padding: 20px;

mt5 → margin-top: 5px;

pl15 → padding-left: 15px;

Tamaño y caja
w100p → ` -->