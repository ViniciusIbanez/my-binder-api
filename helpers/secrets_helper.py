from dotenv import load_dotenv
from .json_helper import load_json
from pathlib import Path
import os


def load_env():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

def retrieve_secrets(local=os.getenv('local')):
    if local:
        load_env()
    secrets = {}
    env_variables = load_json(f'{os.getcwd()}/model/secrets/SecretsModel')

    for variable in env_variables.get('env_variables'):
        secrets[variable] = os.getenv(variable)

    return secrets
