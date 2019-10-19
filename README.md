# Minicurso Introdução ao Git e GitHub

## Instrutores: Diego Pessoa e Diogo Moreira
## Monitor: Antônio Ricart

### Parte 1 - Git

#### Introdução
* Problema: controle de versão - motivações
*  Sistemas de controle de versão (centralizado VS distribuído)
* Origem e características
    * Linus Torvalds - 2005 (abril-junho)

#### Comandos básicos
* Configuração de nome e e-mail (`git config --global user.email <email>`)
* Criar um repositório (`git init`)
* Adicionar arquivos à área de staging (`git add arquivo`)
* Realizar commit (`git commit`)
* Convenções para mensagens de commit
* Desfazer commit (`git reset`)
* Visualizar histórico do que foi feito commit (`git log`)
* Mostrar o que foi modificado na versão atual (`git diff <arquivo>`)
* Mostrar o que foi alterado em um commit (`git show <hash>`)

#### Branches
* Criar uma branch (`git branch <branch>`)
* Convenções para nomes de branches
* Passar a trabalhar em uma branch (`git checkout branch`)
* Remover uma branch (`git branch -d <branch>`)
* Comparar branches (`git diff <branch1> <branch2>`)
* Mesclar branch atual com outra (`git merge <target>`) 
* Mesclar mantendo ordem do histórico de commits (`git rebase <target>`) 


## Parte 2 - Github (Repositórios remotos)
* Visão geral do Github
* Criar conta
* Criar repositório
* Visão geral de um projeto: issues, contributors, wiki, releases, etc
* Utilizar Github Student Pack
* Integrando o repositório local com o repositório remoto
* Clonar de repositório (`git clone <url>`)
* Adicionar um remoto ao projeto (`git add remote <url>`)
* Enviar modificações para um repositório remoto (`git push`)
* Puxar modificações de um repositório remoto (`git pull`)
* Contribuindo com projetos de terceiros no Github
* Criar um fork de um repositório existente
* Modificar o fork localmente e submeter para o  repositório remoto
* Fazer um Pull Request

### Ferramentas Visuais para utilizar o Git
* Github Desktop
* SourceTree
