import json


class PyJson():
    def __init__(self, encode: str) -> None:
        self.encode = encode

    def readjson(self, filename: str, mode: str = "r") -> dict[str]:
        with open(filename, mode=mode, encoding=self.encode) as fp:
            data = json.load(fp)
        return data

    def writejson(self, filename: str, data: dict ,mode: str = "w"):
        with open(filename, mode=mode, encoding=self.encode) as fp:
            data = json.dump(dados_json,fp)
        return data
    
    def appenddata(self, filename: str, data: dict):
        with open(filename, encoding=self.encode,mode="a+") as fp:
            data = json.dump(dados_json,fp)
        return data
    


def id_in_dict(id: str, dict: dict ) -> bool:
    ids_livros = tuple(dict.keys())
    if id in ids_livros:
        return True
    else:
        return False

if __name__ == "__main__":
    pyjson = PyJson("utf-8")
    dados_json = pyjson.readjson("models/base.json", "r")
    # pyjson.writejson("teste.json",dados_json)  
    id = "5"
    print(id_in_dict(id,dados_json))
    
      