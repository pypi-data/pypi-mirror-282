import typing as _t
import io as _io

import sqlalchemy as _sa

import fullmetalcopy.drivers as _drivers


def copy_from_csv(
    connection: _sa.engine.base.Connection,
    csv_file: _io.BytesIO,
    table_name: str,
    sep: str = ',',
    null: str = '',
    columns: _t.Optional[list[str]] = None,
    headers: bool = True,
    schema: _t.Optional[str] = None
) -> None:
    """
    Copy CSV file to PostgreSQL table.

    Example
    -------
    import sqlalchemy as sa
    from pgcopyinsert.synchronous.copy import copy_from_csv

    engine = sa.create_engine('postgresql+psycopg://user:password@host:port/dbname')
    with engine.connect() as connection:
        with open('people.csv', 'br') as csv_file:
            copy_from_csv(connection, csv_file, 'people')
        connection.commit()
    """
    driver: str = _drivers.connection_driver_name(connection)

    if driver == 'psycopg':
        import fullmetalcopy.synchronous.pg3.copycsv as _pg3_copy
        _pg3_copy.copy_from_csv(connection, csv_file, table_name, sep, null, columns, headers, schema)
    elif driver == 'psycopg2':
        import fullmetalcopy.synchronous.pg2.copycsv as _pg2_copy
        _pg2_copy.copy_from_csv(connection, csv_file, table_name, sep, null, columns, headers, schema)
    else:
        raise ValueError('driver must be psycopg or pscopg2')
    
    
