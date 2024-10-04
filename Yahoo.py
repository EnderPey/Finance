import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
    


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.history = yf.Ticker(ticker).history(period='5y')

    def display(self):
        df = self.history
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])
        fig.update_layout(margin=dict(l=20, r=20, t=60, b=20),
                      height=600, width=800,
                      title=f'{self.ticker} Stock Price Over Time',
                      xaxis_title='Date',
                        yaxis_title='Price',
                        xaxis_rangeslider_visible=False,
                      )


        fig.show()

    def __str__(self) -> str:
        return f'{self.ticker}'