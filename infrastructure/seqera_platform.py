class SeqeraConfigInterface():
    def fetch_secrets():
        pass 
    
    def parse_config():
        pass 
     

class SeqeraConfig(SeqeraConfigInterface):
    
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        
    def fetch_secrets(self):
        pass 
    
    def parse_config(self):
        pass 
    
    
class SeqeraGCPConfig(SeqeraConfig):
    
    def __init__(self, file_path: str) -> None:
       self.file_path = file_path
       super().__init__(file_path)
       
    
    def fetch_secrets(self):
        pass
    
    def parse_config(self):
        pass

    