class ui:
    def __init__(self):
        pass
    @staticmethod
    def printTest():
        print("\033[30m║\033[31m║\033[32m║\033[33m║\033[34m║\033[35m║\033[36m║\033[37m║")
    @staticmethod
    def printError(message):
        print(f"\033[31m{message}\033[0m")
    @staticmethod
    def printMainMessage(message):
        print(f"\033[36m{message}\033[0m")
    @staticmethod
    def printStageStart(stageNumber):
        print(f"\033[32mEtapa {stageNumber} iniciada...\033[0m")
    @staticmethod
    def printStageFinish(stageNumber):
        print(f"\033[32mEtapa {stageNumber} terminada\033[0m")
    @staticmethod
    def printStageMessage(message):
        print(f"\033[33m{message}\033[0m")
    @staticmethod
    def printStageMessageSubProcess(message):
        print(f"\033[34m{message}\033[0m")
    @staticmethod
    def printInternalProcess(message):
        print(f"\033[35m{message}\033[0m")
