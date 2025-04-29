#needed in this file: An API that has key ratios and financial metrics, and computed in functions that have been created

# Utility function to safely divide two numbers, handling errors like division by zero or None
def safe_divide(numerator, denominator):
    try:
        return numerator / denominator if denominator else None
    except (TypeError, ZeroDivisionError):
        return None

# -----------------------
# VALUATION RATIOS
# -----------------------

# Price-to-Earnings Ratio: current share price divided by earnings per share
def pe_ratio(price, eps):
    return safe_divide(price, eps)

# Price-to-Book Ratio: current share price divided by book value per share
def pb_ratio(price, book_value_per_share):
    return safe_divide(price, book_value_per_share)

# Price-to-Sales Ratio: current share price divided by revenue per share
def ps_ratio(price, revenue_per_share):
    return safe_divide(price, revenue_per_share)

# Enterprise Value to EBITDA: a valuation ratio comparing enterprise value to earnings before interest, taxes, depreciation, and amortisation
def ev_ebitda(ev, ebitda):
    return safe_divide(ev, ebitda)

# Enterprise Value to Revenue: a valuation ratio comparing enterprise value to revenue
def ev_to_revenue(ev, revenue):
    return safe_divide(ev, revenue)

# -----------------------
# PROFITABILITY RATIOS
# -----------------------

# Gross Margin: gross profit as a percentage of revenue
def gross_margin(gross_profit, revenue):
    return safe_divide(gross_profit, revenue)

# Operating Margin: operating income as a percentage of revenue
def operating_margin(operating_income, revenue):
    return safe_divide(operating_income, revenue)

# Net Margin: net income as a percentage of revenue
def net_margin(net_income, revenue):
    return safe_divide(net_income, revenue)

# Return on Assets: net income divided by total assets
def roa(net_income, total_assets):
    return safe_divide(net_income, total_assets)

# -----------------------
# EFFICIENCY RATIOS
# -----------------------

# Asset Turnover: revenue divided by total assets
def asset_turnover(revenue, total_assets):
    return safe_divide(revenue, total_assets)

# Inventory Turnover: cost of goods sold divided by average inventory
def inventory_turnover(cogs, avg_inventory):
    return safe_divide(cogs, avg_inventory)

# -----------------------
# MARKET METRICS
# -----------------------

# Dividend Yield: dividend per share divided by price
def dividend_yield(dividend, price):
    return safe_divide(dividend, price)

# Earnings Yield: earnings per share divided by price (inverse of P/E)
def earnings_yield(eps, price):
    return safe_divide(eps, price)

# Price to Cash Flow: price per share divided by cash flow per share
def price_to_cash_flow(price, cash_flow_per_share):
    return safe_divide(price, cash_flow_per_share)
