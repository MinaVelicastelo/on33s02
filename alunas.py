nome = input('Digite o nome da aluna: ');
idade = int (input('Digite a idade da aluna: '));
altura = float (input('Digite a altura da aluna: '));
hobbies = input('Digite os hobbies da aluna separados por vírgula: ');
hobbies1 = hobbies.split(',');
endereco_rua = input('Digite o nome da rua da aluna:');
endereco_numero = int(input('Digite o nº da casa da aluna:'));
endereco_cidade = input('Digite a cidade da aluna:');
endereco = (endereco_rua, endereco_numero, endereco_cidade);
email = input('Digite o email da aluna: ');
telefone = input('Digite o telefone da aluna: ');
contato = {'E-mail': email, 'Telefone': telefone};

print('\nOlá, seguem informações sobre a aluna: ')
print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('Hobbies: ', hobbies)
print('Endereço: ', endereco)
print('Contato: ', contato)