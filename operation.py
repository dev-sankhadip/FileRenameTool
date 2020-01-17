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
        if os.path.isdir(path):
            answers = prompt(questions, style=custom_style_2)
            fileTypeId =  answers['type'].split('.')
            files = os.listdir(path)
            if fileTypeId[0]=='1':
                for f in files:
                    print(f)
            elif fileTypeId[0]=='2':
                allFile=[]
                for f in files:
                    allFile.append(path+'/'+f)
                allFiles = sorted(allFile, key=os.path.getctime)
                for file in allFiles:
                    fileArray = file.split('/')
                    fileName = fileArray[len(fileArray)-1]
                    print(fileName)
        else:
            print("Invalid directory path")