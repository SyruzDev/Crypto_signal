from flask import Flask, jsonify
from flask_cors import CORS
from binance_client import BinanceService
from trading_signals import TradingSignalAnalyzer
from telegram_alerts import TelegramAlertService

app = Flask(__name__)
CORS(app)

@app.route('/analyze/<symbol>')
def analyze_crypto(symbol='BTCUSDT'):
    try:
        # Fetch historical prices
        binance_service = BinanceService()
        prices = binance_service.get_historical_prices(symbol)

        # Generate trading signals
        signal_analyzer = TradingSignalAnalyzer(prices)
        signals = signal_analyzer.generate_signals()

        # Send Telegram alerts
        telegram_service = TelegramAlertService()
        telegram_service.send_trading_alert(signals)

        return jsonify({
            'symbol': symbol,
            'signals': signals,
            'status': 'success'
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
