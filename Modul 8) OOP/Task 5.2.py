class PasswordChecker:
    def set_password_range(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def check_passwords(self, passwords):
        return list(map(lambda password: self.min_len <= len(password) <= self.max_len, passwords))


checker1 = PasswordChecker()
checker1.set_password_range(5, 10)
print(checker1.min_len, checker1.max_len)

# 5 10

print(checker1.check_passwords(['qwer', 'fool67', 'ghjo478hl404']))

# [False, True, False]

