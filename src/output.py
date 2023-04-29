import datetime

"""
todo: Add header to output. Default header is the main URL and time it was scanned
todo: add ability to customize output file name
"""

class Writer:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_header(self, url):
        time_data = datetime.datetime.now()
        date = time_data.strftime("%x")
        time = time_data.strftime("%X")
        f = open(self.file_name, "a")
        f.write(f"================= {url} [{time} {date}] =================\n")
        f.close()

    def write_log(self, text):
        f = open(self.file_name, "a")
        f.write(text + "\n")
        f.close()

Writer().write_header("byui.edu")