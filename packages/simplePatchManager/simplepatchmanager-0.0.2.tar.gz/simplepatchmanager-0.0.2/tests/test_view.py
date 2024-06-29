from .basecommandtest import BaseCommandTest

import os


class ViewCommandTests(BaseCommandTest):

    def test_should_print_patch(self):
        with open(os.path.join(self.repository_patches_folder, 'patch.patch'), 'w') as patch_file:
            patch_file.write('diff --git file file\n')
            patch_file.write('index 1191247..8a1218a 100644\n')
            patch_file.write('--- file\n')
            patch_file.write('+++ file\n')
            patch_file.write('@@ -1,2 +1,5 @@\n')
            patch_file.write(' 1\n')
            patch_file.write(' 2\n')
            patch_file.write('+3\n')
            patch_file.write('+4\n')
            patch_file.write('+5\n')

        self._spm('view', 'patch')

        self.stdout.finish()

        self.assertRegex(self.stdout[0], '>>>>> /tmp/simplePatchManager-[a-z0-9_]{8}/patches/repository/patch.patch')
        self.assertEqual(self.stdout[1], 'diff --git file file')
        self.assertEqual(self.stdout[2], 'index 1191247..8a1218a 100644')
        self.assertEqual(self.stdout[3], '--- file')
        self.assertEqual(self.stdout[4], '+++ file')
        self.assertEqual(self.stdout[5], '@@ -1,2 +1,5 @@')
        self.assertEqual(self.stdout[6], ' 1')
        self.assertEqual(self.stdout[7], ' 2')
        self.assertEqual(self.stdout[8], '+3')
        self.assertEqual(self.stdout[9], '+4')
        self.assertEqual(self.stdout[10], '+5')
        self.assertRegex(self.stdout[11], '<<<<< /tmp/simplePatchManager-[a-z0-9_]{8}/patches/repository/patch.patch')

