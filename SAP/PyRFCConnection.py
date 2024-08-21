from abc import ABC

import pyrfc

from SAP.SAPConnectionInterface import SAPConnectionInterface


class PyRFCConnection(SAPConnectionInterface, ABC):
    """
    A Python Package containing modules to call SAP BAPI
    functions to communicate with SAP

    :param user: SAP Logon ID
    :type user: str
    :param password: SAP Logon Password
    :type password: str
    :param sysid: SAP System ID Example "DEV"
    :type sysid: str
    :param sysnr: SAP System Number Example "00"
    :type sysnr: str
    :param group: SAP group ip Example "192.168.200.19"
    :type group: str
    :param ashost: Host name Example "192.168.200.19"
    :type ashost: str
    :param saprouter: SAP Router Example "/H/43.242.212.21/S/3299"
    :type saprouter: str
    :param client: SAP client ID Example "500"
    :type client: str
    """

    def __init__(self,
                 user: str,
                 password: str,
                 sysid: str,
                 sysnr: str,
                 group: str,
                 ashost: str,
                 saprouter: str,
                 client: str) -> None:
        """
        Constructor method

        :param user: SAP Logon ID
        :type user: str
        :param password: SAP Logon Password
        :type password: str
        :param sysid: SAP System ID Example "DEV"
        :type sysid: str
        :param sysnr: SAP System Number Example "00"
        :type sysnr: str
        :param group: SAP group ip Example "192.168.200.19"
        :type group: str
        :param ashost: Host name Example "192.168.200.19"
        :type ashost: str
        :param saprouter: SAP Router Example "/H/43.242.212.21/S/3299"
        :type saprouter: str
        :param client: SAP client ID Example "500"
        :type client: str
        """
        self.connection = pyrfc.Connection(
            user=user,
            passwd=password,
            sysid=sysid,
            sysnr=sysnr,
            group=group,
            ashost=ashost,
            saprouter=saprouter,
            client=client
        )

    def call(self, function_name: str, **kwargs) -> dict:
        """
        Executes a SAP function
        :param function_name: Name of the SAP function
        :type function_name: str
        :param kwargs:
        :return: Dictionary containing data from SAP table
        :rtype: dict
        """
        return self.connection.call(function_name, **kwargs)
