# StockInfo

## Description:
An app for data about various publicly listed companies. Currently supports NASDAQ only, more to be added.  
Made in python using [streamlit](https://streamlit.io/).  
Data from [Yahoo! Finance](https://finance.yahoo.com/) API using the [yfinance](https://pypi.org/project/yfinance/) library.  
Ticker data is from `nasdaq_screener_1670824351837.csv` file, downloaded from [NASDAQ](https://www.nasdaq.com/market-activity/stocks/screener).  
The `tickers` folder contains other unused files, which may be supported later on.  
The app uses two types of caching provided by streamlit, singleton(for single shared object) and memo(essentially memoization) to improve performance and reduce recomputation.  The time to live is 5 minutes for functions mentioned in `dataFunctions.py` (the outputs) and 10 minutes for all other cached data.   
- [ ] TODO: Explain this better  

## Running:
It is recommended to run locally since the instance hosted on streamlit is quite slow due to resource sharing and is sometimes unusable   

Run locally:  
1. Clone this repo with `git clone https://github.com/sudokara/StockInfo.git`  
2. Change to the directory with `cd StockInfo`  
3. Create a virtual environment if necessary  
4. Install requirements with `pip install -r requirements.txt`  
5. Run the app with `streamlit run app.py`  
6. If you face an error with the previous command, then pip is installing libraries outside your `PATH`. Use `python -m streamlit app.py` instead or add the necessary directory to `PATH`  

Or(not representative of stability and performance)  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sudokara-stockinfo-app-sx18xf.streamlit.app/) 

Known Bugs:  
- Loading data seems to be fast for famous companies like Apple, Microsoft and American Airlines but is painfully slow for obscure companies  
- Two horizontal line breaks separating input from the first output  

Check out todo.md for future plans  