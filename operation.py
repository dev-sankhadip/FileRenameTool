import os
from PyInquirer import Token, prompt, Separator
from examples import custom_style_2


class Operation:

    def read(self,path):
        files = os.listdir(path)
        for f in files:
            print(f)
    
    def listType(self, path):
        questions = [
            {
                'type': 'list',
                'name': 'type',
                'message': 'How do you want to list files?',
                'choices': ['1. Alphabetical Order', '2. File creation time', '3. File Size'],
                'filter': lambda val: val.lower()
            },
        ]
        answers = prompt(questions, style=custom_style_2)
        fileType =  answers['type'].split('.')
        print(fileType)
        if os.path.isdir(path):
            files = os.listdir(path)
            print(files)
        else:
            print("Invalid directory path")