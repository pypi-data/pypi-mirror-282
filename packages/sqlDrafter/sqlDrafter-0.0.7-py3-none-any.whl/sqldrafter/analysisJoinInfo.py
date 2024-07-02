

def analysis(row: tuple,joinInfo: list):
    if "源字段" in row :
        return
    joinInfo.append(TableItemJoinInfoDTO(row[0].split(","),row[1],row[2],row[3].split(",")))


class TableItemJoinInfoDTO:
    def __init__(self, fields, refDb, refTable, refFields):
        self.fields = fields
        self.refDb = refDb
        self.refFields = refFields
        self.refTable = refTable
