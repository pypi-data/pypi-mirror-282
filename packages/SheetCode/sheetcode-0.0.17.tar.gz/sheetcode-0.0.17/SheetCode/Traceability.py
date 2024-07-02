import os
import pandas as pd
from tabulate import tabulate # need pip install tabulate
from termcolor import colored # need pip install termcolor
import warnings
import tempfile
import shutil

SheetReqs = pd.DataFrame(columns=['Coverage', 'Test sheet', 'Line', 'LoopTargetName'])
SheetParams = pd.DataFrame(columns=['Coverage', 'Test sheet', 'Line', 'LoopTargetName'])

def RequirementsFilepath():
    return os.path.join(os.environ["TRACEABILITY_PATH"], 'requirements.xlsx')

def ParametersFilepath():
    return os.path.join(os.environ["TRACEABILITY_PATH"], 'parameters.xlsx')

def Clear():
    if os.path.exists(RequirementsFilepath()):
        os.remove(RequirementsFilepath())    
    if os.path.exists(ParametersFilepath()):
        os.remove(ParametersFilepath())   

def AddRequirement(reqId, sheet, line, loopTargetName):
    CheckRequirementSyntax(sheet, reqId)
    SheetReqs.loc[len(SheetReqs.index)] = [reqId, sheet, line, loopTargetName]

def AddParameter(xpath, sheet, line, loopTargetName):
    CheckParameterSyntax(sheet, xpath)
    SheetParams.loc[len(SheetParams.index)] = [xpath, sheet, line, loopTargetName]

def CheckRvtCoverage(sheetName):
    _CheckCoverage(sheetName, SheetReqs, os.environ["RVT_FILEPATH"], "RVT", 3, "Req ID", "Req Text", "Test Sheet Name", None)

def CheckParametersCoverage(sheetName):
    _CheckCoverage(sheetName, SheetParams, os.environ["PARAMETERS_FILEPATH"], "Parameters", 1, "Xpath", None, "Project Test scenario", "Used by project")

def GetReferenceItems(referenceFilepath, referenceSheetName, headerRowIdx, usedColumnName):
    # Do not check coverage if reference path set to empty
    if referenceFilepath == "":
        return
    
    # Check if file exists !
    if not os.path.exists(referenceFilepath): 
        print(colored(f"Can't find {os.path.basename(referenceFilepath)}. Coverage not evaluated !", "red", attrs=["bold"]))
        return None
        
    # Try to open the file
    try:
        warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
        referenceItems = pd.read_excel(referenceFilepath, sheet_name=referenceSheetName, header=headerRowIdx)
    except:
        print(colored(f"Can't open {os.path.basename(referenceFilepath)}, file is probably opened in Excel. Coverage not evaluated !", "red", attrs=["bold"]))
        return None

    # Filter Used items (if applicable)
    if usedColumnName != None:
        referenceItems = referenceItems[referenceItems[usedColumnName].str.contains("Yes", na = False) | referenceItems[usedColumnName].str.contains("Always", na = False)]

    return referenceItems

def _CheckCoverage(testSheetName, sheetItems, referenceFilepath, referenceSheetName, headerRowIdx, itemIdColumnName, itemTextColumnName, testSheetColumnName, usedColumnName):
    # Get all reference items (only "used" ones if applicable)
    referenceItems = GetReferenceItems(referenceFilepath, referenceSheetName, headerRowIdx, usedColumnName)
    if referenceItems is None: return # Return if reference not found

    # Get items allocated to this sheet
    referenceItems = referenceItems[referenceItems[testSheetColumnName].str.contains(testSheetName, na = False)]

    # Get Reqs covered by this sheet
    SheetItemsGrouped = sheetItems.groupby("Coverage")["Line"].agg(concatenate_lines).reset_index()

    # Evaluate coverage
    print(colored(f"Coverage against {os.path.basename(referenceFilepath)} for {testSheetName}", "white", attrs=["bold", "underline"]))
    print(f"{len(referenceItems)} items allocated to {testSheetName}")
    notInSheet = referenceItems[~referenceItems[itemIdColumnName].str.lower().isin(SheetItemsGrouped["Coverage"].str.lower())]
    if notInSheet.shape[0] > 0:
        print(colored(f"{notInSheet.shape[0]} items are expected to be covered by this sheet but aren't:", "red", attrs=["bold"]))
        if itemTextColumnName is None:
            # Params
            print(colored(tabulate(notInSheet[[itemIdColumnName]], headers='keys', tablefmt='simple', showindex=False, maxcolwidths=[250, 70]), "red"))
        else:
            # Reqs
            print(colored(tabulate(notInSheet[[itemIdColumnName, itemTextColumnName]], headers='keys', tablefmt='simple', showindex=False, maxcolwidths=[35, 70]), "red"))
    else:
        print(colored(f"All {len(referenceItems)} items covered in {testSheetName}", "green"))

    # Evaluate non-expected items
    notInReference = SheetItemsGrouped[~SheetItemsGrouped["Coverage"].str.lower().isin(referenceItems[itemIdColumnName].str.lower())]
    if notInReference.shape[0] > 0:
        print(colored(f"{notInReference.shape[0]} items appear in the test sheet but are not allocated to it:", "yellow", attrs=["bold"]))
        if itemTextColumnName is None:
            # Params
            print(colored(tabulate(notInReference, headers='keys', tablefmt='simple', showindex=False, maxcolwidths=[250, 40]), "yellow"))
        else:
            # Reqs
            print(colored(tabulate(notInReference, headers='keys', tablefmt='simple', showindex=False, maxcolwidths=[35, 40]), "yellow"))
    
