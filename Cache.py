from FileManager import FileManager

class Cache:
    def __init__(self,CacheFileName,classCache, keyFieldName, valueField):
        self.CacheFileName=CacheFileName
        self.classCache=classCache
        self.keyFieldName=keyFieldName
        self.valueField=valueField
        self.RS = '\x1E'  # separador de conjuntos
        self.US = '\x1F'  # separador de idiomas
        self.Load()
    def Load(self):
        cacheTextsTranslatedText = FileManager.ReadAllText(self.CacheFileName)
        cacheTextsTranslated = cacheTextsTranslatedText.split(self.RS)
        cacheTextsTranslated = cacheTextsTranslated[:-1]
        cache=[self.classCache(*ct.split(self.US)) for ct in cacheTextsTranslated]
        self.storedCache =cache
    def Save(self, Field, Value):
        FileManager.AppendAllText(self.CacheFileName,f"{Field}{self.US}{Value}{self.RS}")
        self.Load()
    def GetValue(self, key):
        values=[getattr(t,self.valueField) for t in self.storedCache if getattr(t,self.keyFieldName)==key]
        if len(values)>0:
            return values[0]
        else:
            return None