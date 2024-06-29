from .basecommandtest import BaseCommandTest

import os


class InfoCommandTests(BaseCommandTest):

    def test_should_print_context_name_patches_folder_and_patch_count(self):
        self._create_empty_patch('patch1')
        self._create_empty_patch('patch2')

        self._spm('info')

        self.stdout.finish()

        self.assertRegex(self.stdout[0], r'^Repository        /tmp/simplePatchManager-[0-9a-z]{8}/patches$')
        self.assertEqual(self.stdout[1], f'Active context    repository')
        self.assertEqual(self.stdout[2], f'Patch count       2')


    def test_should_get_context_from_git_remote_when_available(self):
        self._git('remote', 'add', 'origin', 'git@host:user/repo_name.git')

        # self.stdout.finish()

        #breakpoint(context=20)
        self.context = None
        self._spm('info')

        self.stdout.finish()

        self.assertEqual(self.stdout[1], f'Active context    repo_name')

