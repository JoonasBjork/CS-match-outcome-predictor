def integrityErrorPrint(index, line, error):
    print(f"Error index/line: {index}")
    print(f"Error line data: {line}")
    print(f"Error reason: \"{error}\"")
    print("Quitting Program")
    quit()


def unicodeErrorPrint(index, error):
    print(f"Error index/line: {index}")
    print(f"Most likely data contains unknown character")
    print(f"Error reason: \"{error}\"")
    print("Quitting Program")
    quit()


def operationalErrorPrint(tableName, error):
    print(f"Could not remove \"{tableName}\" for reason \"{error}\"")
    print(error)


def fileNotFoundErrorPrint(filename, error):
    print(f"Couldn't find file from path \"{filename}\"")
    print("Quitting program")
    quit()
