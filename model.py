from dataclasses import dataclass
from tinydb import TinyDB, where

DB_PATH = 'mvc-history-db.json'
db = TinyDB(DB_PATH)
history_numbers_table = db.table('history')


@dataclass
class history:
    """
    Represents commands history
    :attribute number: the number that entered by the user in the request
    :attribute amount: the number of times this number has appeared in the bot history
    """
    number: int
    amount: int


class HistoryModelWrapper:
    """
    Wrapped class to handle request history and store it in the db
    """
    @classmethod
    def get_by_number(cls, number: int) -> history:
        """
        return the record that fits num
        :return: record from the db by num
        """
        return history_numbers_table.search(where('number') == number)
    
    
    @classmethod
    def create(cls, num: int) -> None:
        """  
        insert the db new record or update the amount if the number already exists
        """
        if cls.get_by_number(num):
            amount = cls.get_by_number(num)[0]['amount'] + 1
            history_numbers_table.update({'amount': amount},where('number') == num)
        else:    
            history_numbers_table.insert({'number': num, 'amount': 1})  

    @classmethod
    def get_all_history(cls) -> list:
        """
        :return: list of all records from the db
        """
        return history_numbers_table.all()