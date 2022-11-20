def integrity_error_print(index, error):
    print(f"Error index/line: {index}")
    print(f"Error reason: \"{error}\"")
    print("Quitting Program")
    quit()


def unicode_error_print(index, error):
    print(f"Error index/line: {index}")
    print(f"Most likely data contains unknown character")
    print(f"Error reason: \"{error}\"")
    print("Quitting Program")
    quit()


def operational_error_print(tableName, error):
    print(f"Could not remove \"{tableName}\" for reason \"{error}\"")
    print(error)


def file_not_found_error_print(filename, error):
    print(f"Couldn't find file from path \"{filename}\"")
    print("Quitting program")
    quit()
