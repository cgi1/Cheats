import dask.dataframe as dd


        approx_MB_per_chunk = 256
        divisions = list('abcdefghijklmnopqrstuvwz')

        bytes_per_chunk = approx_MB_per_chunk * 2 ** 20
        print("Memory consumptions will be around %.2f GB; %.0f MB per chunk on %.0f chunks." % (
            (approx_MB_per_chunk * len(divisions))/1024, approx_MB_per_chunk, len(divisions)
        ))
        df = dd.read_sql_table(table=tbl_name,
                               uri=self.db.get_create_engine_string(), # This returns an sqlalchemy create engine scheme
                               index_col='symbol',
                               divisions=divisions,
                               columns=columns,
                               bytes_per_chunk=bytes_per_chunk)

        print("Finished read_sql_table... (%s)" % tbl_name)
        df = df.set_index('timestamp')  # set the index to make some operations fast
        print("Finished set_index... (%s)" % 'timestamp')
