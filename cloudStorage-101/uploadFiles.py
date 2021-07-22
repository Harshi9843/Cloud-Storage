import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accsess_token):
        self.access_token = accsess_token
    
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                local_path = name
            

        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A1F1kcb8_sYTIxc1XSVGj3MRHseenPY1dTGDrL3z97U9JkFtSXxey4KOKh1uDfpRFcXO8qWA93egiSRFlDzQH-NffCn_KF5Z3jBBHYgNkfY0m-ZU6XDQTnMps-A9mcurtbwreh4'
    transferData = TransferData(access_token)
    
    file_from = input("Enter the folder path you want to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ") 

    transferData.upload_files(file_from, file_to)
    print("Files have been moved")

main()
