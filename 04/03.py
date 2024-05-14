#https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
import tabula

pdf_path = "spanning_cells.pdf"
dfs = tabula.read_pdf(
    pdf_path,
    pages="1",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)
print(dfs[0])

tabula.convert_into(pdf_path, "spanning_cells.json", output_format="json", stream=True)
tabula.convert_into(pdf_path, "spanning_cells.csv", output_format="csv", stream=True)