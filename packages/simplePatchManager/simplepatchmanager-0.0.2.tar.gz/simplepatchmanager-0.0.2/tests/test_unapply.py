from .applyunapplybasecommandtest import ApplyUnapplyBaseCommandTest

import os


class UnapplyCommandTests(ApplyUnapplyBaseCommandTest):

    def test_should_unapply_patch(self):
        with open(self.filename, 'a') as file:
            file.write('3\n')
            file.write('4\n')
            file.write('5\n')

        self._create_patch_file()

        self._spm('unapply', 'patch')

        with open(self.filename) as file:
            self.assertEqual(file.readline(), '1\n')
            self.assertEqual(file.readline(), '2\n')
            self.assertEqual(file.readline(), '')


    def test_should_keep_patch(self):
        with open(self.filename, 'a') as file:
            file.write('3\n')
            file.write('4\n')
            file.write('5\n')

        self._create_patch_file()

        self._spm('unapply', 'patch', '--dry-run')

        with open(self.filename) as file:
            self.assertEqual(file.readline(), '1\n')
            self.assertEqual(file.readline(), '2\n')
            self.assertEqual(file.readline(), '3\n')
            self.assertEqual(file.readline(), '4\n')
            self.assertEqual(file.readline(), '5\n')
            self.assertEqual(file.readline(), '')
