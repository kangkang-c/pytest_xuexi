import yaml
import os

def readyml(filePath):

    f = open(filePath, "r", encoding="utf-8")
    y = f.read()
    data = yaml.load(y)
    print("读取yaml转字典:%s"%data)
    return data

if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(os.getcwd()))
    #print(path)
    file_name = "testdata.yml"
    file = os.path.join(path,'case',file_name)
    print(file)
    a = readyml(file)
    #print(a['test_add_param_demo'])