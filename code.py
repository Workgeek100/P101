import dropbox
class Transfer_data:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'sl.Aoi7_oggnrgFnA00hF-ynfHVLs6vDt3XrlhBzZ2payIVg57NfrNU07SAeBbd0R9RQ5nInjDrwtEzz4BcA-XfP5T6Ujm0_aY34Vr8kYrW4rmjELVdYHkogrIMlsfVyY28nByiYg8'
    transfer_data = Transfer_data(access_token)
    file_from = 'abcd.txt'
    file_to = '/test_dropbox/abcd.txt'
    transfer_data.upload_file(file_from,file_to)
    print("File has been uploaded successfully")
main()