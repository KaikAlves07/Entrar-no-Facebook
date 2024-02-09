import pyodbc

#configuração de conexão
server = 'DESKTOP-EQDV27O'
database = 'TESTE'
driver = '{ODBC Driver 17 for SQL Server}'
trusted_connection = 'yes'

# conectar com o sql server
try:
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}')
    cursor = conn.cursor()

    # Exemplo de inserção de dados
    id = int(input("insira o id: "))
    eamil = input("insira o email: ")
    senha = input("insira a senha: ")

    cursor.execute("INSERT INTO login (id, eamil, senha) VALUES (?, ?, ?)", (id, eamil, senha))
    conn.commit()  # Para confirmar a operação de inserção

    print("Inserção de dados bem-sucedida!")

except pyodbc.Error as e:
    print(f"Erro ao conectar ao SQL Server: {e}")
    