import streamlit as st
import yfinance as yf
import pandas as pd


@st.experimental_memo(
    ttl=300,
    max_entries=10
)
def show_company_info(ticker_symbol: str, _ticker_data: yf.Ticker):
    st.markdown("***")
    st.subheader("Company Info")
    with st.spinner("Fetching Company Info..."):
        col1, col2 = st.columns(2)
        with col2:
            st.markdown(
                f"![{_ticker_data.info.get('shortName', 'Company')} Logo]({_ticker_data.info.get('logo_url', 'Logo URL')})")
        with col1:
            keys = ['symbol', 'longName', 'country',
                    'sector', 'industry', 'website']
            values = [_ticker_data.info.get(x, 'Unknown')
                      for x in keys]  # faster for some reason
            st.write(f"""Ticker Symbol: {values[0]}  
            Company Name: {values[1]}  
            Country: {values[2]}  
            Sector: {values[3]}  
            Industry: {values[4]}  
            Website: {values[5]}""")
        expander = st.expander(
            f"Details about {_ticker_data.info.get('shortName', 'Company')}")
        expander.write(_ticker_data.info.get(
            'longBusinessSummary', 'Unspecified'))
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_open_data(ticker_symbol: str, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Open over time")
        st.line_chart(_company_df.Open)
    
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_high_data(ticker_symbol: str, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("High over time")
        st.line_chart(_company_df.High)
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_low_data(ticker_symbol: str, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Low over time")
        st.line_chart(_company_df.Low)
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_close_data(ticker_symbol, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Closing Price(USD) over time")
        st.line_chart(_company_df.Close)
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_volume_data(ticker_symbol, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Volume over time")
        st.line_chart(_company_df.Volume)
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_dividends_data(ticker_symbol, _company_df: pd.DataFrame):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Dividends over time")
        st.line_chart(_company_df.Dividends)
    return


@st.experimental_memo(
    ttl=300,
    max_entries=5
)
def show_recommendations_data(ticker_symbol, _ticker_data: yf.Ticker):
    st.markdown("***")
    with st.spinner("Loading graph..."):
        st.write("Recommendations: ")
        st.dataframe(_ticker_data.recommendations)
    return
