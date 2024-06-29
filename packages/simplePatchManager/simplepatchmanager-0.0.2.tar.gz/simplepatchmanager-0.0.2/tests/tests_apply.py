from .applyunapplybasecommandtest import ApplyUnapplyBaseCommandTest


class ApplyCommandTests(ApplyUnapplyBaseCommandTest):

    def test_should_apply_patch(self):
        self._create_patch_file()

        self._spm('apply', 'patch')

        with open(self.filename) as file:
            self.assertEqual(file.readline(), '1\n')
            self.assertEqual(file.readline(), '2\n')
            self.assertEqual(file.readline(), '3\n')
            self.assertEqual(file.readline(), '4\n')
            self.assertEqual(file.readline(), '5\n')
            self.assertEqual(file.readline(), '')


    def test_should_not_apply_patch(self):
        self._create_patch_file()

        self._spm('apply', 'patch', '--dry-run')

        with open(self.filename) as file:
            self.assertEqual(file.readline(), '1\n')
            self.assertEqual(file.readline(), '2\n')
            self.assertEqual(file.readline(), '')

