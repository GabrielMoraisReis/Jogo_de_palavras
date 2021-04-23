from unidecode import unidecode #Pode ser necessário o download dessa biblioteca
dicionario_palavras_original = ["Abacaxi", "Manada", "mandar", "porta", "mesa", "Dado", "Mangas", "Já", "coisas",
"radiografia", "matemática", "Drogas", "prédios", "implementação", "computador", "balão",
"Xícara", "Tédio", "faixa", "Livro", "deixar", "superior", "Profissão", "Reunião", "Prédios",
"Montanha", "Botânica", "Banheiro", "Caixas", "Xingamento", "Infestação", "Cupim",
"Premiada", "empanada", "Ratos", "Ruído", "Antecedente", "Empresa", "Emissário", "Folga",
"Fratura", "Goiaba", "Gratuito", "Hídrico", "Homem", "Jantar", "Jogos", "Montagem",
"Manual", "Nuvem", "Neve", "Operação", "Ontem", "Pato", "Pé", "viagem", "Queijo", "Quarto",
"Quintal", "Solto", "rota", "Selva", "Tatuagem", "Tigre", "Uva", "Último", "Vitupério",
"Voltagem", "Zangado", "Zombaria", "Dor"]

dicionario_palavras_atualizado = list(map(unidecode, map(str.lower, dicionario_palavras_original)))
print(dicionario_palavras_atualizado)