def SaveRvtCoverage(): 
    if os.path.exists(RequirementsFilepath()):
        Reqs = pd.read_excel(RequirementsFilepath())
        # File exists, merge
        mergedReqs = pd.concat([Reqs, SheetReqs])
        # mergedReqsGrouped = mergedReqs.groupby(["Coverage"]).agg({"Test sheet": lambda x: '\r\n'.join(map(str, pd.unique(x))), "Line": lambda x: '\r\n'.join(map(str, x))})
        mergedReqs.to_excel(RequirementsFilepath())
    else:
        # File not yet existing
        if not os.path.exists(os.environ["TRACEABILITY_PATH"]): os.mkdir(os.environ["TRACEABILITY_PATH"])
        SheetReqs.to_excel(RequirementsFilepath())

def SaveParametersCoverage(): 
    if os.path.exists(ParametersFilepath()):
        Params = pd.read_excel(ParametersFilepath())
        # File exists, merge
        mergedParams = pd.concat([Params, SheetParams])
        #mergedParamsGrouped = mergedParams.groupby(["Coverage"]).agg({"Test sheet": lambda x: '\r\n'.join(map(str, pd.unique(x))), "Line": lambda x: '\r\n'.join(map(str, x))})
        mergedParams.to_excel(ParametersFilepath())
    else:
        # File not yet existing
        if not os.path.exists(os.environ["TRACEABILITY_PATH"]): os.mkdir(os.environ["TRACEABILITY_PATH"])
        SheetParams.to_excel(ParametersFilepath())

def concatenate_lines(series):
    return ", ".join(map(str, series))

def CheckRequirementSyntax(sheet, reqId):
    if reqId.count('[') == 0:
        raise Exception (f"Missing '[' in {reqId} in {sheet}")
    elif reqId.count('[') > 1:
        raise Exception (f"More than 1 '[' in {reqId} in {sheet}")
    if reqId.count(']') == 0:
        raise Exception (f"Missing ']' in {reqId} in {sheet}")
    elif reqId.count(']') > 1:
        raise Exception (f"More than ']' in {reqId} in {sheet}")
    
def CheckParameterSyntax(sheet, xpath):
    if xpath.count('/') == 0:
        raise Exception (f"No '/' in {xpath} in {sheet}")
    
def EvaluateSheetsCoverage(validationMethod):
    # Get all reference items (only "used" ones if applicable)
    referenceItems = GetReferenceItems(os.environ["RVT_FILEPATH"], "RVT", 3, None)
    if referenceItems is None: return # Return if reference not found

    # Filter target VM, eg. RBC Data Validation RM
    expectedItems = referenceItems[referenceItems["Validation Method"].str.contains(validationMethod, na = False)]


    # Retrieve current traceability
    actualItems = pd.read_excel(RequirementsFilepath())

    coverage = pd.merge(expectedItems, actualItems, left_on="Req ID", right_on="Coverage", how="left", sort=False)
    mergedCoverage = coverage.groupby(["Req ID", "Req Text"]).agg({"Test sheet": lambda x: '\r\n'.join(map(str, pd.unique(x)))})

    expectedCount = len(mergedCoverage.index)
    notCoveredCount = mergedCoverage['Test sheet'].value_counts()["nan"]
    printProgressBar(expectedCount - notCoveredCount , expectedCount, prefix = f"Coverage for '{validationMethod}'", suffix = 'Complete', length = 50)
        
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = ""):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'{prefix} |{bar}| {percent}% {suffix}', end = printEnd)



    


    


