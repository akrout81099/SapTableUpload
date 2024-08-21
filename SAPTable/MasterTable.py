from datetime import datetime
from SAP.PyRFCConnection import PyRFCConnection
from SAP.RFCReadLongTable import RFCReadLongTable


class MasterTable:
    """
    Class responsible for reading data from SAP tables. This class
    represents table that contain date time fields and does not depend
    on other table to fill data.

    :param sap_connection: SAP Connection object
    :type sap_connection: PyRFCConnection
    :param table_name: Name of the Table
    :type table_name: str
    :param query_field: Dictionary containing field and info like date and time about the field
    :type query_field: dict
    :param additional: Dictionary containing any additional query for the table
    :type additional: dict
    """

    def __init__(self,
                 sap_connection: PyRFCConnection,
                 table_name: str,
                 query_field: dict,
                 fields: list = None,
                 additional: dict = None):
        """
        Constructor method

        :param sap_connection: SAP Connection object
        :type sap_connection: PyRFCConnection
        :param table_name: Name of the Table
        :type table_name: str
        :param fields: List of Field Name to be fetched
        :type fields: list
        :param query_field: Dictionary containing field and info like date and time about the field
        :type query_field: dict
        :param additional: Dictionary containing any additional query for the table
        :type additional: dict
        """
        self.sap_connection = sap_connection
        self.table_name = table_name
        self.query_field = query_field
        self.fields = fields
        self.additional = additional

    def get_data(self, query_datetime: datetime) -> dict:
        """
        Fetch Data from the table
        :param query_datetime: Query Date and Time
        :type query_datetime: datetime
        :return: Return Data from SAP
        :rtype: dict
        """
        rfc_read_table = RFCReadLongTable(self.sap_connection)
        query_date = query_datetime.strftime('%Y%m%d')
        query_time = query_datetime.strftime('%H%M00')

        if 'TIME' in self.query_field.keys():
            res = rfc_read_table.run(query_table=self.table_name,
                                     options=[{'TEXT': f"{self.query_field['DATE']} >= '{query_date}'"},
                                              {'TEXT': ' AND '},
                                              {'TEXT': f"{self.query_field['TIME']} >= '{query_time}'"}],
                                     fields=self.fields)
        else:
            res = rfc_read_table.run(query_table=self.table_name,
                                     options=[{'TEXT': f"{self.query_field['DATE']} >= '{query_date}'"}],
                                     fields=self.fields)


        return res
