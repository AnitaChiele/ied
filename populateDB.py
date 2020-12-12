import psycopg2


def main():
    insertCustomers()
    insertBooks()
    insertTransactions()


def insertCustomers():
    for data in getCustomers():
        inserToDB(getSqlCustomer(), data)


def getCustomers():
    return [
        (
            'Rayssa Carla Jennifer Cavalcanti',
            'rayssacarlajennifercavalcanti_@maiamaquinas.com.br',
            'Rua da Pitanga 956 Mocinha Magalhães', '6828220039', 'Rio Branco',
            'Acre', '69920036'
        ), (
            'Carlos André Baptista',
            'carlosandrebaptista__carlosandrebaptista@jp.ind.br',
            'Travessa Cassimiro 582 Conjunto Esperança', '6828636830',
            'Rio Branco', 'Acre', '69915116'
        ), (
            'Rayssa Helena Luana dos Santos',
            'rayssahelenaluanadosos_rayssahelenaluanadossa@metalplasma.com.br',
            'Rua Cassimiro de Abreu 241 Colonial', '6828636830',
            'Ariquemes', 'Rondônia', '69915116'
        )
    ]


def inserToDB(sql, data):
    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(sql, data)
    connection.commit()


def getConnection():
    return psycopg2.connect(
        user="postgres",
        password="12345678",
        host="172.17.0.2",
        port="5432",
        database="postgres"
    )


def getSqlCustomer():
    sql = 'INSERT INTO customer '
    sql += '(name, email, address, phone, city, state, zip_code) '
    sql += "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    return sql


def insertBooks():
    for data in getBooks():
        inserToDB(getSqlBook(), data)


def getSqlBook():
    sql = "INSERT INTO book "
    sql += "(publisher_name, author_name, publisher, customer_review) "
    sql += "VALUES (%s, %s, %s, %s)"

    return sql


def getBooks():
    return [
        (
            'Memórias da plantação: episódios de racismo cotidiano',
            'Grada Kilomba', 'Cobogó', '5'
        ),
        (
            'Armas, Germes e Aço - Os Destinos das Sociedades Humanas',
            'Jared Diamond', 'Editora Record', '5'
        ),
        (
            'Sapiens: Uma breve história da humanidade',
            'Yuval Noah Harari', 'L&PM', '5'
        ),
        (
            'Código Limpo: Habilidades Práticas do Agile Software',
            'Robert C. Martin', 'Alta Books', '5'
        ),
        (
            'O rei do inverno - As crônicas de Artur - vol. 1',
            'Bernard Cornwell', 'Record', '5'
        )
    ]


def insertTransactions():
    insertTransactionCustomers()
    insertTransactionBooks()


def getSqlTransactionCustomers():
    sql = "INSERT INTO customer_transaction"
    sql += "(customer_id, status) "
    sql += "VALUES (%s, %s)"

    return sql


def insertTransactionCustomers():
    data_transaction_customer = [
        (1, 'completed'),
        (2, 'in progress'),
        (3, 'cancelled')
    ]

    for data in data_transaction_customer:
        inserToDB(getSqlTransactionCustomers(), data)


def insertTransactionBooks():
    data_transaction_book = [
        (1, [1]),
        (2, [2, 3]),
        (3, [4, 5])
    ]

    for data in data_transaction_book:
        customer_id = data[0]

        for book in data[1]:
            data_insert = (customer_id, book)
            inserToDB(getSqlTransactionBooks(), data_insert)


def getSqlTransactionBooks():
    sql = "INSERT INTO book_transaction"
    sql += "(customer_transaction_id, book_id) "
    sql += "VALUES (%s, %s)"

    return sql


if __name__ == "__main__":
    main()
