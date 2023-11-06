## Let e Const
No ES6, temos algumas novas palavras-chave variáveis ​​que essencialmente substituíram a palavra-chave var. Antes do ES6, o JavaScript tinha apenas escopo funcional e global. Com a adição de let e const, agora temos escopo de bloco.

```js
let x = 5;

function blockExample() {
	let x = 2 //this is function scope;
	if(x >= 3) {
		let x = 10; // this is block scope
		console.log(x, "inside if block");''
	} else {
		let x = 1;
		console.log(x, "inside else block")
	}
	console.log(x, "inside function");
}

blockExample();
console.log(x, "global example");
```

A palavra-chave let pode ser reatribuída conforme necessário. Quando usada no mesmo escopo, uma redeclaração da mesma variável gerará um erro de sintaxe.

Esta é uma melhoria na palavra-chave var, onde você pode declarar novamente variáveis ​​com outro valor. Isso se mostrou problemático quando tínhamos o mesmo nome de variável com valores diferentes que produziam bugs não intencionais.

```js
// pre-ES6:
var x = 5;
var x = 120; //produces no errors

// ES6: 
let x = 5;
let x = 120; // produces a syntax error
```

A palavra-chave const é útil quando você tem uma variável que não tem intenção de reatribuir. Irá gerar um erro se você tentar reatribuir sua variável const para outro valor.
## Promises
As promessas são uma maneira de lidar melhor com a programação JavaScript assíncrona. Antes, as chamadas assíncronas eram feitas usando funções de retorno de chamada, o que poderia tornar o código complicado e confuso muito rapidamente.

```js
console.log("before promise")
let promise = new Promise((resolve, reject) => {
	let resolvedFlag = false;
//this is just a flag so we can intentionally throw the response to test logic
	console.log("this is eventually going to be an API call");
	resolvedFlag = true; //flip resolved to true once all console logs are done

	if(resolvedFlag) { //if resolved is true invoke the resolve function
		resolve("Promise resolved THIS IS THE RESPONSE");
	} else { // else invoke the reject function with a new Error object with message
		reject(new Error("Promise failed"));
		console.log("after promise");
	}
});

promise.then(resp => {
	console.log(resp); //promise response
})
```

==**Continuação - [[JS 1.3.7 - Mudanças no ES6 - Rest-Spread e Template Literals]]==**