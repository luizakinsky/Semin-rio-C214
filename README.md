# Seminário-C214

## PyUnit

### O que é?

PyUnit é um framework de teste unitário em Python. Ele faz parte da biblioteca padrão do Python e é inspirado no JUnit, um framework de teste para Java. O objetivo do PyUnit é facilitar a criação, organização e execução de testes unitários para garantir que pequenas partes individuais do código (as "unidades") funcionem como esperado.

### Instalação

O unittest, o módulo que implementa o PyUnit, já vem incluído na biblioteca padrão do Python. Portanto, não é necessária a instalação de nada adicional para começar a usá-lo em aplicações Python.

### Integração com IDEs

O PyUnit tem integração com diversas IDEs como PyCharm, Eclipse com PyDev, Visual Studio Code, IntelliJ IDEA e ATOM.  
Alguns exemplos de integração:

#### Visual Studio Code (VS Code)

- **Extensão Python:** A extensão Python para VS Code detecta testes unittest automaticamente.
- **Test Explorer:** A extensão adiciona uma interface de usuário para explorar, executar e depurar testes.
- **Configuração:** É possível configurar o descobrimento de testes no arquivo de configuração .vscode/settings.json:

### Passo a passo - criação de um projeto (Exemplo: calculadora)

#### Passo 1: Configuração do ambiente de desenvolvimento

**1. Diretório de projeto**  
Criar uma pasta onde o projeto será armazenado  
**2. Ambiente Virtual**  
Criar um ambiente virtual para a execução do projeto  
> python -m venv venv

#### Passo 2: Estruturação do projeto

**Estrutura de diretórios**
Estruturar as pastas e arquivos da seguinte maneira:
> meu_projeto/
> 
> ├── src/
> 
> │   └── calculadora.py
> 
> └── tests/
> 
> │   └── test_calculadora.py  

#### Passo 3: Implementação da Função

No arquivo src/calculadora.py, escrever a função abaixo:
> def soma(a, b):
>     return a + b

#### Passo 4: Implementação dos testes

No arquivo tests/test_calculadora.py, escrever os testes abaixo:
> import unittest
> from src.calculadora import soma
>
> class TestCalculadora(unittest.TestCase):
>
>     def test_soma_positivos(self):
>         self.assertEqual(soma(2, 3), 5)
>
>     def test_soma_negativos(self):
>         self.assertEqual(soma(-1, -1), -2)
>
>     def test_soma_zero(self):
>         self.assertEqual(soma(0, 0), 0)
>
> if __name__ == '__main__':
>     unittest.main()

#### Passo 5: Execução os testes

No terminal, entrar no diretório do projeto e rodar o seguinte comando:
> python -m unittest discover -s tests
