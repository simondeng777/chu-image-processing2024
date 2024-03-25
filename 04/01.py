#https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
import tabula


pdf_path ='data.pdf'
dfs = tabula.read_pdf(pdf_path, stream=True)
# read_pdf returns list of DataFrames
print(len(dfs))
print(dfs[0])

# set pages option
dfs = tabula.read_pdf(pdf_path, pages=3, stream=True)
print(dfs[0])


# pass pages as string
dfs =tabula.read_pdf(pdf_path, pages="1-2,3", stream=True)
print(dfs[0])

# extract all pages
dfs =tabula.read_pdf(pdf_path, pages="all", stream=True)
print(dfs[0])

# set area option
dfs = tabula.read_pdf(pdf_path, area=[126,149,212,462], pages=2)
print(dfs[0])


pdf_path2 = "campaign_donors.pdf"

dfs = tabula.read_pdf(pdf_path2, columns=[47, 147, 256, 310, 375, 431, 504], guess=False, pages=1)
df = dfs[0].drop(["Unnamed: 0"], axis=1)
print(df)



dfs =tabula.read_pdf(pdf_path, output_format="json")
print(dfs[0])

tabula.convert_into(pdf_path, "test.json", output_format="json", stream=True)


tabula.convert_into(pdf_path, "test.tsv", output_format="tsv", stream=True)

tabula.convert_into(pdf_path, "test.csv", output_format="csv", stream=True)


pdf_path3 = "spanning_cells.pdf"
dfs = tabula.read_pdf(
    pdf_path3,
    pages="1",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)
print(dfs[0])