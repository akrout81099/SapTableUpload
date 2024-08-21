import pyrfc
from abc import ABC, abstractmethod


class SAPConnectionInterface(ABC):
    """

    """

    @abstractmethod
    def call(self, function_name: str, **kwargs) -> dict:
        """
        Executes a SAP function
        :param function_name: Name of the SAP function
        :type function_name: str
        :param kwargs:
        :return: Dictionary containing data from SAP table
        :rtype: dict
        """