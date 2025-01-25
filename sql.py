import psycopg2
import csv

conn_params = {
    'dbname': 'hackday-bookstore-cds',
    'user': 'alunocds',
    'password': 'hackday2025',
    'host': '34.55.27.249',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful")

    cur = conn.cursor()

    sql = """
    create temporary table award_att as
    select
    "BookID" as "book_id",
    "Title" ,
    "Award Name" ,
    "Year Won"
    from award a;
    create temporary table sales_att as
    select
    case
    when s.isbn is null then split_part(sale_date, ',', 1)
    else
    sale_date
    end as sale_date,
    case
    when s.isbn is null then split_part(sale_date, ',', 2)
    else
    isbn
    end as isbn,
    case
    when s.isbn is null then split_part(sale_date, '"', 2)
    else
    discount
    end as discount,
    case
    when s.isbn is null then split_part(sale_date, ',', 5)
    else
    item_id
    end as item_id,
    case
    when s.isbn is null then split_part(sale_date, ',', 6)
    else
    order_id
    end as order_id
    from sales s;
    select
    b.book_id ,
    b.title ,
    b.author_id ,
    a."Award Name",
    a."Year Won",
    a2.first_name,
    a2.last_name ,
    a2.birthday ,
    a2.country_residence ,
    a2.hrs_writing_day,
    r.rating ,
    r.review_id ,
    r.reviewer_id,
    i.genre_id ,
    g.genre_desc ,
    i.series_id ,
    s.series_name,
    i.volume_number,
    e.format_id ,
    f.format_desc ,
    e.isbn ,
    e.pages ,
    e.price ,
    e.print_run_size_k ,
    e.pub_id ,
    e.publication_date,
    sa.sale_date,
    sa.discount,
    sa.item_id,
    sa.order_id
    from book b left join award_att a on (b.book_id = a.book_id)
    left join author a2 on (b.author_id = a2.author_id)
    left join ratings r on (b.book_id = r.book_id )
    left join info i on (b.book_id = i.book_id)
    left join series s on (i.series_id = s.series_id)
    left join genders g on (i.genre_id = g.genre_id)
    left join edition e on (b.book_id = e.book_id)
    left join "format" f on (e.format_id = f.format_id)
    left join sales_att sa on (e.isbn = sa.isbn);
    """

    cur.execute(sql)
    rows = cur.fetchall()

    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([desc[0] for desc in cur.description])
        csvwriter.writerows(rows)

except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed")
