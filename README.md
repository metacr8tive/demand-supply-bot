# Demand and Supply Trading Bot

A sophisticated Forex and Cryptocurrency trading bot that leverages demand/supply zone analysis and chart pattern recognition for intelligent trading decisions.

## Features

- **Demand & Supply Zone Detection**: Identifies key support and resistance zones based on demand/supply principles
- **Chart Pattern Recognition**: Detects technical patterns (Head & Shoulders, Triangles, Flags, etc.)
- **Multi-Exchange Support**: Trade on Bybit (Cryptocurrency) and MetaTrader 5 (Forex)
- **Risk Management**: Integrated stop-loss and take-profit mechanisms
- **Backtesting Framework**: Test strategies on historical data before live trading
- **Real-time Alerts**: Get notified of trading opportunities
- **Technical Analysis**: Multiple indicators (RSI, MACD, Moving Averages, etc.)

## System Requirements

- Python 3.8 or higher
- MetaTrader 5 installed (for Forex trading)
- Bybit account with API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/metacr8tive/demand-supply-bot.git
cd demand-supply-bot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your API keys:
```bash
cp .env.example .env
# Edit .env with your API credentials
```

## Configuration

Edit `config.py` with your trading parameters:

```python
# Bybit API Keys
BYBIT_API_KEY = 'your_api_key'
BYBIT_API_SECRET = 'your_api_secret'

# MetaTrader 5 Credentials
MT5_LOGIN = 'your_mt5_login'
MT5_PASSWORD = 'your_mt5_password'

# Trading Parameters
TRADING_SYMBOL = 'BTCUSD'
TRADE_AMOUNT = 0.01
TAKE_PROFIT = 50.0
STOP_LOSS = 50.0
```

## Usage

Start the bot:
```bash
python main.py
```

## Project Structure

```
demand-supply-bot/
├── main.py                 # Main entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── modules/
│   ├── technical_analysis.py    # TA indicators & patterns
│   ├── bybit_exchange.py        # Bybit API integration
│   ├── mt5_trader.py            # MetaTrader 5 integration
│   ├── strategy.py              # Trading strategy logic
│   └── risk_management.py       # Risk management rules
├── backtesting/
│   └── backtest.py              # Backtesting framework
└── logs/
    └── trading.log              # Trading activity logs
```

## Trading Strategy

The bot uses a multi-layered approach:

1. **Demand/Supply Zone Identification**: Finds key price levels where demand/supply imbalances occur
2. **Chart Pattern Recognition**: Detects breakout and reversal patterns
3. **Confirmation Signals**: Uses technical indicators for entry confirmation
4. **Risk Management**: Applies stop-loss and take-profit levels
5. **Position Management**: Monitors and manages open positions

## Backtesting

Test your strategies before live trading:
```bash
python backtesting/backtest.py
```

## Risk Disclaimer

⚠️ **IMPORTANT**: Trading forex and cryptocurrency involves substantial risk. This bot is provided for educational purposes. Always:
- Start with a demo account
- Use proper risk management
- Never invest more than you can afford to lose
- Test thoroughly before live trading

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue on GitHub or contact the maintainer.

---

**Disclaimer**: This bot is provided as-is. Use at your own risk. Past performance is not indicative of future results.