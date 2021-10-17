class FileHandler:
    def __init__(self):
        pass


    def read_file(self, file_path):
        try:
            file_obj = open(file_path, "r")
            file_content = file_obj.readline()
            file_obj.close()
            return file_content
        except Exception as e:
            print(str(e))
            raise Exception(str(e))