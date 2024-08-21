from datetime import datetime

from SAPTable.MasterTable import MasterTable
from SAPTable.SlaveTable import SlaveTable


class MasterSlaveFetch:
    """
    Class controlling Master and Slave Table
    """
    def __init__(self, master: MasterTable, slaves: list[SlaveTable]):
        """

        :param master: Master Table Object
        :type master: MasterTable
        :param slaves: List of Slave Table Object
        :type slaves: list[SlaveTable]
        """
        self.master = master
        self.slaves = slaves

    def run(self, query_timestamp: datetime):
        master_res = self.master.get_data(query_timestamp)
        slave_res = []
        for slave in self.slaves:
            slave_res.append(slave.get_data(master_res['DATA']))
        return {'MASTER': master_res, 'SLAVES': slave_res}



