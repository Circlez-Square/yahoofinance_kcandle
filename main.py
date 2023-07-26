import streamlit as st,pandas as pd, numpy as  np,yfinance as yf
import datetime

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# end = st.sidebar.date_input('End Date', value=datetime.date.today())
# start = st.sidebar.date_input('Start Date', value=(datetime.date.today() - datetime.timedelta(days=120)))

ticker = st.sidebar.text_input('Ticker')
start = st.sidebar.date_input('Start Date')
end = st.sidebar.date_input('End Date')
# period=str(period), interval='1d'
period = (end - start).days
df = yf.download(ticker, start,end, interval = '1d')

def get_candlestick_plot(
        df: pd.DataFrame,
        # ma1: int,
        # ma2: int,
        ticker: str,

):

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(f'{ticker} Stock Price', 'Volume Chart'),
        row_width=[0.3, 0.7]
    )
    # df = df[df['Volume'] > 0]
    fig.add_trace(
        go.Candlestick(

            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='Candlestick chart',
            increasing_line_color='green',  # 设置涨幅的颜色为绿色
            decreasing_line_color='red'
        ),
        row=1,
        col=1,
    )

    # fig.add_trace(
    #     go.Line(x=df.index, y=df[f'{ma1}_ma'], name=f'{ma1} SMA'),
    #     row=1,
    #     col=1,
    # )
    #
    # fig.add_trace(
    #     go.Line(x=df.index, y=df[f'{ma2}_ma'], name=f'{ma2} SMA'),
    #     row=1,
    #     col=1,
    # )

    fig.add_trace(
        go.Bar(x=df.index, y=df['Volume'], name='Volume'),
        row=2,
        col=1,
    )

    fig['layout']['xaxis2']['title'] = 'Date'
    fig['layout']['yaxis']['title'] = 'Price'
    fig['layout']['yaxis2']['title'] = 'Volume'

    fig.update_xaxes(
        rangebreaks=[{'bounds': ['sat', 'mon']}],
        rangeslider_visible=False,
    )
    return fig

#    均線設計小心

with st.container():

    fig = get_candlestick_plot(df,ticker)
    st.plotly_chart(fig)
    # df['5_ma'] = df['Close'].rolling(5).mean()
    # df['10_ma'] = df['Close'].rolling(10).mean()
    # df.dropna(inplace=True)
#
# # if __name__ == '__main__':
# #     df['5_ma'] = df['Close'].rolling(5).mean()
# #     df['10_ma'] = df['Close'].rolling(10).mean()
# #     fig = get_candlestick_plot(df.tail(-30), 5, 10, '^TWII')





