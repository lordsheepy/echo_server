import unittest
import mysocket
import myclient

"""Test package for echo_server"""


class TestServer(unittest.TestCase):

    def testMessageShort(self):
        test_s = "a3th8go"
        self.assertequal(test_s, myclient.start_client(test_s))

    def testMessageLong(self):
        test_L = "a;ewghaohnghenrgi;uhae;roguhna;owrogun;kunnfg;jn"
        self.assertequal(test_L, myclient.start_client(test_L))

    def testMessageExact(self):
        test_e = "12345678909876543212345678909876"
        self.assertequal(test_e, myclient.start_client(test_e))

if __name__ == "__main__":
    unittest.main()
