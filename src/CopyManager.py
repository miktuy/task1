import shutil
from typing import List

from src.ConfigHandler import FileDescription
from src.logger import logger


class CopyManager:
    def __init__(self, files: List[FileDescription]):
        self.files = files
        self._copy_all_with_replace = False
        self._skip_existed_destination = False

    def copy(self):
        if not self.files:
            logger.warning('Nothing to copy...')
            return

        logger.info('Copying is started...')
        for file in self.files:
            should_process_file = True
            if self._skip_existed_destination and file.destination_path.exists():
                continue
            elif file.destination_path.exists() and not self._copy_all_with_replace:
                should_process_file = self._handle_file_destination(file)

            if should_process_file:
                self._copy(file)
        logger.info('Copying is finished!')

    def _handle_file_destination(self, file: FileDescription):
        print(
            f'File {file.destination_path} already exists! '
            f'Do you want replace\n'
            f'\t(print `all` if you want to replace all existed files\n'
            f'\t print `skip` if you do not want to replace all existed files)?'
            f' (y/n/all/skip):',
            end=' '
        )
        answer = input().lower()
        if answer == 'all':
            self._copy_all_with_replace = True
            return True
        if answer == 'skip':
            self._skip_existed_destination = True
            return False
        elif answer == 'y':
            return True
        return False

    @staticmethod
    def _copy(file: FileDescription):
        try:
            file.destination_path.parent.mkdir(exist_ok=True, parents=True)
            shutil.copy(file.source_path, file.destination_path)
        except Exception as e:
            logger.warning(f'Something wrong: {e}')

        logger.info(f'File `{file.source_path.resolve()}` is copied to `{file.destination_path.resolve()}`.')
