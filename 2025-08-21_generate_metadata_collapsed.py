
import pandas as pd
import plotly.express as px
from plotly.io import to_html
from pathlib import Path

# =============================================================================
# Load data
# =============================================================================

import os
os.chdir('.\\')

# read all sheets in your excel file
file_path = Path("2025-09-17_ref_metadata_model_v1.1_share.xlsx")
xls = pd.ExcelFile(file_path)

# =============================================================================
# colors and descriptions for data classes
# =============================================================================

# determine colors for Mandatory, Recommended & Optional for each data class
base_colors = {
    "synthesis": {"M": "#d73027", "R": "#f46d43", "O": "#fdae61"},
    "characterization": {"M": "#4575b4", "R": "#74add1", "O": "#abd9e9"},
    "reaction": {"M": "#1a9850", "R": "#66bd63", "O": "#a6d96a"},
    "simulation": {"M": "#984ea3", "R": "#b358cb", "O": "#e082ea"},
    "cat_core": {"M": "#e66101", "R": "#fdb863", "O": "#fddbc7"}
}

description_map = {
    "cat core": "The CatCore describes the minimum information which must be reported with research data concerning the field of catalysis. This guideline should help to handle and standarise data in this versatile research field based on the FAIR principle (F-indable, A-ccessible, I-nteroperable, R-eusable). This should help to ensure that research results are supported by high quality data and to simplify quering the shared data for a future of data-driven material discovery. The guideline is based on the terminology of Voc4Cat. The inner CatCore describes the most fundamental metadata which is mandatory to describe the research on the most general level with the goal of facilitating a categorization of the research data and help researchers to make their data findable. The expanded CatCore contains the data classes 'Synthesis', 'Reaction', 'Characterization' and 'Simulation'. It is important to note that 'Synthesis' and 'Reaction' are the two data classes which are fundamental for catalysis and cannot be transferred to other fields, whereas the characterization methods and simulations are well-known in other chemistry fields.",
    "synthesis": "The data class 'Synthesis' describes the minimum information which should be reported with research data concerning the field of catalyst synthesis. Based on the various catalysis research fields, this data class is kept general to allow relevant entries of the various research fields. To ensure a reasonable description of the synthesised catalyst, also parameters which need to be determined by analytical methods (such as BET or NMR) can be entered.",
    "characterization": "The data class 'Characterization' describes the minimum information which should be reported with research data to describe the nature of the catalyst. Herefore, various characterization methods are listed which are highly important in the catalysis research field. To ensure a standaridisation of the data, recommendations on the meta data report are given for the specific methods.",
    "reaction": "The data class 'Reaction' describes the minimum information which should be reported with research data concerning the reaction for which the catalyst is applied and the evaluation of the catalyst's performance.",
    "simulation": "The data class 'Simulation' describes the minimum information which should be reported with research data for conduction simulations in the field of catalysis to gain theoretical insights."
}

# =============================================================================
# Drop-down function
# =============================================================================

def build_dropdown_tree(df, parent_label, level=1):
    children = df[df["parent"] == parent_label]
    if children.empty:
        return ""
    class_name = "nested" if level == 1 else "subnested"
    html = ""
    for _, row in children.iterrows():
        label = row["label"]
        uri = row.get("voc4cat URI", "")
        link = f'<a href="{uri}" target="_blank">{label}</a>' if uri else label
        sub = build_dropdown_tree(df, label, level + 1)
        if sub:
            html += f'<details class="{class_name}"><summary>{link}</summary>\n{sub}</details>\n'
        else:
            html += f'<div class="{class_name}">{link}</div>\n'
    return html

html_all = """<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <title>Metadata Reference Model</title>
  <style>
    body { font-family: Arial; line-height: 1.6; margin: 20px; }
    details summary { font-weight: bold; cursor: pointer; margin-top: 10px; }
    .nested { margin-left: 20px; }
    .subnested { margin-left: 40px; }
    .indented-section { margin-left: 20px; }
  </style>
  <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
</head>
<body>
<h1>Metadata Reference Model</h1>
"""

