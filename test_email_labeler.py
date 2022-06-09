# Importing the unittest library which would help perform the tests and
# also the email_label function coming from the email_labeler script.

import unittest
from email_labeler import email_label


# Creating a class with inheritance from the TestCase class found in the unittest module
class TestEmailLabeler(unittest.TestCase):
    '''
        Performs unit testing to assert that the email labels from the "email_label" function are correct.

        Attributes:
            Inherited from the TestCase class in Unittest module

        Methods:
            Runs unit tests on the "email_label" function to validate the result.

    '''

    def test_email_label(self):
        '''
        Runs unit tests to validate the results of the "email_label" function

        Args:
            None

        Returns:
            Returns whether the test was OK or failed.
        '''

        self.assertEqual(email_label("share", "Can I share your email"), 'Student wants to know if can share')
        self.assertEqual(email_label("share", "I will share your email"), 'Student wants to know if can share')
        self.assertEqual(email_label("share", "I've shared your email"), 'Student has shared')
        self.assertEqual(email_label("share", "Should I share your email"), 'Student wants to know if can share')
        self.assertEqual(email_label("share", "I already shared the email"), 'Student has shared')


# Renaming to ensure we can easily run "python test_email_labeler.py" in the command line to perform the testing
if __name__ == '__main__':
    unittest.main()
