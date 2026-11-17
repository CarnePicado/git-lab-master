import unittest

from src.auth.login import authenticate
from src.auth.register import register_user


class AuthTests(unittest.TestCase):
    def test_register_user(self):
        users = {}
        self.assertTrue(register_user("alice", "secret", users))
        self.assertEqual(users["alice"], "secret")

    def test_duplicate_user(self):
        users = {"alice": "secret"}
        self.assertFalse(register_user("alice", "another", users))

    def test_authenticate_success(self):
        self.assertTrue(authenticate("alice", "secret", {"alice": "secret"}))

    def test_authenticate_failure(self):
        self.assertFalse(authenticate("alice", "wrong", {"alice": "secret"}))


if __name__ == "__main__":
    unittest.main()
