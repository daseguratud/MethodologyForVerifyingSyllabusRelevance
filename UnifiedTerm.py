class UnifiedTerm:
    def __init__(self,term, syllabusFrecuency, referenceFrecuency):
        self.term = term
        self.syllabusFrecuency = syllabusFrecuency
        self.referenceFrecuency = referenceFrecuency
    def __str__(self):
        return f"{self.term};{self.syllabusFrecuency};{self.referenceFrecuency}"