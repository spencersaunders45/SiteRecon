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
                        pass
                    case '-fn':
                        pass
                    case '-Dag':
                        pass
                    case '-Dfn':
                        pass