import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

# Configure
EXCEL_PATH = Path("RWCDCF.xlsx")   
OUTPUT_PNG = Path("FCFF2.png") 

# Rad Excel
raw = pd.read_excel(EXCEL_PATH, sheet_name=0, header=None)

# Get exact range D13:J23 
block = raw.iloc[12:23, 3:10]
# drop blank NOPAT spacer row 
block = block[block.iloc[:,0].notna()]

# Extract Metric & Units
metrics = block.iloc[:,0].astype(str).tolist()
units   = block.iloc[:,1].fillna("").astype(str).tolist()

# Year labels 
raw_years = raw.iloc[12, 5:10]
years     = [str(int(x)) for x in raw_years if pd.notna(x)]

# Build DataFrame
data = { years[i]: block.iloc[:, 2+i].tolist() for i in range(len(years)) }
fcff_df = pd.DataFrame({"Metric": metrics, "Units": units, **data})

# Formating the data cells
for r, m in enumerate(fcff_df["Metric"]):
    for y in years:
        v = fcff_df.at[r, y]
        if pd.isna(v) or v == "":
            fcff_df.at[r, y] = ""
        elif "Date" in m:
            fcff_df.at[r, y] = pd.to_datetime(v).strftime("%d-%b-%y")
        elif "Tax Rate" in m:
            fcff_df.at[r, y] = f"{v:.2%}"
        elif "Capex" in m:
            fcff_df.at[r, y] = f"({abs(v):.0f})"
        elif "Discount Period" in m:
            fcff_df.at[r, y] = str(round(v, 2))
        else:
            fcff_df.at[r, y] = f"{v:.0f}"

# Styling
fig, ax = plt.subplots(
    figsize=(10, fcff_df.shape[0] * 0.35),
    tight_layout=True
)
ax.axis("off")

# Blue banner title
banner_h, banner_c = 0.12, "#1F4E79"
ax.add_patch(Rectangle((0,1.0), 1.0, banner_h,
             transform=ax.transAxes, color=banner_c, clip_on=False))
ax.text(
    0.01, 1.0 + banner_h/2,
    "Free Cash Flow to Firm (FCFF)",
    transform=ax.transAxes,
    fontsize=14, fontweight="bold",
    color="white", va="center"
)

# Create table with headers
cols = ["", "Units"] + years
tbl = ax.table(
    cellText=fcff_df.values,
    colLabels=cols,
    loc="upper center"
)

# Remove gridlines
for cell in tbl.get_celld().values():
    cell.set_linewidth(0)

n_rows, n_cols = fcff_df.shape[0]+1, len(cols)

# Shade & style header row and align
grey = "#F2F2F2"
for c in range(n_cols):
    cell = tbl[(0, c)]
    cell.set_facecolor(grey)
    cell.get_text().set_weight("bold")
    # header alignment
    if c >= 2:
        cell.get_text().set_ha("right")
    elif c == 1:
        cell.get_text().set_ha("center")
    else:
        cell.get_text().set_ha("left")

# Align data rows Metric left, Units left, years right
for r in range(1, n_rows):
    for c in range(n_cols):
        txt = tbl[(r, c)].get_text()
        if c >= 2:
            txt.set_ha("right")
        else:
            txt.set_ha("left")

# Bold key totals
totals = {"NOPAT", "FCFF", "Discounted FCFF"}
for r, m in enumerate(fcff_df["Metric"], start=1):
    if m in totals:
        for c in range(n_cols):
            tbl[(r, c)].get_text().set_weight("bold")

# Size & save
tbl.auto_set_column_width(list(range(n_cols)))
tbl.set_fontsize(10)
fig.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight", pad_inches=0.1)
plt.close(fig)

