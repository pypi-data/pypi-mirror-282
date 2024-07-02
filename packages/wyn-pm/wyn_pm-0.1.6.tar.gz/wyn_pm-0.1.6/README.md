# WYN-PM 📈💼

Welcome to the `wyn-pm` library, an official library from [W.Y.N. Associates, LLC](https://wyn-associates.com/) FinTech branch. This library provides tools for stock analysis, efficient portfolio generation, and training sequential neural networks for financial data.

## Installation 🚀

To install the library, use the following command:

```bash
! pip install wyn-pm
```

## Stock Analyzer: Plot Buy/Sell Signal 📊

Analyze stocks and plot buy/sell signals using the MACD indicator.

### Example Usage:

```python
from wyn_pm.stock_analyzer import *

# Initialize stock analysis for a given ticker
stock_analysis = StockAnalysis(ticker="AAPL")

# Fetch stock data
stock_analysis.fetch_data()

# Calculate MACD
stock_analysis.calculate_macd()

# Find crossovers to generate buy/sell signals
stock_analysis.find_crossovers(bullish_threshold=-2, bearish_threshold=2)

# Create and show the plot
fig = stock_analysis.create_fig()
fig.show()
```

## Efficient Portfolio: Generate Optimal Weights 💹

Create an optimal portfolio by generating efficient weights for a list of stock tickers.

### Example Usage:

```python
from wyn_pm.efficient_portfolio import *

# Initialize portfolio with given tickers and date range
portfolio = EfficientPortfolio(tickers=["AAPL", "MSFT", "GOOGL"], start_date="2020-01-01", end_date="2022-01-01", interval="1d")

# Download stock data
stock_data = portfolio.download_stock_data()

# Calculate portfolio returns
portfolio_returns = portfolio.create_portfolio_and_calculate_returns(top_n=5)

# Calculate mean returns and covariance matrix
mean_returns = stock_data.pct_change().mean()
cov_matrix = stock_data.pct_change().cov()

# Define the number of portfolios to simulate and the risk-free rate
num_portfolios = 10000
risk_free_rate = 0.01

# Display the efficient frontier with randomly generated portfolios
fig, details = portfolio.display_simulated_ef_with_random(mean_returns.values, cov_matrix.values, num_portfolios, risk_free_rate)
fig.show()

# Print details of the max Sharpe and min volatility portfolios
print(details)
```

## Training Sequential Neural Networks: Stock Prediction 🤖📈

Train various neural network models on stock data and perform Monte Carlo simulations.

### Example Usage:

```python
from wyn_pm.trainer import *

# Example usage:
stock_modeling = StockModeling()

# Training: ~ 9 min on CPU
forecast_results, mc_figure = stock_modeling.forecast_and_plot(stock="AAPL", start_date="2020-01-01", end_date="2023-01-01", look_back=50, num_of_epochs=10, n_futures=365, n_samples=1000, verbose_style=1)

# Results
print(forecast_results)
mc_figure.show()
```

---

Enjoy analyzing stocks, creating efficient portfolios, and training neural networks with `wyn-pm`! If you have any questions, feel free to reach out.

Happy coding! 🖥️✨