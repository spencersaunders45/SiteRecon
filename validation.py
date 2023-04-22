import requests
from display import IO

class Validation:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def __init__(self):
        pass

    def check_site(self, site):
        # adds https to url if not found
        if "https://" not in site or "http://" not in site:
            site = "https://" + site
        # makes site request
        r = requests.get(site, headers=self.headers)
        # checks if the request is a 500 error
        if r.status_code >= 500:
            IO().status_report_bad(r.status_code, site)
            exit()

    def check_c_flag(self, max, min):
        try:
            int(max)
            int(min)
        except:
            IO().invalid_flag()
            exit()

    def user_command(self, command):
        command_list = command.split(" ")
        self.check_site(command_list[0])
        for i in range(1,len(command_list)):
            flag = command_list[i]
            if '-' in flag:
                match flag:
                    case '-C':
                        try:
                            int(command_list[i+1])
                            int(command_list[i+2])
                        except:
                            IO().invalid_c_flag()
                            exit()
                    case '-fn':
                        unacceptable_symbols = {'.', '"', '>', '<', '\\', '/', ':', '|', '?', '*'}
                        if unacceptable_symbols in command_list[i+1]:
                            IO().invalid_symbol()
                            exit()
                        unacceptable_names = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
                        if unacceptable_names in command_list[i+1]:
                            IO().invalid_filename(command_list[i])
                            exit()
                    case '-Dag':
                        flag_options = {'A', 'M', 'P', 'C'}
                        if flag_options not in command_list[i+1]:
                            IO().invalid_aggression_parameter(command_list[i+1])
                            exit()
                        if command_list[i+1] == 'C':
                            try:
                                int(command_list[i+2])
                                int(command_list[i+3])
                            except:
                                IO().invalid_c_flag()
                                exit()
                    case '-Dfn':
                        pass