from .basecommandtest import BaseCommandTest

import os


class ListCommandTests(BaseCommandTest):

    def test_should_print_patches_list(self):
        self._create_empty_patch('patch1')
        self._create_empty_patch('patch2')

        self._spm('list')

        self.stdout.finish()

        self.assertRegex(self.stdout[0], '^Folder: /tmp/simplePatchManager-[a-z0-9_]{8}/patches/repository$')
        self.assertRegex(self.stdout[1], 'patch1 +')
        self.assertRegex(self.stdout[2], 'patch2 +')


    def test_should_print_patches_list_with_descriptions(self):
        self._create_empty_patch('patch1')
        self._create_description_file('patch1', 'Description for patch 1')
        self._create_empty_patch('patch2')

        self._spm('list')

        self.stdout.finish()

        self.assertRegex(self.stdout[0], '^Folder: /tmp/simplePatchManager-[a-z0-9_]{8}/patches/repository$')
        self.assertRegex(self.stdout[1], 'patch1 +Description for patch 1')
        self.assertRegex(self.stdout[2], 'patch2 +')


    def test_should_print_patches_list_raw_format(self):
        self._create_empty_patch('patch1')
        self._create_empty_patch('patch2')

        self._spm('list', '--raw')

        self.stdout.finish()

        self.assertRegex(self.stdout[0], 'patch1 +')
        self.assertRegex(self.stdout[1], 'patch2 +')

