from SheetCode import Sheet
import scripts.RT_Common as RT_Common

sheet = Sheet(__file__)

sheet.Name = "Conditional Emergency Stop due to signal replacement"
sheet.Description = ["For each elementary route marked with Referential/Route/@Type='Inside' and in every applicable mode as per <Referential/Route/PossibleModes> (FS, OS or SH).",
                      "1) a train will be set upstream of the start signal and the route will be set. We are not checking the MA content as it's done already in RT_L2, RT_ENTRY, RT_EXIT",
                      "2) the signal will be set to Emergency",
                      "3) RBC shall send a CES and the connections and mode profiles shall be set according to the signal capabilities (FS, OS, SH)"]

sheet.StartConditions = ["No elementary routes is set or locked.",
                          "No train is set on the track."]

for mode in ["FS", "OS", "SH"]:
    # *********************************************************************************************************************************************
    sheet.Case(f"Route set in {mode}")
    
    RT_Common.InitialConditionsL2(sheet, RT_Common.Aspects.RNP, RT_Common.InitialPositions.Valid)

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    sheet.Action(f"Set route under test in {mode}")
    
    sheet.ExpectedResult("SLR: MA is received") 
    
    
        
sheet.Save()
