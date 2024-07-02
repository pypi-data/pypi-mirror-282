

def analysis(row: tuple,fields:list) :
    if "是否主键" in row :
        pass
    else:
        fields.append(TableItemFieldsDTO(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))


class TableItemFieldsDTO:
    def __init__(self, primaryKey, name,  type, cnName, samples, remarks, used):
        self.cnName = cnName
        self.name = name
        self.primaryKey = primaryKey
        self.remarks = remarks
        self.type = type
        self.samples = samples
        self.used = used
