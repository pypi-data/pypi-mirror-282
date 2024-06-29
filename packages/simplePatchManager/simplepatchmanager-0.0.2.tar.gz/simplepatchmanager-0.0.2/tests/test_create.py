from .basecommandtest import BaseCommandTest

import os


class CreateCommandTests(BaseCommandTest):

    def _create_patch_file(self):
        with open(self.filename, 'w') as file:
            file.write('1\n')
            file.write('1.1\n')
            file.write('1.2\n')
            file.write('1.3\n')
            file.write('2\n')

        self._spm('create', 'patch_file')


    def test_should_create_a_patch_file(self):
        self._create_patch_file()

        self.assertFilesEquals('create_tests__simplest_creation.patch', os.path.join(self.patches_folder, self.context, 'patch_file.patch'))


    def test_should_append_to_patch_file(self):
        self._create_patch_file()

        self._git('restore', '.')

        with open(self.filename, 'a') as file:
            file.write('3\n')
            file.write('4\n')
            file.write('5\n')

        self._spm('c', '--append', 'patch_file')

        self.assertFilesEquals('create_tests__appending_to_file.patch', os.path.join(self.patches_folder, self.context, 'patch_file.patch'))


if __name__ == '__main__':
    unittest.main()
