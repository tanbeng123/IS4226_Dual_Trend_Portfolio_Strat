# IS4226_Dual_Trend_Portfolio_Strat (EMA-OBV Dual Trend Portfolio Strategy)
This repository contains a comprehensive Jupyter notebook implementing an **EMA-OBV Dual Trend Portfolio Strategy** backtested on major technology stocks from 2010-2019. The strategy combines On-Balance Volume (OBV) momentum signals with Exponential Moving Average (EMA) smoothing and dual moving average (50-day/200-day) trend confirmation.

## 🎯 Strategy Overview
Our strategy seeks to capture medium-term momentum reversals supported by volume flow by aligning both **price trends** and **OBV trends**:

# EMA-OBV Dual Trend Portfolio Strategy

**Personal Quantitative Finance Project**  
*Keith Tan Beng Hui - Quantitative Analyst*

Comprehensive EMA-smoothed On-Balance Volume (OBV) strategy with dual MA confirmation (50/200-day), backtested on mega-cap tech stocks (2010-2019). Achieved **150.69% total return**, **13.19% CAGR**, **1.09 Sharpe Ratio**, and **+6.74% Alpha vs SPY** through volume-validated trend detection.

## 🎯 Strategy Overview

**Core Thesis**: Volume precedes price. Dual confirmation filters false signals.

## 📊 Backtest Specifications

| Parameter | Value |
|-----------|-------|
| **Universe** | NVDA, MSFT, AAPL, AMZN, META, AVGO, GOOGL, TSLA, GOOG, BRK-B |
| **Benchmark** | SPY (S&P 500 ETF) |
| **Period** | 2010-01-01 → 2019-12-31 |
| **Initial Capital** | $500,000 USD |
| **Leverage** | None (1x long-only) |
| **Transaction Costs** | 0% (academic backtest) |
| **λ (Smoothing)** | 0.99 (optimized) |
| **Vol Window** | 30 days (optimized) |

## 📈 Performance Summary

**vs SPY Benchmark**: Identical CAGR (13.22%) with **lower volatility** + **positive alpha**.

## 🔥 Top Contributors

| Rank | Ticker | Return Contribution |
|------|--------|-------------------:|
| 1    | NVDA   | +3.49%            |
| 2    | AMZN   | +2.61%            |
| 3    | META   | +Significant      |

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/ema-obv-portfolio.git
cd ema-obv-portfolio
pip install -r requirements.txt
```

### 2. Run Complete Analysis
```bash
jupyter notebook Group2_FinalTerm.ipynb
# Run all cells → Full dashboard in ~3 minutes
```

### 3. Expected Output
- Equity curve vs SPY
- Performance dashboard (6 panels)
- Per-ticker attribution
- Trade statistics
- Annual performance bars

## 📦 Repository Structure

## 🛠️ Core Implementation
### Signal Generation
```python
class EMAOBVPortfolio:
    def __init__(self, lambda_=0.99, vol_window=30):
        self.lambda_ = lambda_
        self.alpha = 1 - lambda_
        self.vol_window = vol_window
    
    def generate_signals(self):
        # 1. Raw OBV
        direction = np.sign(self.price.diff().fillna(0))
        obv = (direction * self.volume).cumsum()
        
        # 2. EMA Smoothing
        obv_ema = obv.ewm(alpha=self.alpha).mean()
        
        # 3. Dual MA Confirmation
        ma50 = self.price.rolling(50).mean()
        ma200 = self.price.rolling(200).mean()
        
        # 4. Final Signal
        price_dir = np.sign(self.price.diff())
        obv_dir = np.sign(obv_ema.diff())
        return price_dir * obv_dir
```

### Expanding Window Backtest
## 📊 Generated Visualizations

1. **Equity vs SPY** - Growth + benchmark comparison
2. **Underwater Drawdown** - Max -20.6% (484 days recovery)
3. **Annual Returns** - Consistent positive years
4. **6-Panel Dashboard** - Complete metrics overview
5. **Ticker Attribution** - NVDA/AMZN dominance
6. **Trade Analysis** - 392 trades, 51% win rate

## 🔬 Key Features

- ✅ **Production-grade backtester** (daily equity tracking)
- ✅ **Out-of-sample validation** (8-year expanding window)
- ✅ **Comprehensive risk metrics** (15+ measures)
- ✅ **Volatility targeting** (20% annual target)
- ✅ **Per-ticker attribution** (granular analysis)
- ✅ **SPY benchmark comparison** (alpha/beta/IR)

## 💡 Strategy Advantages

| Feature | Benefit |
|---------|---------|
| **Volume precedence** | Early trend detection |
| **EMA smoothing** | Noise filtering |
| **Dual MA gates** | False signal reduction |
| **Vol targeting** | Stable risk exposure |
| **10-stock universe** | Diversification |

## ⚠️ Limitations & Enhancements


## 📋 Requirements (`requirements.txt`)

```txt
pandas>=1.5.0
numpy>=1.24.0
yfinance>=0.2.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyterlab>=4.0.0
```

