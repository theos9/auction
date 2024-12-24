import random

class OtpGenerator():
    @staticmethod
    def GenerateOtp():
        return str(random.randint(100000, 999999))