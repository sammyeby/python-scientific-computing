
def sqlFromFile(sqlFilePath: str):
    if not sqlFilePath or len(sqlFilePath) < 1:
        raise Exception('Please provide an sql file path')
    sql = ''
    try:
        file = open(sqlFilePath)
        sql = file.read()
    except:
        raise Exception("Cannot read file. Make sure it\'s the correct filepath")
    return sql