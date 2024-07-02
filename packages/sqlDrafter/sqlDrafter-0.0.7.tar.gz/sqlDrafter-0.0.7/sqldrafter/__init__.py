import base64
import json
import os
from importlib.metadata import version
from sqldrafter import space_manager, generate_schema

try:
    __version__ = version("sqldrafter")
except:
    pass

SUPPORTED_DB_TYPES = [
    "mysql",
    "doris",
    "hive",
    "spark"
]


class sqlDrafter:

    def __init__(
            self,
            api_key: str = "",
            db_type: str = "",
            db_creds: dict = {},
            base64creds: str = "",
            save_json: bool = True,
            base_url: str = "https://www.sqldrafter.com",
            verbose: bool = False,
    ):
        if base64creds != "":
            self.from_base64_creds(base64creds)
            return
        self.home_dir = os.path.expanduser("~")
        self.filepath = os.path.join(self.home_dir, ".sqldrafter", "connection.json")

        if not os.path.exists(self.filepath) and (api_key != "" and db_type != ""):
            self.check_db_creds(db_creds)  # throws error for case 2
            self.api_key = api_key
            self.db_type = db_type
            self.db_creds = db_creds
            self.base_url = base_url
            if save_json:
                self.save_connection_json()
        elif os.path.exists(self.filepath):
            if verbose:
                print(
                    "Connection details found. Reading connection details from file..."
                )
            if api_key == "":
                with open(self.filepath, "r") as f:
                    data = json.load(f)
                    if "api_key" in data and "db_type" in data and "db_creds" in data:
                        self.check_db_creds(data["db_creds"])
                        self.api_key = data["api_key"]
                        self.db_type = data["db_type"]
                        self.db_creds = data["db_creds"]
                        self.base_url = data.get("base_url", "https://www.sqldrafter.com")
                        if verbose:
                            print(f"Connection details read from {self.filepath}.")
                    else:
                        raise KeyError(
                            f"Invalid file at {self.filepath}.\n"
                            "数据错误"
                        )
            else:  # case 5
                if api_key != "":
                    self.api_key = api_key
                if db_type != "":
                    self.db_type = db_type
                self.base_url = base_url
                self.db_creds = db_creds
                self.check_db_creds(self.db_creds)
                if save_json:
                    self.save_connection_json()
        else:  # case 1
            raise ValueError(
                "Connection details not found. Please set up with the CLI or pass in the api_key, db_type, and db_creds parameters."
            )

    def save_connection_json(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, "w") as f:
            json.dump(
                {
                    "api_key": self.api_key,
                    "db_type": self.db_type,
                    "db_creds": self.db_creds,
                    "base_url": self.base_url

                },
                f,
                indent=4,
            )
        print(f"Connection details saved to {self.filepath}.")

    @staticmethod
    def check_db_creds(db_creds: dict):
        if db_creds == {}:
            return
        if "host" not in db_creds:
            raise KeyError("host  必须设置")
        if "port" not in db_creds:
            raise KeyError("端口必须设置")
        if "user" not in db_creds and "username" not in db_creds:
            raise KeyError("用户名必须设置")
        if "password" not in db_creds:
            raise KeyError("密码必须设置")

    def to_base64_creds(self) -> str:
        creds = {
            "api_key": self.api_key,
            "db_type": self.db_type,
            "db_creds": self.db_creds,
        }
        return base64.b64encode(json.dumps(creds).encode("utf-8")).decode("utf-8")

    def from_base64_creds(self, base64_creds: str):
        creds = json.loads(base64.b64decode(base64_creds).decode("utf-8"))
        self.api_key = creds["api_key"]
        self.db_type = creds["db_type"]
        self.db_creds = creds["db_creds"]


for name in dir(space_manager):
    attr = getattr(space_manager, name)
    if callable(attr):
        setattr(sqlDrafter, name, attr)

for name in dir(generate_schema):
    attr = getattr(generate_schema, name)
    if callable(attr):
        setattr(sqlDrafter, name, attr)


class spaceAddTable:

    def __init__(self, database, sqlStr):
        self.database = database
        self.sqlStr = sqlStr

class addMultiTableRequest:

    def __init__(self,spaceId,dbTableSqlDtoList):
        self.spaceId=spaceId
        self.dbTableSqlDtoList = dbTableSqlDtoList