- Curso realizado no FreeCodeCamp.org
- A base de estudos é um banco de dados que contém dados sobre um grupo de estudantes que estudam ciência da computação.
- Há certos comandos que podem vir a ser executados de maneira diferente, uma vez que os comandos abordados estão sendo via Terminal
#### 1. Estabelecer a Conexão com o Banco
Para logar no banco de dados, usamos:
``` sql
psql --username=AAAAAAA --dbname=AAAAAAA 
```
#### 2. Exibindo Bancos existentes
Para exibir os bancos existentes, é utilizado o comando ```\l```



#### 3. Como criar um Banco de Dados
Para criar um Banco de Dados, usamos o comando ```CREATE DATABASE```
Se atente a formatação pois há a inclusão de ```;``` no final da sentença
``` sql
CREATE DATABASE banco_de_dados;
```
#### 4. Verificando se o Banco foi criado
**Volte ao passo 2**

#### 5. Conectando em outro Banco de Dados
Para conectar em outro banco de dados é usado o comando ```\c``` como no exemplo a seguir 
``` sql
\c banco_de_dados
```
#### 6. Criando uma tabela no Banco de Dados
Para criar uma tabela em um banco de dados é usado o comando ```CREATE TABLE``` como no exemplo a seguir
``` sql
CREATE TABLE students();
```
#### 7. Visualizando tabelas criadas
Para visualizar as tabelas criadas, é usado o comando ```\d```

#### 8. Criando uma coluna dentro de uma tabela
Para fins de melhor definição:
```ALTER TABLE``` - é usada para adicionar, excluir ou modificar colunas em uma tabela existente.
```ADD COLUMN``` - é usado para adicionar uma coluna

Para criar uma coluna dentro de uma tabela é usado o comando 
``` sql 
ALTER TABLE nome_tabela ADD COLUMN nome_coluna TYPE CONSTRAINTS
```
Em um exemplo real ficaria da seguinte maneira:
``` sql
ALTER TABLE students ADD COLUMN student_id SERIAL PRIMARY KEY;
```
#### 9. Adicionando uma Coluna com o tipo Varchar
Para adicionar uma coluna com campo do tipo ```VARCHAR``` é usada a mesma estrutura anterior
``` sql
ALTER TABLE nome_tabela ADD COLUMN nome_coluna VARCHAR(50) NOT NULL;
```
#### 10. Adicionando o parâmetro ```NOT NULL```
Utilizando a mesma estrutura anterior, passamos o parâmetro ```NOT NULL``` para indicar que não podemos passar o valor nulo dentro do campo
``` sql
ALTER TABLE nome_tabela ADD COLUMN nome_coluna VARCHAR(50) NOT NULL;
```