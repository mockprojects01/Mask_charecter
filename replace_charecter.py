import pandas as pd

df = pd.read_csv('file_to_mask.csv')


class ColumnReplacer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def replace_columns(self):
        self.dataframe['email'] = self.dataframe['email'].apply(
            lambda x: self.replace_email(x))
        self.dataframe['phone_number'] = self.dataframe['phone_number'].apply(
            lambda x: self.replace_phone_number(x))
        self.dataframe['credit_card'] = self.dataframe['credit_card'].apply(
            lambda x: self.replace_credit_card(x))
        return self.dataframe

    @staticmethod
    def replace_email(email):
        if '@gmail.com' in email:
            return email.replace('@gmail.com', '@' + '#' * 8)
        return email

    @staticmethod
    def replace_phone_number(phone_number):
        return '#' * 10

    @staticmethod
    def replace_credit_card(credit_card):
        return credit_card[:-12] + '#' * 12


class DollarSignRemover:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remove_dollar_sign(self):
        self.dataframe['Amount'] = self.dataframe['Amount'].apply(
            lambda x: self.remove_dollar(x))
        return self.dataframe

    @staticmethod
    def remove_dollar(amount):
        return amount.replace('$', '')


column_masker = ColumnReplacer(df)
masked_df = column_masker.replace_columns()
print(masked_df)

dollar_removal = DollarSignRemover(masked_df)
result_df = dollar_removal.remove_dollar_sign()
print(result_df)
