from SAP.SAPConnectionInterface import SAPConnectionInterface


class BapiMaterialSaveData:

    def __init__(self, connection: SAPConnectionInterface):
        """
        Constructor method

        :param connection: An instance of a class implementing SAPConnectionInterface Interface
        :type connection: SAPConnectionInterface
        """
        self.connection = connection

    def run(self,
            headdata: dict = None,
            clientdata: dict = None,
            clientdatax: dict = None,
            plantdata: dict = None,
            plantdatax: dict = None,
            forecastparameters: dict = None,
            forecastparametersx: dict = None,
            planningdata: dict = None,
            planningdatax: dict = None,
            storagelocationdata: dict = None,
            storagelocationdatax: dict = None,
            valuationdata: dict = None,
            valuationdatax: dict = None,
            warehousenumberdata: dict = None,
            warehousenumberdatax: dict = None,
            salesdata: dict = None,
            salesdatax: dict = None,
            storagetypedata: dict = None,
            storagetypedatax: dict = None
            ):
        result = self.connection.call('BAPI_MATERIAL_SAVEDATA',
                                      HEADDATA=headdata,
                                      CLIENTDATA=clientdata,
                                      CLIENTDATAX=clientdatax,
                                      PLANTDATA=plantdata,
                                      PLANTDATAX=plantdatax,
                                      FORECASTPARAMETERS=forecastparameters,
                                      FORECASTPARAMETERSX=forecastparametersx,
                                      PLANNINGDATA=planningdata,
                                      PLANNINGDATAX=planningdatax,
                                      STORAGELOCATIONDATA=storagelocationdata,
                                      STORAGELOCATIONDATAX=storagelocationdatax,
                                      VALUATIONDATA=valuationdata,
                                      VALUATIONDATAX=valuationdatax,
                                      WAREHOUSENUMBERDATA=warehousenumberdata,
                                      WAREHOUSENUMBERDATAX=warehousenumberdatax,
                                      SALESDATA=salesdata,
                                      SALESDATAX=salesdatax,
                                      STORAGETYPEDATA=storagetypedata,
                                      STORAGETYPEDATAX=storagetypedatax
                                      )
        _ = self.connection.call('BAPI_TRANSACTION_COMMIT', WAIT='X')
        return result
