from config import setting
import platform
import sys

def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in setting.model_dump().items()]
    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    properties = '\n'.join(items)

    with open(setting.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)