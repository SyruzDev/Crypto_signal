import React, { useState, useEffect } from 'react'
import { TrendingUp, TrendingDown, AlertCircle } from 'lucide-react'

interface TradingSignals {
  buy_signals: boolean[]
  sell_signals: boolean[]
}

function App() {
  const [signals, setSignals] = useState<TradingSignals | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchTradingSignals() {
      try {
        const response = await fetch('http://localhost:5000/analyze/BTCUSDT')
        const data = await response.json()
        
        if (data.status === 'success') {
          setSignals(data.signals)
        } else {
          setError(data.error || 'Unknown error occurred')
        }
        setLoading(false)
      } catch (err) {
        setError('Failed to fetch trading signals')
        setLoading(false)
      }
    }

    fetchTradingSignals()
    const interval = setInterval(fetchTradingSignals, 60000) // Refresh every minute
    return () => clearInterval(interval)
  }, [])

  const renderSignalStatus = () => {
    if (loading) return <p>Loading trading signals...</p>
    if (error) return <p className="text-red-500">{error}</p>

    return (
      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">Trading Signals</h2>
        <div className="flex space-x-4">
          <div className="flex-1 bg-green-50 p-4 rounded">
            <h3 className="flex items-center text-green-600">
              <TrendingUp className="mr-2" /> Buy Signals
            </h3>
            <p>{signals?.buy_signals.filter(Boolean).length || 0} Active</p>
          </div>
          <div className="flex-1 bg-red-50 p-4 rounded">
            <h3 className="flex items-center text-red-600">
              <TrendingDown className="mr-2" /> Sell Signals
            </h3>
            <p>{signals?.sell_signals.filter(Boolean).length || 0} Active</p>
          </div>
        </div>
        {(!signals?.buy_signals.some(Boolean) && !signals?.sell_signals.some(Boolean)) && (
          <div className="mt-4 text-yellow-600 flex items-center">
            <AlertCircle className="mr-2" />
            No significant trading signals detected
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          Crypto Trading Signal Monitor
        </h1>
        {renderSignalStatus()}
      </div>
    </div>
  )
}

export default App
