from SAP.SAPConnectionInterface import SAPConnectionInterface


class EMGetNumberOfEntries:
    """
    Class responsible to get number of entries in a Table
    It uses RFC function "EM_GET_NUMBER_OF_ENTRIES"
    """
    def __init__(self, connection: SAPConnectionInterface):
        """
        Constructor method

        :param connection: An instance of a class implementing SAPConnectionInterface Interface
        :type connection: SAPConnectionInterface
        """
        self.connection = connection

    def run(self, it_tables: list) -> dict:
        """
        RFC EM_GET_NUMBER_OF_ENTRIES function to get number of entries in a Table in SAP
        :param it_tables: List of Tables
        :type it_tables: list
        :return: Dictionary containing List of Tables with number of entries
        :rtype: dict
        """
        return self.connection.call('EM_GET_NUMBER_OF_ENTRIES',
                                    IT_TABLES=it_tables)
