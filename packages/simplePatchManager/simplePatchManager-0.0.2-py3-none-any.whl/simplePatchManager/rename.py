from .command import AbstractCommand
from .status import Status
import os


class RenameCommand(AbstractCommand):

    def __init__(self, args):
        super().__init__(args)

    @staticmethod
    def make_parser(subparsers):
        create_parser = subparsers.add_parser('rename', aliases=['rn'], help='Rename a patch')
        create_parser.set_defaults(handler_class=RenameCommand)
        create_parser.add_argument('old_name')
        create_parser.add_argument('new_name')

    def _do_run(self):
        oldpath = self._getPatchFileName(self._args.old_name)
        newpath = self._getPatchFileName(self._args.new_name)

        os.rename(oldpath, newpath)

        print(f'{oldpath} -> {newpath}')

        return Status.ok()
