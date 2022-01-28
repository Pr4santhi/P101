import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)  

def main():
    access_token="sl.BAUll5acBGFcdeuz52ZmpclZPwtr_1v_3VY0eKd6SNL01E9ugapIZ5bVDNo1_LS0YIEqbUgk1OCOCnaE38mrQvQAVoCj-ZdT17j36A0lkL6H3KqM-BhQ-u72UvDcW_-Rqds4uGY"
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer:")
    file_to = input("enter the file path to upload to dropbox")
    transferData.upload_files(file_from,file_to)
    print("file has been moved")   

main()    
        
         