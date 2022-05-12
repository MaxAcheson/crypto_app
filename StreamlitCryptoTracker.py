# Usual Imports
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Plotting and UI
import streamlit as st

# Data Collection
import pandas_datareader.data as pdr
import yfinance as yf

# Settings
yf.pdr_override()
st.set_page_config(layout="wide")

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

# Functions
# ---------

def SMA(values, n):
    """
    Return simple moving average of `values`, at
    each step taking into account `n` previous values.
    """
    return pd.Series(values).rolling(n).mean()

st.markdown('''# **Cool Kids Crypto Tracker**''')

st.header('**Live Prices**')

# Load market data from Binance API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('ETHBUSD') )
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('BTCBUSD') )
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('MATICBUSD') )
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('LRCBUSD') )
col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD') )
col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('LINKBUSD') )

# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]

# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)

# Select the priceChangePercent column
col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'
col3_percent = f'{float(col3_df.priceChangePercent)}%'
col4_percent = f'{float(col4_df.priceChangePercent)}%'
col5_percent = f'{float(col5_df.priceChangePercent)}%'
col6_percent = f'{float(col6_df.priceChangePercent)}%'

# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col1.metric(col4_selection, col4_price, col4_percent)
col2.metric(col5_selection, col5_price, col5_percent)
col3.metric(col6_selection, col6_price, col6_percent)


st.markdown("---")
st.header('**Plot Cryptocurrency**')

# Create crypto dictionary
currencies_dict = {
    "Ethereum" : "ETH-USD",
    "Polygon" : "MATIC-USD",
    "Bitcoin" : "BTC-USD",
    "Loopring" : "LRC-USD",
    "Cardano" : "ADA-USD",
    "Chainlink" : "LINK-USD",

}

# Select crypto to analyze
crypto = st.selectbox("Select Currency", currencies_dict.keys())


# Obtain crypto pricing from Pandas-Datareader
start_date = ('2015-5-13')
end_date = ('2022-5-12')
stock_df = pdr.get_data_yahoo(
    currencies_dict[crypto],
    start_date,
    end_date
)

stock_df = stock_df.drop(columns=['Close'])
stock_df = stock_df.rename(columns={'Adj Close' : 'Close'})

class SmaCross(Strategy):
    n1=10
    n2=20
    
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)
        
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.position.close()
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.position.close()
            self.sell()
            
bt = Backtest(stock_df, SmaCross, commission=.002,
             exclusive_orders=True)
stats = bt.run()
fig = bt.plot(open_browser=False)

st.bokeh_chart(fig)
