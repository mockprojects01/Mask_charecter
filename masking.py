import pandas as pd

data = {
    'name': ['Vaibhaw', 'Aftab', 'Harbeer'],
    'email': ['vaibhaw2345@gmail.com', 'aftab123@gmail.com', 'harbeer234@gmail.com'],
    'phone_number': ['7890123456', '9876543210', '7654321067'],
    'credit_card': ['1234 5678 9012 3456', '9876 5432 1098 7654', '1098 7654 9876 5432']
}

df = pd.DataFrame(data)


class ColumnMasking:
    def __init__(self, dataframe, masking_character='*'):
        self.dataframe = dataframe
        self.masking_character = masking_character

    def mask_columns(self):
        self.dataframe['email'] = self.dataframe['email'].apply(
            lambda x: self.mask_email(x))
        self.dataframe['phone_number'] = self.dataframe['phone_number'].apply(
            lambda x: self.mask_phone_number(x))
        self.dataframe['credit_card'] = self.dataframe['credit_card'].apply(
            lambda x: self.mask_credit_card_number(x))
        return self.dataframe

    def mask_email(self, email):
        username, domain = email.split('@')
        username_masked = self.masking_character * len(username)
        return f"{username_masked}@{domain}"

    def mask_phone_number(self, phone_number):
        return self.masking_character * len(phone_number)

    def mask_credit_card_number(self, credit_card):
        last_4_digits = credit_card[-4:]
        return self.masking_character * (len(credit_card) - 4) + last_4_digits


column_masker = ColumnMasking(df)
masked_df = column_masker.mask_columns()

print(masked_df)
