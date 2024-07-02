import requests
import json


def create_space(
        self,
        title: str,
        desc: str,
        dbQueryType:str
) -> int:
    try:
        headers = {"api_key": self.api_key}
        res = requests.post(f"{self.base_url}/api/space/manage/add",
                            json={
                                "name": title,
                                "busiDesc": desc,
                                "engineType": self.db_type,
                                "dbQueryType": dbQueryType,
                                "sqlStr": "1"
                            },
                            headers=headers
                            )
        resp = res.json()
        if (resp["success"]):
            return resp["data"]["id"]
        else:
            print("创建失败！")
    except Exception as e:
        print("发生了一个错误:", str(e))
        return 0

def query(
        self,
        spaceID: int,
        question: str
) -> int:
    try:
        headers = {"api_key": self.api_key}
        res = requests.post(f"{self.base_url}/api/query",
                            json={
                                "spaceID": spaceID,
                                "question": question
                            },
                            headers=headers
                            )
        resp = res.json()
        if (resp["success"]):
            return resp["data"]
        else:
            print(resp["msg"])
    except Exception as e:
        print("发生了一个错误:", str(e))
        return 0

def add_table(self,
              requestBody: json) -> bool:
    try:
        headers = {"api_key": self.api_key}
        res = requests.post(f"{self.base_url}/api/space/manage/addMultiTable",
                            json=json.loads(requestBody),
                            headers=headers
                            )

        resp = res.json()
        return resp["success"]
    except Exception as e:
        print("发生了一个错误:", str(e))
        return False


def get_detail(self,
               space_id: int) -> str:
    try:
        headers = {"api_key": self.api_key}
        res = requests.get(f"{self.base_url}/api/space/manage/detail",
                           params={
                               "id": space_id
                           },
                           headers=headers
                           )
        resp = res.json()
        return resp
    except Exception as e:
        print("发生了一个错误:", str(e))
        return False


def edit_space(self,
               requestBody: json) -> str:
    try:
        headers = {"api_key": self.api_key}
        res = requests.post(f"{self.base_url}/api/space/manage/edit",
                           json=json.loads(requestBody),
                           headers=headers
                           )
        resp = res.json()

        if resp["success"]:
            print("更新成功")
        else:
            print(resp["msg"])
        return resp
    except Exception as e:
        print("发生了一个错误:", str(e))
        return False
