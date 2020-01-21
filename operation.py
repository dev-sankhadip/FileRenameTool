import os
from PyInquirer import Token, prompt, Separator
from examples import custom_style_2


class Operation:

    def read(self,path):
        files = os.listdir(path)
        for f in files:
            print(f)
    
    def listType(self, path):
        # questions to user
        questions = [
            {
                'type': 'list',
                'name': 'type',
                'message': 'How do you want to list files?',
                'choices': ['1. Alphabetical Order', '2. File creation time', '3. File Size'],
                'filter': lambda val: val.lower()
            },
        ]
        # path should be directory
        if os.path.isdir(path):
            answers = prompt(questions, style=custom_style_2)
            fileTypeId =  answers['type'].split('.')

            # get all files inside directory
            files = os.listdir(path)

            # add file to array with original base path
            allFile=[]
            for f in files:
                allFile.append(path+'/'+f)


            # if choice is in alphabetical order
            if fileTypeId[0]=='1':
                for f in files:
                    print(f)

            # if choice is in file creation time
            elif fileTypeId[0]=='2':
                # allFile=[]
                # for f in files:
                #     allFile.append(path+'/'+f)
                allFiles = sorted(allFile, key=os.path.getctime)
                for file in allFiles:
                    # fileArray = file.split('/')
                    # fileName = fileArray[len(fileArray)-1]
                    # print(fileName)
                    print(self.getFileName(file))

            # if choice is in file size
            elif fileTypeId[0]=='3':
                allFiles = sorted(allFile, key=os.path.getsize)
                for file in allFiles:
                    print(self.getFileName(file))
        
        # if path is not directory
        else:
            print("Invalid directory path")

    def getFileName(self, file):
        fileArray = file.split('/')
        fileName = fileArray[len(fileArray)-1]
        return fileName