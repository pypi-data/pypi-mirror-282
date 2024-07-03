
from sqlalchemy import create_engine, Table, MetaData, text, insert, values, table, column, Integer
import pandas as pd


class DataManager:
    def __init__(self, database_conf: dict):
        # conn = SqlAlchemyConnector.load("scrappy-sql-connector")
        # self.engine = create_engine('postgresql://scrappy_user:idaho777@localhost:5435/spy')
        # TODO need to check if it works the same way for bigquery and mysql
        self.engine = create_engine(
            f"{database_conf.get('database_type')}://{database_conf.get('user')}:{database_conf.get('password')}@{database_conf.get('host')}:{database_conf.get('port')}/{database_conf.get('database')}")
        self.conn = self.engine.connect()

    def select_query(self, query: str, data_type_mapping: dict = None, index_column: str = None, iterator_chunk_size: int= None, auto_convert_to_float: bool = False)-> pd.DataFrame:
        return pd.read_sql_query(query, con=self.engine, index_col=index_column, coerce_float=auto_convert_to_float, dtype=data_type_mapping, chunksize=iterator_chunk_size)

    def select_all_from(self, schema, table, columns:list = None, data_type_mapping: dict = None, index_column: str = None, iterator_chunk_size: int= None, auto_convert_to_float: bool = False)-> pd.DataFrame:
        return pd.read_sql_table(table_name=table, schema=schema, columns=columns, con=self.engine, index_col=index_column, coerce_float=auto_convert_to_float, dtype=data_type_mapping, chunksize=iterator_chunk_size)

    def _clean_data_type(self, table, data_dic):
        for col in table.columns:
            val = data_dic.get(col.name)
            if val is not None:
                data_dic[col.name] = col.type.python_type(val)

    def insert_dict_into_db(self, schema: str, table_name: str, data_dic: dict):
        try:
            _table = Table(table_name, MetaData(), schema=schema, autoload_with=self.engine)
            data_dic = self._clean_data_type(table, data_dic)
            query = insert(_table).values(data_dic)
            # self.conn.rollback()
            row_id = self.conn.execute(query).inserted_primary_key[0]
            self.conn.commit()
            return row_id
        except Exception as e:
            self.conn.rollback()
            return None

    def insert_query_into_db(self, sql_statement: str, returning: str = None, autocommit: bool = True):
        try:
            if returning is None:
                returning = 'RETURNING *'
            result = self.conn.execute(text(f'{sql_statement} {returning}')).all()
            if autocommit:
                self.conn.commit()
            return result[0][0], result[0]
        except Exception as e:
            if autocommit:
                self.conn.rollback()
            raise Exception(e)

    def update_with_query_db(self, sql_update_statement: str, returning: str = None, autocommit: bool = True):
        return self.insert_query_into_db(sql_update_statement, returning=returning, autocommit=autocommit)

    @staticmethod
    def update_df_column_by_index(df: pd.DataFrame, index: str, update_clumn, update_value) -> pd.DataFrame:
        ### UPDATE / UPDATE SPECIFIC ROW/COLUMN WHERE COLUMN  EQUALS VALUE
        df.loc[index, update_column] = update_value
        return df

    @staticmethod
    def update_df_column_by_column_search(df: pd.DataFrame, update_column: str, update_value, search_column: str, search_value: str ) -> pd.DataFrame:
        ### UPDATE / UPDATE SPECIFIC ROW/COLUMN WHERE COLUMN  EQUALS VALUE
        df.loc[df[search_column] == search_value, update_column] = update_value
        return df
        # usr_result_copy.loc[user_result.casuser_id == str(created_user_id), 'created_by_login_user_name'] = created_by_user

    @staticmethod
    def delete_df_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        return df.drop(column_name, axis=1, inplace=True)

    @staticmethod
    def delete_df_columns(df: pd.DataFrame, column_name_list: list) -> pd.DataFrame:
        return df.drop(column_name_list, axis=1, inplace=True)

    @staticmethod
    def delete_df_row(df: pd.DataFrame, row_index: int) -> pd.DataFrame:
        return df.drop(row_index, inplace=True)

    @staticmethod
    def delete_df_rows(df: pd.DataFrame, row_index_list: list) -> pd.DataFrame:
        return df.drop(row_index_list, inplace=True)

    @staticmethod
    def select_row_by_index(df: pd.DataFrame, colulmn_value) -> pd.DataFrame:
        return df.loc[colulmn_value]

    @staticmethod
    def select_row_by_column_search(df: pd.DataFrame, column_name, column_value) -> pd.DataFrame:
        return df.loc[df[column_name] == column_value]

    @staticmethod
    def delete_row_with_NaN_by_column(df: pd.DataFrame, column_name) -> pd.DataFrame:
        df = df.dropna(subset=[column_name])
        return df
