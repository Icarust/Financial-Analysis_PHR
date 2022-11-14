import pandas as pd
def read_data(ticker):
    df = pd.read_csv(ticker, thousands=",")    #thousand thay the bang dau ","
    
    # Đổi tên các Columns
    df.columns = ['Date','Close','Open','High','Low','Volume','%Change']

    # Loại bỏ (Drop) cột "%Change"
    df.drop('%Change', axis=1, inplace=True)

    # Quy ước Index là Columns "Date"
    df = df.set_index("Date")

    # Format lại Date
    df.index = pd.to_datetime(df.index)

    # Sắp xếp (Sort) Date từ quá khứ đến hiện tại (Oldest to Newest)
    df.sort_values(by="Date",ascending=True,inplace=True)

    return df




