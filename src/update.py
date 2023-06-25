import json


class Settings:

    def __init__(self,
                file_path, 
                search_count,
                aggression,
                aggressive,
                moderate,
                passive,
                ):
        self.settings = self.read_json()
        self.file_path = file_path,
        self.search_count = search_count,
        self.aggression = aggression,
        self.aggressive_max = aggressive[0],
        self.aggressive_min = aggressive[1]
        self.moderate_max = moderate[0],
        self.moderate_min = moderate[1],
        self.passive_max = passive[0],
        self.passive_min = passive[1]


    def read_json() -> dict:
        with open("settings.json", 'r') as f:
            settings = json.load(f)
        return settings


    def write_json(self) -> None:
        with open('settings.json', 'w') as f:
            json.dump(self.settings, f)


    def set_count(self) -> None:
        if self.search_count != None:
            self.settings["maxSiteSearch"] = self.search_count


    def set_path(self) -> None:
        if self.file_path != None:
            self.settings["filePath"] = self.file_path


    def set_aggression(self) -> None:
        if self.aggression != None:
            self.settings["defaultAggression"] = self.aggression


    def set_aggressive_wait(self) -> None:
        if self.aggressive_max != None and self.aggressive_min != None:
            self.settings["aggressiveMaxWait"] = self.aggressive_max
            self.settings["aggressiveMinWait"] = self.aggressive_min


    def set_moderate_wait(self) -> None:
        if self.moderate_max != None and self.moderate_min != None:
            self.settings["moderateMaxWait"] = self.moderate_max
            self.settings["moderateMinWait"] = self.moderate_min


    def set_passive_wait(self) -> None:
        if self.passive_max != None and self.passive_min != None:
            self.settings["passiveMaxWait"] = self.passive_max
            self.settings["passiveMinWait"] = self.passive_min


    def show_settings(self) -> None:
        print("DEFAULT SETTINGS")
        for key in self.settings:
            print(f"{key}: {self.settings[key]}")


    def update_settings(self) -> None:
        self.set_count()
        self.set_path()
        self.set_aggression()
        self.set_aggressive_wait()
        self.set_moderate_wait()
        self.set_passive_wait()
        self.write_json()
