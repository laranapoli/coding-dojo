# Criando Repositório

## GitHub CLI
### Instalação
```bash
sudo apt install gh
```

### Autenticação
```bash
gh auth login
```

### Criação do repositório
- Privado:
```bash
gh repo create <nome-do-repo> --private --description "Descrição"
```

- Público:
```bash
gh repo create <nome-do-repo> --public --description "Descrição"
```

### Vincular com local
#### Inicializar git
```bash
cd nome-do-repo
git init
```

#### Adicionar repositório remoto
```bash
git remote add origin <URL>
```

#### Commit inicial
```bash
echo "# Nome do repo" >> README.md
git add .
git commit -m "Inicializando repositório"
git branch -M main
git push -u origin main
```

- `git push origin main`: Envia o branch main para o remoto origin
- `git push -u origin main`: Além de enviar, vincula o branch local ao remoto