# =============================================================================
# create mark-down for all sheets
# =============================================================================

output_dir = Path("metadata_individual_charts")
output_dir.mkdir(exist_ok=True)


for sheet_name in xls.sheet_names:
    sheet_key = sheet_name.strip().lower()
    df = xls.parse(sheet_name).fillna("")
    df["label"] = df["label"].astype(str).str.strip()
    df["parent"] = df["parent"].astype(str).str.strip()
    df["mro"] = df["mandatory, recommended, optional"].astype(str).str.strip().str.upper()

    html_all += f"<details><summary>{sheet_name}</summary>\n"
    html_all += f"<p>{description_map.get(sheet_key, 'This section contains structured metadata definitions.')}</p>\n"
    html_all += "<div class='indented-section'>\n"

    for section, mro_code in [("Mandatory", "M"), ("Recommended", "R"), ("Optional", "O")]:
        html_all += f"<details><summary>{section}</summary>\n"
        top_level = df[(df["mro"] == mro_code) & (df["parent"].isin(["", "na"]))]
        for _, row in top_level.iterrows():
            label = row["label"]
            uri = row.get("voc4cat URI", "")
            link = f'<a href="{uri}" target="_blank">{label}</a>' if uri else label
            html_all += f'<details class="nested"><summary>{link}</summary>\n'
            html_all += build_dropdown_tree(df, label)
            html_all += '</details>\n'
        html_all += '</details>\n'
    html_all += "</div>\n"

    labels, ids, parents, hover_texts, colors = [], [], [], [], []
    node_map = {}

    labels.append(sheet_name)
    ids.append(sheet_name)
    parents.append("")
    hover_texts.append(f"Data class: {sheet_name}")
    root_color = base_colors.get(sheet_key, {"M": "#cccccc"})["M"]
    colors.append(root_color)
    node_map[(sheet_name, sheet_name)] = sheet_name

    for _, row in df.iterrows():
        label = row["label"]
        node_map[(sheet_name, label)] = f"{sheet_name}|{label}"

    for _, row in df.iterrows():
        label = row["label"]
        parent = row["parent"]
        mro = row["mro"]
        node_id = node_map[(sheet_name, label)]
        parent_id = sheet_name if parent.lower() in ["", "na"] else node_map.get((sheet_name, parent), sheet_name)
        color_dict = base_colors.get(sheet_key, base_colors["cat_core"])
        color = color_dict.get(mro, "#dddddd")

        labels.append(label)
        ids.append(node_id)
        parents.append(parent_id)
        hover_texts.append(f"{label} (child of {parent})")
        colors.append(color)

    fig = px.sunburst(
        ids=ids,
        names=labels,
        parents=parents,
        hover_name=labels
    )
    
    fig.update_traces(marker=dict(colors=colors))
    fig.update_layout(
        margin=dict(t=10, l=10, r=10, b=10),
        autosize=True
    )

    chart_html = to_html(
        fig,
        full_html=False,
        include_plotlyjs=False,
        config={"responsive": True}
    )

    if sheet_key in ["simulation", "reaction", "synthesis", "characterization"]:
        single_html = f"""<!DOCTYPE html>
    <html>
    <head>
      <meta charset='UTF-8'>
      <script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
      <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
        }}
        .chart-container {{
            width: 100%;
            height: 100vh;
        }}
      </style>
    </head>
    <body>
    <div class="chart-container">
    {chart_html}
    </div>
    </body>
    </html>
    """

        single_file_path = output_dir / f"metadata_{sheet_key}_hierarchy.html"

        with open(single_file_path, "w", encoding="utf-8") as sf:
            sf.write(single_html)

    html_all += f"""<details>
    <summary><strong>Metadata Hierarchy Chart</strong></summary>
    {chart_html}
    </details>\n"""
    html_all += "</details>\n"

html_all += "</body>\n</html>"

with open("metadata_collapsed_charts_all_sheets.html", "w", encoding="utf-8") as f:
    f.write(html_all)
