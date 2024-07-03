import os
from os.path import join
from dotenv import load_dotenv

class Config:
    def get(value: str):
        load_dotenv(join(os.path.abspath(os.curdir), '.env'))
        return os.getenv(value)
    
    def project_key():
        return os.getenv('PROJECT_KEY', "ADOPOC")
    
    def test_type():
        return os.getenv('TEST_TYPE', "CUCUMBER")
    
    def xray_api():
        return os.getenv('XRAY_API', "https://xray.cloud.getxray.app/api/v2")
    
    def xray_client_id():
        return os.getenv('XRAY_CLIENT_ID', "263D777731484300A57C5517281F615B")
    
    def xray_client_secret():
        return os.getenv('XRAY_CLIENT_SECRET', "3b011f11247182b751d7689b291245888538b12b79d89aa88a590f5dfa4fcca1")
    
    def cucumber_path():
        return os.getenv('CUCUMBER_PATH', "/tmp/")