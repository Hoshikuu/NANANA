from configparser import ConfigParser

def config(filename="C:/Users/Cristian/Documents/py/DATABASE/Database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {} is not found in the {} file".format(section, filename))
    return db