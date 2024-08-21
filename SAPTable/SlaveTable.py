import math
from datetime import datetime
from SAP.PyRFCConnection import PyRFCConnection
from SAP.RFCReadLongTable import RFCReadLongTable


class SlaveTable:
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
                 master_table: str,
                 field_relations: list,
                 fields: list = None,
                 additional: dict = None):
        """
        Constructor method

        :param sap_connection: SAP Connection object
        :type sap_connection: PyRFCConnection
        :param table_name: Name of the Table
        :type table_name: str
        :param master_table: Name of the Master Table
        :type master_table: str
        :param fields: List of Field Name to be fetched
        :type fields: list
        :param field_relations: List containing field and info like date and time about the field
        :type field_relations: list
        :param additional: Dictionary containing any additional query for the table
        :type additional: dict
        """
        self.sap_connection = sap_connection
        self.table_name = table_name
        self.master_table = master_table
        self.field_relations = field_relations
        self.fields = fields
        self.additional = additional

    def get_data(self, master_data_list: list) -> dict:
        """
        Fetch Data from the table

        :param master_data_list: List of Identifying info from Master Table
        :type master_data_list: list
        :return: Return Data from SAP
        :rtype: dict
        """
        query_list = self._generate_query_list(master_data_list)
        rfc_read_table = RFCReadLongTable(self.sap_connection)
        list_length = len(query_list)
        options_arr = []
        for i in range(math.ceil(list_length / 1000)):
            if i == math.ceil(list_length / 1000) - 1:
                options_arr.append(query_list[i * 1000:])
            else:
                options_arr.append(query_list[i * 1000:(i + 1) * 1000])

        result_arr = []
        _f = None
        _o = None
        for _options in options_arr:
            options = []
            for op in _options:
                options.append(op)
                options.append({'TEXT': ' OR '})

            options = options[:-1]

            res = rfc_read_table.run(query_table=self.table_name,
                                     options=options,
                                     fields=self.fields)
            result_arr = result_arr + res['DATA']
            _f = res['FIELDS']
            _o = res['OPTIONS']

        return {'DATA': result_arr,
                'FIELDS': _f,
                'OPTIONS': _o}

    def _generate_query_list(self, master_data_list: list) -> list:
        options_list = []
        for item in master_data_list:
            if len(self.field_relations) == 1:
                rel = self.field_relations[0]
                master_field = rel['MASTER']
                slave_field = rel['SLAVE']
                option = {'TEXT': f"{slave_field} = '{item[master_field]}'"}
                options_list.append(option)
            else:
                option_sub_arr = []
                for rel in self.field_relations:
                    master_field = rel['MASTER']
                    slave_field = rel['SLAVE']

                    option = {'TEXT': f"{slave_field} = '{item[master_field]}'"}
                    option_sub_arr.append(option)
                    option_sub_arr.append({'TEXT': ' AND '})

                option_sub_arr[0]['TEXT'] = "(" + option_sub_arr[0]['TEXT']
                option_sub_arr = option_sub_arr[:len(option_sub_arr) - 1]
                option_sub_arr[-1]['TEXT'] = option_sub_arr[-1]['TEXT'] + ")"
                option = {'TEXT': option_sub_arr}
                options_list.append(option)
        return options_list
