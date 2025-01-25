import pandas as pd

df_author    = pd.read_csv('dataset/author.csv')
df_award     = pd.read_csv('dataset/award.csv')
df_book      = pd.read_csv('dataset/book.csv')
df_edition   = pd.read_csv('dataset/edition.csv')
df_format    = pd.read_csv('dataset/format.csv')
df_genders   = pd.read_csv('dataset/genders.csv')
df_info      = pd.read_csv('dataset/info.csv')
df_publisher = pd.read_csv('dataset/publisher.csv')
df_ratings   = pd.read_csv('dataset/ratings.csv')
df_sales     = pd.read_csv('dataset/sales.csv')
df_series    = pd.read_csv('dataset/series.csv')
cols_new = ['book_id', 'title', 'award_name', 'year_won']
df_award.columns = cols_new
df = pd.merge(df_book, df_author, how='left', on='author_id')
df = pd.merge(df, df_award, how='left', on='book_id')
df = pd.merge(df, df_edition, how='left', on='book_id')
df = pd.merge(df, df_format, how='left', on='format_id')
df = pd.merge(df, df_info, how='left', on='book_id')
df = pd.merge(df, df_genders, how='left', on='genre_id')
df = pd.merge(df, df_publisher, how='left', on='book_id')
df = pd.merge(df, df_series, how='left', on='series_id')
df = pd.merge(df, df_sales, how='left', on='isbn')
rating_mean = df_ratings.groupby('book_id')['rating'].mean().reset_index()
rating_mean.columns = ['book_id', 'mean_rating']
df = pd.merge(df, rating_mean, how='left', on='book_id')

df.to_csv('dataset/concatData.csv', index=False)