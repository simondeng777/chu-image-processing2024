#https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html
import tabula

pdf_path ='campaign_donors.pdf'

dfs = tabula.read_pdf(pdf_path, columns=[47, 147, 256, 310, 375, 431, 504], guess=False, pages=1)
df = dfs[0].drop(["Unnamed: 0"], axis=1)
print(df)

tabula.convert_into(pdf_path, "campaign_donors.json", output_format="json", stream=True)
tabula.convert_into(pdf_path, "campaign_donors.csv", output_format="csv", stream=True)