import time
import yfinance as yf
import plotly.express as px


# Function to get the price from the ticker
def get_current_price(ticker):
    ticker = ticker
    ticker_data = yf.Ticker(ticker)
    price = ticker_data.history(period="1d")['Close'].iloc[-1]
    return price


# Track ticker price with time interval
def track_current_price(ticker, interval=5):
    while True:
        try:
            price = get_current_price(ticker)
            print(price)
        except Exception as e:
            print(e)
            time.sleep(interval)


# Display graph of closing prices of a ticker

def plot_close_price(ticker):
    ticker = ticker
    ticker_data = yf.Ticker(ticker).history(period='max')
    # Create a line plot
    fig = px.line(ticker_data, x=ticker_data.index, y='Close', title=f'{ticker} Closing Prices',
                  labels={'Close': 'Closing Price', 'Date': 'Date'})
    return fig.show()

# Display the moving averages of a ticker


# Price to earnings ratio (P/E Ratio)

def p_e_ratio(ticker):
    # Share price / Earnings per share

    earning_per_share =
    pe_ratio = share_price / earning_per_share



