L: test_public_repos_url (test_client.TestGithubOrgClient)
      ----------------------------------------------------------------------
      Traceback (most recent call last):
        File "/usr/local/lib/python3.7/unittest/mock.py", line 1204, in
        patched
            return func(*args, **keywargs)
              File
"/alx-backend-python/0x03-Unittests_and_integration_tests/test_client.py",
              line 37, in test_public_repos_url
                  self.assertEqual(recieved,'https://api.github.com/orgs/test_org/repos')
                  AssertionError: <MagicMock name='org.__getitem__()'
id='140060953759024'> != 'https://api.github.com/orgs/test_org/repos'

                  ----------------------------------------------------------------------
                  Ran 3 tests in 0.002s

                  FAILED (failures=1)
