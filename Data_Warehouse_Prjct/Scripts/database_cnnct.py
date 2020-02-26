import psycopg2


def data_loader(file_name)
    conn = psycopg2.connect(host="localhost", database="Sales_Data", user="postgres", password="elyon100")

    cur = conn.cursor()


    with open('file_name', 'r') as f:
        next(f)
        cur.copy_from(f, 'public.SalesData', sep=',')
        conn.commit()

        cur.close()


if __name__ == "__main__":
    file_name = SalesData_17022020.csv
    data_loader(file_name)
