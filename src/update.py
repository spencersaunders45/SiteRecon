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
        self.aggressive_wait = aggressive,
        self.moderate_wait = moderate,
        self.passive_wait = passive
        self.write_changes = False


    def read_json(self) -> dict:
        """
        Reads the json file to be edited

        Parameters:
            None

        Returns:
            None
        """
        with open("settings.json", 'r') as f:
            settings = json.load(f)
        return settings


    def write_json(self) -> None:
        """
        Writes the changes to the json file

        Parameters:
            None

        Returns:
            None
        """
        with open('settings.json', 'w') as f:
            json.dump(self.settings, f)


    def set_count(self) -> None:
        """
        Updates the number of sites to be scanned

        Parameters:
            None

        Returns:
            None
        """
        if self.search_count[0] != None:
            self.settings["maxSiteSearch"] = self.search_count[0]
            self.write_changes = True


    def set_path(self) -> None:
        """
        Updates the path where the file is to be saved

        Parameters:
            None

        Returns:
            None
        """
        if self.file_path[0] != None:
            self.settings["filePath"] = self.file_path[0]
            self.write_changes = True


    def set_aggression(self) -> None:
        """
        Updates the default aggression

        Parameters:
            None

        Returns:
            None
        """
        if self.aggression[0] != None:
            self.settings["defaultAggression"] = self.aggression[0]
            self.write_changes = True


    def set_aggressive_wait(self) -> None:
        """
        Sets the wait time for aggressive

        Parameters:
            None

        Returns:
            None
        """
        if self.aggressive_wait[0] != None:
            self.settings["aggressiveMaxWait"] = self.aggressive_wait[0][1]
            self.settings["aggressiveMinWait"] = self.aggressive_wait[0][0]
            self.write_changes = True


    def set_moderate_wait(self) -> None:
        """
        Sets the wait time for moderate

        Parameters:
            None

        Returns:
            None
        """
        if self.moderate_wait[0] != None:
            self.settings["moderateMaxWait"] = self.moderate_wait[0][1]
            self.settings["moderateMinWait"] = self.moderate_wait[0][0]
            self.write_changes = True


    def set_passive_wait(self) -> None:
        """
        Sets the wait time for passive

        Parameters:
            None

        Returns:
            None
        """
        if self.passive_wait != None:
            self.settings["passiveMaxWait"] = self.passive_wait[1]
            self.settings["passiveMinWait"] = self.passive_wait[0]
            self.write_changes = True


    def show_settings(self) -> None:
        """
        Prints the current settings

        Parameters:
            None

        Returns:
            None
        """
        print("DEFAULT SETTINGS")
        for key in self.settings:
            print(f"\t{key}: {self.settings[key]}")


    def update_settings(self) -> None:
        """
        Calls the functions to update all the settings

        Parameters:
            None

        Returns:
            None
        """
        self.set_count()
        self.set_path()
        self.set_aggression()
        self.set_aggressive_wait()
        self.set_moderate_wait()
        self.set_passive_wait()
        if self.write_changes:
            self.write_json()


def read_settings() -> dict:
    """
    Reads the json file

    Parameters:
        None

    Returns:
        None
    """
    with open("settings.json", 'r') as f:
        settings = json.load(f)
    return settings
