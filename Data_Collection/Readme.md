
Data Collection Process : 

# Each iteration of this process adds up to 250 lines to our database.

1. After executing the "Generation_of_Circle_Scenarios.py" file, you'll obtain a random antipodal scenario with 10 robots, equidistant, in the format of an XML file. This XML file will serve as input for the C++ code. We have attached a link to the repository containing the C++ code.

2. Once you run the C++ code (executed using the CMake method with detailed steps provided in the Readme of the repository: ORCA-ALGORITHM; the link is available in the "C++_Code_Implémentation_ORCA.md" file), it will generate an XML output file containing the paths of the ten robots in the antipodal scenario. Please note the specific name of this XML file for reference.

3. To incorporate the results into our database, you need to convert this XML file to Excel. You can achieve this by running the "XML_to_Excel.py" script. This Python script will facilitate the conversion process.

Make sure to follow these steps sequentially to obtain and process the data effectively.
