import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

# Configure
EXCEL_PATH = Path("RWCDCF.xlsx")
OUT_DIR    = Path("Excel_Tables")
OUT_DIR.mkdir(exist_ok=True)

# Load Excel
raw = pd.read_excel(EXCEL_PATH, sheet_name=0, header=None)

# Selecting needed rows 
rows = [ 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36,  37, 38, 40, 41, 42, 43, 44, 45]

# Extract Metric & Value
metrics = raw.iloc[rows, 3].astype(str).tolist()
values  = raw.iloc[rows, 4].tolist()
td_df = pd.DataFrame({"Metric": metrics, "Value": values})

# Formatting
for i, m in enumerate(td_df["Metric"]):
    v = td_df.at[i, "Value"]
    if pd.isna(v) or v == "":
        td_df.at[i, "Value"] = ""
    elif "premium" in m.lower():
        # premium stored as decimal 
        td_df.at[i, "Value"] = f"{float(v)*100:.2f}%"
    elif m.startswith("Value per Share"):
        # prefix currency symbol
        td_df.at[i, "Value"] = f"$ {float(v):.2f}"
    elif "growth rate" in m.lower():
        td_df.at[i, "Value"] = f"{float(v):.2%}"
    else:
        # all other numbers go to 2dp
        try:
            td_df.at[i, "Value"] = f"{float(v):,.2f}"
        except:
            td_df.at[i, "Value"] = str(v)

# Styling and formatting
fig, ax = plt.subplots(
    figsize=(6, td_df.shape[0] * 0.3),
    tight_layout=True
)
ax.axis("off")

# full-width blue banner
banner_h = 0.12
banner_c = "#1F4E79"
ax.add_patch(Rectangle(
    (0, 1.0), 1.0, banner_h,
    transform=ax.transAxes, color=banner_c, clip_on=False
))
ax.text(
    0.01, 1.0 + banner_h/2,
    "Terminal Growth DCF Method",
    transform=ax.transAxes,
    fontsize=12, fontweight="bold",
    color="white", va="center"
)

# draw table 
tbl = ax.table(
    cellText=td_df.values,
    cellLoc="left",
    loc="center"
)

# remove all cell borders
for cell in tbl.get_celld().values():
    cell.set_linewidth(0)

# grey headers
grey = "#F2F2F2"
for r, m in enumerate(td_df["Metric"]):
    if m in {"Calculating EV", "Calculating Equity Value", "Price Per Share"}:
        tbl[(r,0)].set_facecolor(grey)
        tbl[(r,1)].set_facecolor(grey)
        tbl[(r,0)].get_text().set_weight("bold")
        tbl[(r,1)].get_text().set_weight("bold")

# bold the true totals
totals = {"Enterprise Value", "Equity Value", "Premium (discount) to Market Price"}
for r, m in enumerate(td_df["Metric"]):
    if m in totals:
        tbl[(r,0)].get_text().set_weight("bold")
        tbl[(r,1)].get_text().set_weight("bold")

# autosize & save
tbl.auto_set_column_width([0,1])
tbl.set_fontsize(10)

out = OUT_DIR / "DCF.png"
fig.savefig(out, dpi=300, bbox_inches="tight", pad_inches=0.1)
plt.close(fig)

