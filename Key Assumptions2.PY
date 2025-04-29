import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

# Load & format 
excel_path = Path("RWCDCF.xlsx")
ka = pd.read_excel(
    excel_path,
    sheet_name=0,
    skiprows=2,
    nrows=8,
    usecols="D:E",
    header=None
)
ka.columns = ["Metric","Value"]

# Format values:
for i,row in ka.iterrows():
    m,v = row["Metric"], row["Value"]
    if pd.isna(v):
        ka.at[i,"Value"] = ""
    elif "Date" in m:
        ka.at[i,"Value"] = pd.to_datetime(v).strftime("%d/%m/%Y")
    elif any(k in m for k in ["Rate","tax","Growth"]):
        ka.at[i,"Value"] = f"{v:.2%}"
    else:
        ka.at[i,"Value"] = f"{v:.2f}"

# Configure and format
EXCEL_PATH = Path("RWCDCF.xlsx")   
OUTPUT_PNG = Path("Key_Assumptions2.png") 

fig, ax = plt.subplots(
    figsize=(4, ka.shape[0]*0.4),
    tight_layout=True
)
ax.axis("off")

# banner parameters
banner_height = 0.12
banner_color  = "#1F4E79"  # deep blue

# draw rectangle spanning full axes width
ax.add_patch(Rectangle(
    (0, 1.0),
    width=1.0,
    height=banner_height,
    transform=ax.transAxes,
    color=banner_color,
    clip_on=False
))

# banner text
ax.text(
    0.02, 1.0 + banner_height*0.5,
    "Key Assumptions",
    transform=ax.transAxes,
    fontsize=12,
    fontweight="bold",
    color="white",
    va="center"
)

# draw the table without colLabels
tbl = ax.table(
    cellText=ka.values,
    cellLoc="left",
    loc="center"
)

# remove all cell lines
for cell in tbl.get_celld().values():
    cell.set_linewidth(0)

# force column widths
tbl.auto_set_column_width([0,1])
tbl.set_fontsize(10)

# save
fig.savefig(OUTPUT_PNG, dpi=300, bbox_inches="tight", pad_inches=0.1)
plt.close(fig)

