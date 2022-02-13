import dropbox
class tranfer:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def upload_file(self, fileFrom, fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        with open(fileFrom,"rb")as f:
            dbx.files_upload(f.read(),fileTo)
def main():
    accessToken="sl.BBiyHrcAPkggWcFg90t4nvYuM7jls0WHu04WUr_LQVqIWQ8coJtb4Bf9ziCKLsf9dRaly6kM7y0EBxNbn7dQEn51IGUdJp0YpQa3X8khTw2H_ngObNkGbmHq9owX-B2rxzSPIGWhsdiR"
    transferdata=tranfer(accessToken)
    fileFrom="file.txt"
    fileTo="/notafolder/file.txt"
    transferdata.upload_file(fileFrom,fileTo)
main()
         

        