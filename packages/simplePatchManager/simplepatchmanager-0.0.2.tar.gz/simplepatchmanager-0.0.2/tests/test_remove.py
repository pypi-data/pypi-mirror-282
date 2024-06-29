from .basecommandtest import BaseCommandTest

import os


class RemoveCommandTests(BaseCommandTest):

    def test_should_remove_patchs(self):
        self._create_empty_patch('patch1')
        self._create_empty_patch('patch2')

        self._spm('remove', 'patch1', 'patch2')

        self.assertFalse(os.path.exists(os.path.join(self.repository_patches_folder, 'patch1')))
        self.assertFalse(os.path.exists(os.path.join(self.repository_patches_folder, 'patch2')))
