# 檢查缺失值
df.fillna(method='ffill', inplace=True)

# 計算技術指標
import talib

df['MA20'] = talib.SMA(df['close'], timeperiod=20)
df['RSI'] = talib.RSI(df['close'], timeperiod=14)
df['MACD'], _, _ = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)