"""
Interpretador do Python

python modulo.py (executa o módulo)
python -u (unbuffered = joga direto na tela)
python -m mod (lib mod como script | ex.: python -m venv .venv)
python -c 'cmd' (comando do python | ex.: python -c 'print("Oi")')
python -i mod.py (carregar módulo no modo interativo)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""

# ; PODE funcionar como quebra de linha
print(1+1);print(2+2)

# Se escrever o código abaixo, nunca mais verá nenhuma exceção:
try:
    print('hahaha')
except:
    ...