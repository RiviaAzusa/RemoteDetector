import sys
import yaml
import logging

from PySide6.QtWidgets import QApplication
from src.ui import MainWindow


class RemoteDetector:
    def __init__(self, cfg: dict,):
        self.config = cfg

    def run(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()
        sys.exit(self.app.exec())


def logging_setting(log_path):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        handlers=[logging.FileHandler(log_path),
                                  logging.StreamHandler(sys.stdout)]
                        )

    logging.info(f'Logging Server Start!')


def main(config: str):
    with open(config, 'r') as f:
        config: dict = yaml.safe_load(f)
    logging.info(f'Successful lodding config file from: {config}')
    logging_setting(config.get('log_path'))
    remoteDetector = RemoteDetector(config)
    remoteDetector.run()


if __name__ == '__main__':
    config_path = 'resources/config.yml'
    main(config=config_path)
