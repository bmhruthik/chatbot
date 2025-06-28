from configparser import ConfigParser

class UIConfig:
    def __init__(self, config_file='./src/ui/uiconfig.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")

    def get_usecase_option(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_option(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "Welcome to the multi LLM App!")
    


# if __name__ == "__main__":
#     config = UIConfig()
#     print("LLM Options:", config.get_llm_option())
#     print("Use Case Options:", config.get_usecase_option())
#     print("GROQ Model Options:", config.get_groq_model_option())
#     print("Page Title:", config.get_page_title())