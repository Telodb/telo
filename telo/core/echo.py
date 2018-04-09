import hues

def log(msg, logType='l', priority=4, verbosity=1):
    if priority <= verbosity:
        if logType == 'l':
            hues.log(msg)
        if logType == 'e':
            hues.error(msg)
        if logType == 'w':
            heus.warn(msg)
        if logType == 's':
            hues.success(msg)
        if logType == 'i':
            hues.info(msg)
