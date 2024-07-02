

def analysis(row: tuple,uniq:list) :
    uniq.append(TableItemUniqueKeyInfoListDTO(row[0].split(",")))


class TableItemUniqueKeyInfoListDTO:
    def __init__(self, fields):
        self.fields = fields
