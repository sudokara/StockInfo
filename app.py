import pandas as pd
import yfinance as yf
import streamlit as st
from dataFunctions import *

@st.experimental_memo(
    ttl=600,
    max_entries=10
)
def get_ticker_object(ticker_symbol: str):
    ticker_data = yf.Ticker(ticker_symbol)
    return None if ticker_data.info['regularMarketPrice'] is None else ticker_data


@st.experimental_memo (
    ttl=600,
    max_entries=10
)
def get_ticker_from_name(name, ticker_df: pd.DataFrame)->str:
    if ticker_df_raw is not None:
        return ticker_df_raw.index[ticker_df_raw['Name'] == name].tolist()[0]
    else:
        return ""


def show_results(options: dict):
    st.markdown("***")
    if options.get('ticker') is None:
        if ticker_df_raw is not None:
            options['ticker'] = get_ticker_from_name(options['name'], ticker_df_raw)
            if not options:
                st.error(f"Could not get ticker symbol for {options['name']}")
                return
        else:
            st.error("Empty data frame")
            return
    ticker_data = get_ticker_object(options['ticker'])
    if ticker_data is None:
        st.error("Could not find data for ticker symbol \"{}\". It probably does not exist.".format(options['ticker']))
        return

    functions = {'Company Info': show_company_info, 'Open': show_open_data, 'High': show_high_data, 'Low': show_low_data, 'Close': show_close_data, 'Volume': show_volume_data, 'Dividends': show_dividends_data, 'Recommendations': show_recommendations_data}
    
    showed_results = False
    company_df = ticker_data.history(period='1d', start='2010-01-01')
    for key in options.keys():
        if key != 'ticker' and key != 'name':
            showed_results = True
            if key in ['Company Info', 'Recommendations']:
                functions[key](options['ticker'], ticker_data)
            else:
                functions[key](options['ticker'], company_df)
    
    if not showed_results:
        st.warning("Please select at least one option to display")


def show_display_options()->dict:
    options = ['Company Info', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Recommendations']
    chosen = st.multiselect("What do you want to see?", options=options, default=options)
    chosen_dict = {item:1 for item in chosen}
    return chosen_dict


def search_by_ticker():
    display_options = {}
    display_options['ticker'] = st.selectbox("Company Ticker", options=ticker_options)
    display_options.update(show_display_options())
    if (st.button("Go")):
        show_results(options=display_options)


def search_by_name():
    display_options = {}
    display_options['name'] = st.selectbox("Company Name", options=name_options)
    display_options.update(show_display_options())
    if (st.button("Go")):
        show_results(options=display_options)


@st.experimental_singleton
def generate_options(ticker_df_raw):
    ticker_options = []
    name_options = []
    try:
        ticker_options = ticker_df_raw.index.values.tolist()
        name_options = list(ticker_df_raw.Name)
    except Exception as e:
        st.error("Could not generate options")
        return [], []
    return ticker_options, name_options


@st.experimental_singleton
def get_dataframe(path):
    try:
        ticker_df_raw = pd.read_csv("./tickers/nasdaq_screener_1670824351837.csv", index_col=0)
        return ticker_df_raw
    except Exception as e:
        return None


if __name__ == "__main__":
    st.set_page_config(page_title='NASDAQ Stock Info', page_icon="📈")

    path_to_csv = "./tickers/nasdaq_screener_1670824351837.csv"
    ticker_df_raw = get_dataframe(path_to_csv)
    if ticker_df_raw is None:
        st.error("Could not read data file")
        st.stop()
    ticker_options, name_options = generate_options(ticker_df_raw)
    if not ticker_options or not name_options:
        st.error("Could not resolve names or ticker symbols")
        st.stop()

    st.title("Stock Info and Price Tracking")
    st.markdown("***")

    with st.container():
        st.header("Search for a company on NASDAQ")
        search_method = st.radio("How do you want to search?", ("Ticker Symbol", "Company Name"))
        if search_method == 'Ticker Symbol':
            search_by_ticker()
        else:
            search_by_name()
    
    st.markdown("***")
    expander = st.expander("Tips💡")
    expander.write("""You can change theme in `Menu->Settings->Theme`.  
    You can move around and zoom in on graphs. To return to the default position, double click anywhere in the graph.  
    If you face issues, try clearing cache by pressing `c` or through the menu.  
    If something isn't working, you can tell me on [GitHub](https://github.com/sudokara/StockInfo/issues)  """)
    st.markdown("""Check out the source code on [GitHub](https://github.com/sudokara/StockInfo)!  
    Source for List of Tickers and Names : [Nasdaq](https://www.nasdaq.com/market-activity/stocks/screener)  
    Data is from [Yahoo!Finance](https://finance.yahoo.com/) using the [yfinance](https://pypi.org/project/yfinance/) library""")