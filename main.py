import json
import time
from datetime import datetime

import pyrfc

from SAP.BapiMaterialSaveData import BapiMaterialSaveData
from SAP.DDFieldInfoGet import DDFieldInfoGet
from SAP.EMGetNumberOfEntries import EMGetNumberOfEntries
from SAP.PyRFCConnection import PyRFCConnection
from SAP.RFCReadLongTable import RFCReadLongTable
from SAP.RFCReadTable import RFCReadTable
from SAPTable.MasterSlaveFetch import MasterSlaveFetch
from SAPTable.MasterTable import MasterTable
from SAPTable.SlaveTable import SlaveTable

connection_params = {
    'user': 'AUTOMI1',
    'password': 'Sap@2200',
    'sysid': 'DEV',
    'sysnr': '00',
    'group': '192.168.200.19',
    'ashost': '192.168.200.19',
    'saprouter': '/H/43.242.212.21/S/3299',
    'client': '500'
}

## PRODUCTION
config = {
    "user": 'AUTOMI1',
    "password": 'Sap@2200',
    "sysid": 'ECP',
    "sysnr": '00',
    "group": '192.168.200.20',
    "ashost": '192.168.200.20',
    "saprouter": '/H/43.242.212.21/S/3299',
    "client": '100'
}
t_start = time.time()
sap_connection = PyRFCConnection(**connection_params)

eban = MasterTable(sap_connection, 'EBAN', fields=None,
                   query_field={'DATE': 'ERDAT'})

cdpos = SlaveTable(sap_connection, 'CDPOS', fields=None, master_table='EBAN',
                   field_relations=[{'MASTER': 'BANFN', 'SLAVE': 'OBJECTID'}])

cdhdr = SlaveTable(sap_connection, 'CDHDR', fields=None, master_table='EBAN',
                   field_relations=[{'MASTER': 'BANFN', 'SLAVE': 'OBJECTID'}])

msf = MasterSlaveFetch(eban, [cdpos, cdhdr])

json.dump(msf.run(datetime.strptime('20240807 000000', '%Y%m%d %H%M%S')), open('test.json', 'w'), indent=4)

t_end = time.time()
print(t_end - t_start)
