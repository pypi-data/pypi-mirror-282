

def analysis(row: tuple,partion: list):
    if "字段" in row:
        return
    partion.append(PartitionFieldInfoListDTO(row[0],row[1],row[2],"",""))



class PartitionFieldInfoListDTO:
    def __init__(self,  name,type, remarks,  cnName,samples):
        self.cnName = cnName
        self.name = name
        self.remarks = remarks
        self.type = type
        self.samples = samples

