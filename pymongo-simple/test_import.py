try:
    import pymongo
    print("Module Import Successful")
except ImportError as error:
    print("Module Import Error")
    print(error)
