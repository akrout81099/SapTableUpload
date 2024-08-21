from SAP.SAPConnectionInterface import SAPConnectionInterface


class RFCReadTable:
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
            delimiter: str = None,
            no_data: str = None,
            row_skips: int = None,
            row_count: int = None,
            fields: list = None,
            options: list = None
            ) -> dict:
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
        :return: Dictionary containing data from SAP table
        :rtype: dict
        """
        if delimiter is None:
            delimiter = '^'
        if no_data is None:
            no_data = ''
        if row_skips is None:
            row_skips = 0
        if row_count is None:
            row_count = 0
        if fields is None:
            fields = []
        if options is None:
            options = []

        fields_data = self.connection.call('RFC_READ_TABLE',
                                           QUERY_TABLE=query_table,
                                           NO_DATA='X',
                                           FIELDS=fields)['FIELDS']

        if len(no_data) <= 0:
            _sum = 0
            _delimiter_offset = 0
            for field_data in fields_data:
                length = int(field_data['LENGTH'])
                _sum = _sum + length
                _delimiter_offset = _delimiter_offset + 1

            if _sum + _delimiter_offset > 512:
                raise ValueError(f"Total length ({_sum + _delimiter_offset}) (field length ({_sum}) and delimiter "
                                 f"length ({_delimiter_offset})) exceeds the maximum allowed (512). "
                                 f"Reduce the number of fields.")

        res = self.connection.call('RFC_READ_TABLE',
                                   QUERY_TABLE=query_table,
                                   DELIMITER=delimiter,
                                   NO_DATA=no_data,
                                   ROWSKIPS=row_skips,
                                   ROWCOUNT=row_count,
                                   FIELDS=fields,
                                   OPTIONS=options)

        result = self._merge_responses(responses=res['DATA'], delimiter=delimiter, fields=res['FIELDS'])
        return {'DATA': result,
                'FIELDS': fields_data,
                'OPTIONS': options}

    @staticmethod
    def _merge_responses(responses: list, delimiter: str, fields: list) -> list:
        """
        Merge string result into an object

        :param responses: List of Sub List containing data from SAP table
        :type responses: list
        :param delimiter: Character separating fields
        :type delimiter: str
        :param fields: List of Field Name to be fetched
        :type fields: list
        :return: List of result
        :rtype: list
        """
        result = []
        for i, item in enumerate(responses):
            data = item['WA'].split(delimiter)
            data_obj = {}
            for j,_f in enumerate(fields):
                data_obj[_f['FIELDNAME']] = data[j].strip()
            result.append(data_obj)
        return result
