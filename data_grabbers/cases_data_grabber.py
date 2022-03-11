from data_grabbers.data_grabber import DataGrabber
from data_grabbers.graphs_data_grabber import GraphsDataGrabber

class CasesDataGrabber(DataGrabber):
    DATASET_PREFIX = "cases"

    def __init__(self):
        super()

    def grab_data(self):
        graphs_grabber = GraphsDataGrabber()

        data = graphs_grabber.get_data("coronavirus-cases")
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(CasesDataGrabber.DATASET_PREFIX, dataset_date=dataset_date)
