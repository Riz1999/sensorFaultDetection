from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_filed_path:str
    test_file_path:str