from SheetCode import Sheet
sheet = Sheet(__file__)

sheet.Name = "Inspection of the RBC Middleware Data Preparation"
sheet.Description =["TBD"]

sheet.StartConditions = ["n.a."]

sheet.Case(f"Inspection of RBC MW")
sheet.Action("Inspect RBC MW XML")

sheet.Save()