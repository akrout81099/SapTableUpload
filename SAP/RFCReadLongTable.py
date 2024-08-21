from SAP.SAPConnectionInterface import SAPConnectionInterface


class RFCReadLongTable:
    """
    Class responsible for reading data from SAP tables.
    It uses RFC function "RFC_READ_TABLE"
    """

    def __init__(self, connection: SAPConnectionInterface):
        """
        Constructor method

        :param connection: An instance of a class implementing SAPConnectionInterface Interface
        :type connection: SAPConnectionInterface
        """
        self.connection = connection

    def run(self,
            query_table: str,
            delimiter: str = '^',
            no_data: str = '',
            row_skips: int = 0,
            row_count: int = 0,
            fields: list = None,
            options: list = None) -> dict:
        """
        RFC READ TABLE function to fetch data from table in SAP

        :param query_table: Name of the Table
        :type query_table: str
        :param delimiter: Character to separate fields
        :type delimiter: str
        :param no_data: If this is empty only fields data would be sent
        :type no_data: str
        :param row_skips: Number of rows to skip
        :type row_skips: int
        :param row_count: Number of rows to read
        :type row_count: int
        :param fields: List of Field Name to be fetched
        :type fields: list
        :param options: Query Options
        :type options: list
        :return: List containing data from SAP table
        :rtype: list
        """
        fields = fields or []
        options = options or []

        fields_data = self._fetch_fields(query_table, fields)
        fields_array = self._split_fields(fields_data, no_data)
        responses = self._fetch_data(query_table, delimiter, no_data, row_skips, row_count, options,
                                     fields_array)
        result = self._merge_responses(responses, delimiter)

        return {'DATA': result, 'FIELDS': fields_data, 'OPTIONS': options}

    def _fetch_fields(self, query_table: str, fields: list) -> list:
        """
        Fetches Fields data from SAP

        :param query_table: SAP Table name
        :type query_table: str
        :param fields: List of Field Name to be fetched
        :type fields: list
        :return: List containing fields data from SAP table
        :rtype: list
        """
        return self.connection.call('RFC_READ_TABLE',
                                    QUERY_TABLE=query_table,
                                    NO_DATA='X',
                                    FIELDS=fields)['FIELDS']

    @staticmethod
    def _split_fields(fields_data: list, no_data: str) -> list:
        """
        Split Fields into sub list where total length of sub list is below 512

        :param fields_data: List of fields data from SAP
        :type fields_data: list
        :param no_data: No_data flag
        :type no_data: str
        :return:
        """
        if len(no_data) > 0:
            return []

        fields_array = []
        fields_sub_array = []
        _sum = 0
        _delimiter_offset = 0

        for field_data in fields_data:
            length = int(field_data['LENGTH'])
            if _sum + length + _delimiter_offset >= 512:
                fields_array.append(fields_sub_array)
                fields_sub_array = []
                _sum = 0
                _delimiter_offset = 0

            fields_sub_array.append(field_data)
            _sum += length
            _delimiter_offset += 1

        if fields_sub_array:
            fields_array.append(fields_sub_array)

        return fields_array

    def _fetch_data(self, query_table: str, delimiter: str, no_data: str, row_skips: int, row_count: int,
                    options: list, fields_array: list) -> list:
        """
        Fetches data from SAP

        :param query_table: Name of the Table
        :type query_table: str
        :param delimiter: Character to separate fields
        :type delimiter: str
        :param no_data: If this is empty only fields data would be sent
        :type no_data: str
        :param row_skips: Number of rows to skip
        :type row_skips: int
        :param row_count: Number of rows to read
        :type row_count: int
        :param options: Query Options
        :type options: list
        :return: List containing data from SAP table
        :rtype: list
        :param fields_array: List of Sub List of Appropriate Length
        :type fields_array: list
        :return: List of Sub List containing data from SAP table
        :rtype: list
        """
        responses = []
        for fields_sub_array in fields_array:
            res = self.connection.call('RFC_READ_TABLE',
                                       QUERY_TABLE=query_table,
                                       DELIMITER=delimiter,
                                       NO_DATA=no_data,
                                       ROWSKIPS=row_skips,
                                       ROWCOUNT=row_count,
                                       FIELDS=fields_sub_array,
                                       OPTIONS=options)
            responses.append(res)
        return responses

    @staticmethod
    def _merge_responses(responses: list, delimiter: str) -> list:
        """
        Merge Sub list of result into a single list

        :param responses: List of Sub List containing data from SAP table
        :type responses: list
        :param delimiter: Character separating fields
        :type delimiter: str
        :return: List of result
        :rtype: list
        """
        if not responses:
            return []

        result = []
        _res_len = len(responses[0]['DATA'])

        for i in range(_res_len):
            data_obj = {}
            for res in responses:
                data = res['DATA'][i]['WA'].split(delimiter)
                for index, field in enumerate(res['FIELDS']):
                    data_obj[field['FIELDNAME']] = data[index].strip()
            result.append(data_obj)

        return result
