'''
File Reading
'''
import json
class FileOp:
    def __init__(self):
        #! note that double backslashes are used since they are also used with escape sequences 
        self.folder_path = 'D://python_learn//chapter_10_files'
        ## OR
        # file_path = 'D:\python_learn\chapter_10_files\pi_digits.txt'
        self.default_file_path = self.folder_path + '//pi_digits.txt'
        self.json_path = self.folder_path + "//numbers.json"
        self.pi_string =''

    def print_file_content(self, file_path = ''):
        if not file_path:
            print("file path not mentioned; choosing the default path")
            file_path = self.default_file_path 
        try:
            with open(file_path) as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            print(f"Sorry, the file {file_path} does not exist.")
            return
        print(contents)

    def string_from_file(self, filename):
        with open(filename) as file_object:
            lines = file_object.readlines()
        self.pi_string = ''
        for line in lines:
            self.pi_string += line.rstrip()
        return self.pi_string
    
    def find_bday_in_pi(self):
        birthday = input("Enter your birthday, in the form mmddyy: ")
        if self.pi_string != '' and birthday in self.pi_string:
            print("Your birthday appears in the first 30 digits of pi!")
        else:
            print("Your birthday does not appear in the first 30 digits of pi.")

    def write_to_file(self, msg):
        filename = 'programming.txt'
        with open(filename, 'w') as file_object:
            file_object.write(msg)
    
    def list_to_json_file(self, numbers):
        with open(self.json_path, 'w') as f:
            json.dump(numbers, f)
    
if __name__ == "__main__":
    f = FileOp()
    # printing default file content
    f.print_file_content()
    # printing string from file
    print(f.string_from_file(filename='pi_digits.txt'))
    # finding bday in pi
    f.find_bday_in_pi()

    f.write_to_file("hola!")
    f.list_to_json_file([1,2,3])

    

