# =======================
# Declaration of stock_list and date_range
# =======================
start_date = "2010-01-01"
end_date   = "2019-12-31"

stock_list = [
    "NVDA","MSFT","AAPL","AMZN","META",
    "AVGO","GOOGL","TSLA","GOOG","BRK-B"
]

results = run_backtest(
    start_date, end_date, stock_list,
    weighted="both",                  # runs both variants weighted and unweighted
    compare_and_report=True,          # prints/plots comparison portfolio
    benchmark_symbol="SPY", init_cap=500000
)
