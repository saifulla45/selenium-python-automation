import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    
    @staticmethod
    def get_page_url():
        return config.get('login info','page_url')
    
    @staticmethod
    def get_email_id():
        return config.get('login info','username')
    
    @staticmethod
    def get_password():
        return config.get('login info','password')
    
    @staticmethod
    def get_invalid_email_id():
        return config.get('login info','invalid_username')
    