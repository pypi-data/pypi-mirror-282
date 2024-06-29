from .command import AbstractCommand
from .status import Status
import os

class InfoCommand(AbstractCommand):

    def __init__(self, args):
        super().__init__(args)

    @staticmethod
    def make_parser(subparsers):
        parser = subparsers.add_parser('info', aliases=['i'], help='Print information about folder structure')
        parser.set_defaults(handler_class=InfoCommand)
        parser.add_argument('-f', '--filenames', default=list(), action='extend', nargs='+')

    def _check_args(self):
        return self._check_filename_existence(self._args.filenames)

    def _do_run(self):
        patch_count = len(self._list_patches())

        print(f'Repository        {self._args.patchs_folder}')
        print(f'Active context    {self._args.context}')
        print(f'Patch count       {patch_count}')

        return Status.ok()
