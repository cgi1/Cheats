import dask.dataframe as dd

        approx_MB_per_chunk = 256
        divisions = list('abcdefghijklmnopqrstuvwz')

        bytes_per_chunk = approx_MB_per_chunk * 2 ** 20
        print("Memory consumbtion will be around (%s GB; %s MB per chunk on %s chunks)" % (
            (approx_MB_per_chunk * len(divisions)), approx_MB_per_chunk, len(divisions)
        ))
        df = dd.read_sql_table(table=tbl_name,
                               uri=self.db.get_create_engine_string(), # This returns an sqlalchemy create engine scheme
                               index_col='symbol',
                               divisions=divisions,
                               columns=columns,
                               bytes_per_chunk=bytes_per_chunk)
