import logging
import pandas as pd
import kusto_tools.k_io.kusto_io as kio


class KustoHandler(logging.Handler):
    def __init__(self, cluster:str, database:str, tablename:str, attributes_list:list, linked_service_name:str=None) -> None:
        """Constructor
        Args:
            cluster: kusto cluster name
            database: kusto database
            table (string): table name
            attributes_list: The list of attributes that maps to the schema of the table.
            linked_service_name: linked service for authenticating using Managed Identity
        """
        super().__init__()
        
        self.cluster = cluster
        self.database = database
        self.tablename = tablename
        self.linked_service_name = linked_service_name
        self.db_conn = kio.KustoIngest(kusto_ingest_cluster=self.cluster, kusto_database=self.database, linked_service_name=self.linked_service_name)
        self.attributes = attributes_list

        self.log_rows_list = []
        return

    def emit(self, record):
        self.format(record)
        record_values = [record.__dict__[k] for k in self.attributes]
        self.log_rows_list.append(record_values)
        #print(self.log_rows_list)
        
    def flush_writes(self):
        log_df = pd.DataFrame(self.log_rows_list, columns=self.attributes)
        self.db_conn.write_pandas_to_table(log_df, self.tablename)
        print("\n {0} log records written to: cluster('{1}').database('{2}').{3}"\
            .format(len(self.log_rows_list), self.cluster, self.database, self.tablename))

    def flush(self):
        pass
        #self.flush_writes()

    def close(self):
        super().close()



