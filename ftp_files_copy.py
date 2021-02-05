import fnmatch
from ftplib import FTP
from time import sleep


class FilesCopy:
    def __init__(self):
        self.__ftp = ""
        self.__login = ""
        self.__pass = ""
        self.__folders = (
            r"/SIB_PD/LogFiles/RTU1",
            r"/SIB/LogFiles/RTU2",
        )
        self.__traces = (
            r"/SIB_PD/TraceFiles/RTU1",
            r"/SIB/TraceFiles/RTU2",
        )
        self.__serv_dir = r"D:/Regions/Logfiles_Imported"

    def download(self):
        with FTP(self.__ftp, self.__login, self.__pass) as con:
            try:
                for folder in self.__folders:
                    con.cwd(folder)
                    for logfile in con.nlst():
                        if fnmatch.fnmatch(logfile, "*.trp"):
                            with open(
                                f"{self.__serv_dir}{folder}/{logfile}", "wb"
                            ) as f:
                                con.retrbinary("RETR " + logfile, f.write)
                                con.delete(logfile)
                for folder in self.__traces:
                    con.cwd(folder)
                    for tracefile in con.nlst():
                        if fnmatch.fnmatch(tracefile, "*.7z"):
                            with open(
                                f"{self.__serv_dir}{folder}/{tracefile}", "wb"
                            ) as f:
                                con.retrbinary("RETR " + tracefile, f.write)
                                con.delete(tracefile)
            except:
                pass


if __name__ == "__main__":
    sleep(10)
    ftp = FilesCopy()
    while True:
        ftp.download()
        sleep(2)
