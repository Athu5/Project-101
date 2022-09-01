import os
import dropbox
from dropbox.files import WriteMode

class TransferData:

     def __init__(self,acces_token):
            self.acces_token = acces_token

     def upload_file(self, file_from, file_to):
          dbx = dropbox.Dropbox(self.acces_token)

          for root, dirs, files in os.walk(file_from):
                
               for filename in files:

                    local_path = os.path.join(root, filename)

                    relative_path = os.path.relpath(local_path, file_from)
                    dropbox_path = os.path.join(file_to, relative_path)

                    with open(local_path , 'rb')as f:
                         dbx.files_upload(f.read(), dropbox_path , mode=WriteMode('overwrite'))



def main():
    access__token  = "sl.BBlKL3RDf6UTN8AIsUczOy124qUw3RJJn_3Vx6TGgxl_2DHpiG9_mlvDWR2QQzWiQ87ZEcgOpkpzzVNDTeMUw8rb7CrB7wjsN3aNMUtAGcLKVh5E6jC0LkZC3NVv3tJjzGZIcnKO1Rcy"
    transferData = TransferData(access__token)

    file_from = str(input("Enter the file path to transfer :- "))
    file_to = input("enter the full path to upload to dropbox:- ")

    
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
