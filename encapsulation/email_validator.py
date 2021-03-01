from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __convert_name_to_what_i_need(self, input):
        name, temp = input.split("@")
        mail, domain = temp.split(".")
        return (name, mail, domain)

    def __validate_name(self, name):
        name, *args = self.__convert_name_to_what_i_need(name)
        return len(name) >= self.min_length

    def __validate_email(self, mail):
        _, mail, *args = self.__convert_name_to_what_i_need(mail)
        return mail in self.mails

    def __validate_domain(self, domain):
        *args, domain = self.__convert_name_to_what_i_need(domain)
        return domain in self.domains

    def validate(self, mails):
        return all([self.__validate_name(mails), self.__validate_email(mails), self.__validate_domain(mails)])


if __name__ == "__main__":
    import unittest

    class TestEmailValidator(unittest.TestCase):
        mails = ["gmail", "softuni"]
        domains = ["com", "bg"]

        def setUp(self):
            self.check = EmailValidator(6, __class__.mails, __class__.domains)

        def test_all_is_setup(self):
            self.assertEqual(self.check.min_length, 6)
            self.assertEqual(self.check.mails, __class__.mails)
            self.assertEqual(self.check.domains, __class__.domains)

        def test_decompose_what_i_need(self):
            expected = ("pe77er", "gmail", "com")
            actual = self.check._EmailValidator__convert_name_to_what_i_need("pe77er@gmail.com")
            self.assertEqual(expected, actual)

        def test_validate_name(self):
            actual = self.check._EmailValidator__validate_name("pe77er@gmail.com")
            return actual
            self.assertTrue(actual)

        def test_validate_email(self):
            actual = self.check._EmailValidator__validate_email("pe77er@gmail.com")
            return actual
            self.assertTrue(actual)

        def test_validate_domain(self):
            actual = self.check._EmailValidator__validate_domain("pe77er@gmail.com")
            return actual
            self.assertTrue(actual)

        def test_validate_domain_return_false_when_is_not_correct(self):
            actual = self.check._EmailValidator__validate_domain("pe77er@gmai.co")
            self.assertFalse(actual)

        def test_validate(self):
            actual = all([self.test_validate_name(), self.test_validate_domain(), self.test_validate_email])
            self.assertTrue(actual)

        def test_validate_with_error(self):
            actual = all(
                [
                    self.test_validate_name(),
                    self.test_validate_domain_return_false_when_is_not_correct(),
                    self.test_validate_email,
                ]
            )
            self.assertFalse(actual)

    unittest.main()
