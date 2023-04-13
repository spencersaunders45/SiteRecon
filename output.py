"""
todo: Add header to output. Default header is the main URL and time it was scanned
"""

class Writer:
    def __init__(self):
        pass

    def write_header(self, url, time):
        f = open("siterecon_output.txt", "a")
        f.write(f"================= {url} [{time}] =================\n")
        f.close()

    def 