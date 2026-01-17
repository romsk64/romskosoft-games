# Romsk Python Log Library
# Библиотека для создания простых логов, так как мне лень разбираться в logging
# Распространяется по лицензии MIT
# Русская документация по пути ../docs/romplog/ru-doc.md

class Logger():
    def __init__(self, fpath, fformat):
        self.fpath = fpath
        self.format = fformat
        self.startLog()
    def startLog(self):
        pass
    def endLog(self):
        pass
    def pauseLog(self):
        pass
    def whatLogging(self, func):
        def ret():
            funName = func.__name__
            print(funName)
            return funName
        return ret
    def logConsole(self, level): # логирование только в консоль
        pass
    def logFile(self, level):
        pass
    def log(self, level):
        # levels:
        # 1 - debug (только в файле, не в консоли)
        # 2 - info
        # 3 - warning
        # 4 - error
        # 5 - critical error
        # от 6 до бесконечности - пользовательские приколы
        pass