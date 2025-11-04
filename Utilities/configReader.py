from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/lekhraj.p/PycharmProjects/Student-Android-App/Testcases/testdata.ini")
    return config.get(section, key)
