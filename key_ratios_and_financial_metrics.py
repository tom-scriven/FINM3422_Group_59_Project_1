# -----------------------------------------------
# Utility function
# -----------------------------------------------

#ensures no crashes occur when dividing numbers
def safe_divide(numerator, denominator):
    try:
        return numerator / denominator if denominator else None
    except (TypeError, ZeroDivisionError):
        return None

# -----------------------------------------------
# Data extraction function
# -----------------------------------------------

def extract_financial_data(ticker):
    # Extract main financial dataframes
    info = ticker.info
    bs = ticker.balance_sheet
    fs = ticker.financials
    cf = ticker.cashflow

    # Extract basic market and valuation info
    price = info.get("currentPrice")
    eps = info.get("trailingEps")
    book_value = info.get("bookValue")
    dividend = info.get("dividendRate")
    shares = info.get("sharesOutstanding")
    ebitda = info.get("ebitda")
    market_cap = info.get("marketCap")

    # Extract key income statement items
    revenue = fs.loc["Total Revenue"].iloc[0] if "Total Revenue" in fs.index else None
    gross_profit = fs.loc["Gross Profit"].iloc[0] if "Gross Profit" in fs.index else None
    operating_income = fs.loc["Operating Income"].iloc[0] if "Operating Income" in fs.index else None
    net_income = fs.loc["Net Income"].iloc[0] if "Net Income" in fs.index else None
    ebit = fs.loc["Ebit"].iloc[0] if "Ebit" in fs.index else None
    cogs = fs.loc["Cost Of Revenue"].iloc[0] if "Cost Of Revenue" in fs.index else (
        fs.loc["Cost of Goods Sold"].iloc[0] if "Cost of Goods Sold" in fs.index else None
    )
    # Extract key balance sheet items
    total_assets = bs.loc["Total Assets"].iloc[0] if "Total Assets" in bs.index else None
    current_liabilities = bs.loc["Total Current Liabilities"].iloc[0] if "Total Current Liabilities" in bs.index else None
    inventory = bs.loc["Inventory"].iloc[0] if "Inventory" in bs.index else 0
    cash = bs.loc["Cash"].iloc[0] if "Cash" in bs.index else 0

    # Calculate total debt from long- and short-term debt
    total_debt = 0
    if "Long Term Debt" in bs.index:
        total_debt += bs.loc["Long Term Debt"].iloc[0]
    if "Short Long Term Debt" in bs.index:
        total_debt += bs.loc["Short Long Term Debt"].iloc[0]

    # Calculate derived metrics
    capital_employed = total_assets - current_liabilities if total_assets and current_liabilities else None
    ev = market_cap + total_debt - cash if market_cap and total_debt and cash is not None else None
    revenue_per_share = revenue / shares if revenue and shares else None

    # Extract operating cash flow from cashflow statement
    cash_flow = None
    for key in ["Cash Flowsfromusedin Operating Activities Direct", "Operating Cash Flow"]:
        if key in cf.index:
            cash_flow = cf.loc[key].iloc[0]
            break
            
    cash_flow_per_share = cash_flow / shares if cash_flow and shares else None

    # Return all relevant extracted and derived data
    return {
        "price": price, "eps": eps, "book_value": book_value, "dividend": dividend, "shares": shares,
        "ebitda": ebitda, "market_cap": market_cap, "revenue": revenue, "gross_profit": gross_profit,
        "operating_income": operating_income, "net_income": net_income, "ebit": ebit,
        "total_assets": total_assets, "current_liabilities": current_liabilities,
        "inventory": inventory, "cash": cash, "total_debt": total_debt, "capital_employed": capital_employed,
        "enterprise_value": ev, "revenue_per_share": revenue_per_share, "cash_flow": cash_flow,
        "cash_flow_per_share": cash_flow_per_share,
    }

# -----------------------------------------------
# VALUATION RATIOS
# -----------------------------------------------

def pe_ratio(price, eps):
    return safe_divide(price, eps)

def pb_ratio(price, book_value_per_share):
    return safe_divide(price, book_value_per_share)

def ps_ratio(price, revenue_per_share):
    return safe_divide(price, revenue_per_share)

def ev_ebitda(ev, ebitda):
    return safe_divide(ev, ebitda)

def ev_to_revenue(ev, revenue):
    return safe_divide(ev, revenue)

# -----------------------------------------------
# PROFITABILITY RATIOS
# -----------------------------------------------

def gross_margin(gross_profit, revenue):
    return safe_divide(gross_profit, revenue)

def operating_margin(operating_income, revenue):
    return safe_divide(operating_income, revenue)

def net_margin(net_income, revenue):
    return safe_divide(net_income, revenue)

def roa(net_income, total_assets):
    return safe_divide(net_income, total_assets)

# -----------------------------------------------
# EFFICIENCY RATIOS
# -----------------------------------------------

def asset_turnover(revenue, total_assets):
    return safe_divide(revenue, total_assets)

def inventory_turnover(cogs, inventory):
    return safe_divide(cogs, inventory)

# -----------------------------------------------
# MARKET METRICS
# -----------------------------------------------

def dividend_yield(dividend, price):
    return safe_divide(dividend, price)

def earnings_yield(eps, price):
    return safe_divide(eps, price)

def price_to_cash_flow(price, cash_flow_per_share):
    return safe_divide(price, cash_flow_per_share)