from datetime import datetime

class text_logger:
    _info_log_path = "data/info_log.txt"
    _warning_log_path = "data/warning_log.txt"
    _error_log_path = "data/error_log.txt"

    def INFO(self, message):
        with open(self._info_log_path, 'a+') as f:
            f.write(f"[ * ] [{datetime.now()}] INFO: \"{message}\" \n")

    def WARNING(self, message):
        with open(self._warning_log_path, 'a+') as f:
            f.write(f"[ ? ] [{datetime.now()}] WARNING: \"{message}\" \n")

    def ERROR(self, message):
        with open(self._error_log_path, 'a+') as f:
            f.write(f"[ ! ] [{datetime.now()}] ERROR: \"{message}\" \n")