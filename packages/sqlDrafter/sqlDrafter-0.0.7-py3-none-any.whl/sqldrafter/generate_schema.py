import sqldrafter

from pyhive import hive


def generate_mysql_schema(
        self,
        tables: list,
) -> list:
    try:
        import mysql.connector
    except:
        raise Exception("mysql-connector not installed.")
    result_list = []
    conn = mysql.connector.connect(**self.db_creds)
    cur = conn.cursor()
    print("从数据库中获取schema")
    for table_name in tables:
        db_name = table_name.split(".")[0]
        table = table_name.split(".")[1]
        cur.execute("use " + db_name + ";")
        cur.execute(" show create table " + table)
        result = cur.fetchall()
        for item in result:
            str = sqldrafter.spaceAddTable(db_name, item[1])
            result_list.append(str)
    conn.close()
    return result_list


def generate_hive_schema(
        self,
        tables: list,
) -> list:
    result_list = []
    db_creds = {}
    for key in self.db_creds:
        if self.db_creds[key] == '':
            pass
        else:
            db_creds[key] = self.db_creds[key]
    conn = hive.Connection(**db_creds)
    cur = conn.cursor()
    print("从数据库中获取schema")
    for table_name in tables:
        db_name = table_name.split(".")[0]
        cur.execute(" show create table " + table_name)
        result = cur.fetchall()
        sqlStr = "";
        for item in result:
            sqlStr = sqlStr + "\n" + " ".join(item)
        str = sqldrafter.spaceAddTable(db_name, sqlStr)
        result_list.append(str)
    conn.close()
    return result_list


def generate_db_schema(
        self,
        tables: list,
) -> str:
    if self.db_type == "mysql" or self.db_type == "doris":
        return self.generate_mysql_schema(
            tables,
        )
    elif self.db_type == "hive" or self.db_type == 'spark':
        return self.generate_hive_schema(
            tables,
        )
    else:
        raise ValueError(
            f""
        )
