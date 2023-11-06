===**Continuação do [[JS Cod. 1.3 - Aplicando JS via HTML]]**===
## Explicação
Há maneiras de aplicar configurações de estilo na página, nas quais podem alterar aspectos visuais
## Código
Códigos de Terminal 
```js
// Código 1
document.body.style.backgroundColor = "lightblue";
// Código 2
document.body.style.color = "white";
// Código 3
let p = document.createElement("P");
// Código 4
let t = document.createTextNode("Paragraph text.");
// Código 5
p.appendChild(t);
// Código 6
document.body.appendChild(p);
```
## Retorno
![[Pasted image 20231010163705 1.png]]
![[Pasted image 20231010163738 1.png]]
![[Pasted image 20231011103557 1.png]]






