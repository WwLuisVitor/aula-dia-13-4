opcao=2
filmesdisponiveis=['f1','f2','f3','f4','f5']
filmesalugados=[]

while opcao!=5:
  print()
  print('bem vindo a locadora')
  print('1) listar filmes disponiveis')
  print('2) listar filmes alugados')
  print('3) alugar filme')
  print('4) devolver filme')
  print('5) sair')
  print()
  opcao=int(input('digite sua opçao '))
  if opcao==1:
    print('lista dos filmes disponiveis')
    for filme in filmesdisponiveis:
      print(filme)
  elif opcao==2:
    print('lista dos filmes alugados')
    for filme in filmesalugados:
      print(filme)
  elif opcao==3:
    print('lista de filmes disponiveis para alugar')
    quantidadeDeFilmes = len(filmesdisponiveis)
    for i in range(quantidadeDeFilmes):
      print(i+1,')',filmesdisponiveis[i])
    filmeescolhido=int(input('qual filme voce quer alugar? '))
    filmesalugados.append(filmesdisponiveis[filmeescolhido-1])
    filmesdisponiveis.remove(filmesdisponiveis[filmeescolhido-1])
  elif opcao==4:
    print('esses sao os filmes alugados no momento')
    quantidadeFilmesAlugados= len(filmesalugados)
    for i in range(quantidadeFilmesAlugados):
      print(i+1,')',filmesalugados[i])
    devolverfilme=int(input('qual filme voce deseja devolver? '))
    filmesdisponiveis.append(filmesalugados[devolverfilme-1])
    filmesalugados.remove(filmesalugados[devolverfilme-1])
    filmesdisponiveis.sort()
    filmesalugados.sort
  else:
    print('saindo...')