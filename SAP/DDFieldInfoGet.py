from SAP.SAPConnectionInterface import SAPConnectionInterface


class DDFieldInfoGet:
    """
    Class responsible to get table Metadat from SAP.
    It uses RFC function "DD_FIELDINFO_GET"
    """

    def __init__(self, connection: SAPConnectionInterface):
        """
        Constructor method

        :param connection: An instance of a class implementing SAPConnectionInterface Interface
        :type connection: SAPConnectionInterface
        """
        self.connection = connection

    def run(self,
            tabname: str,
            fieldname: str = None,
            langu: str = None,
            lfieldname: str = None,
            all_types: str = None,
            group_names: str = None,
            uclen: bytes = None,
            do_not_write: str = None
            ) -> dict:
        """
        RFC DD_FIELDINFO_GET function to fetch metadata of the table in SAP

        :param tabname: Table Name
        :type tabname: str
        :param fieldname: Use Parameter LFIELDNAME Instead
        :type fieldname: str
        :param langu: Language by default its EN(english)
        :type langu: str
        :param lfieldname: If Filled, only Field details with this Name will be returned
        :type lfieldname: str
        :param all_types: Take all Types into Consideration
        :type all_types: str
        :param group_names: Take Named Includes into Consideration
        :type group_names: str
        :param uclen: Unicode length with which runtime object was generated
        :type uclen: bytes
        :param do_not_write: Write
        :type do_not_write: str
        :return: Returns Table and Field Information
        :rtype: dict
        """

        if fieldname is None:
            fieldname = ''
        if langu is None:
            langu = 'EN'
        if lfieldname is None:
            lfieldname = ''
        if all_types is None:
            all_types = ''
        if group_names is None:
            group_names = ''
        if uclen is None:
            uclen = bytes(0)
        if do_not_write is None:
            do_not_write = ''

        return self.connection.call('DDIF_FIELDINFO_GET',
                                    TABNAME=tabname,
                                    FIELDNAME=fieldname,
                                    LANGU=langu,
                                    LFIELDNAME=lfieldname,
                                    ALL_TYPES=all_types,
                                    GROUP_NAMES=group_names,
                                    UCLEN=uclen,
                                    DO_NOT_WRITE=do_not_write)
