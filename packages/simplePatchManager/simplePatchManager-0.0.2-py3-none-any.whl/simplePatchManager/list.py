from .command import AbstractCommand
import os
from . status import Status


class ListCommand(AbstractCommand):

    def __init__(self, args):
        super().__init__(args)

    @staticmethod
    def make_parser(subparsers):
        list_parser = subparsers.add_parser('list', aliases=['l', 'ls'], help='List the existing patchs')
        list_parser.set_defaults(handler_class=ListCommand)
        list_parser.add_argument('-r', '--raw', action='store_true', help='Raw listing, no formatted output')

    def _do_run(self):
        if not os.path.isdir(self._getPatchsFolder()):
            return Status.error(f'Patchs folder doesn\'t exist ({self._getPatchsFolder()})...')

        if self._args.raw:
            return self._raw_list()

        return self._default_list()

    def _default_list(self):
        print(f'Folder: {self._getPatchsFolder()}')

        patches = self._list_patches()

        widest_patch = -1
        for patch_name in patches.keys():
            if len(patch_name) > widest_patch:
                widest_patch = len(patch_name)

        separator = '    '

        for patch, description in patches.items():
            filler = ' ' * (widest_patch - len(patch))
            print(f'{patch}{filler}{separator}{description}')

        print()

        patch_count = len(patches.items())
        if patch_count == 0:
            print('No patches found')
        else:
            print(f'{patch_count} patch{"s" if patch_count > 1 else ""} found')

        return Status.ok()

    def _raw_list(self):
        for patch in self._list_patches().keys():
            print(patch)

        return Status.ok()

