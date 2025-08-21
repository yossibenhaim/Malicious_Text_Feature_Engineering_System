from DAL.DAL import DAL
from processor import Processor
from utils import Utils

class Manager:

    def __init__(self):
        self.dal = DAL()
        self.process = Processor()

    def get_data_from_mongo(self):
        data = self.dal.get_all_data()
        data = Utils.correct_the_id(data)
        self.process.create_dataframe(data)
        self.process.create_the_columns_sentiment_and_rarest_word()
        self.process.return_data()
        data_dict = self.process.return_data().to_dict(orient='records')
        print(data_dict)
        return data_dict


