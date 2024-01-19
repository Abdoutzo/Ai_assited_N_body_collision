import xml.etree.ElementTree as ET
import pandas as pd

def xml_to_excel(xml_file, output_excel):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    agent_data = {}

    # Extract all agent information dynamically
    for agent_elem in root.iter('agent'):
        agent_id = int(agent_elem.attrib['id'])
        agent_data[f'Agent{agent_id}_xr'] = []
        agent_data[f'Agent{agent_id}_yr'] = []

        for step_elem in agent_elem.iter('step'):
            step_number = int(step_elem.attrib['number'])
            xr = float(step_elem.attrib['xr'])
            yr = float(step_elem.attrib['yr'])
            agent_data[f'Agent{agent_id}_xr'].append(xr)
            agent_data[f'Agent{agent_id}_yr'].append(yr)

    max_steps = max(len(agent_data[col]) for col in agent_data)

    # Fill in missing values with None to ensure equal length
    for col in agent_data:
        agent_data[col] += [None] * (max_steps - len(agent_data[col]))

    df = pd.DataFrame(agent_data)
    df.to_excel(output_excel, index=False)

if __name__ == "__main__":
    xml_file = "D:/ORCA-algorithm/task_examples/orca45_10_log.xml"
    output_excel = "D:/ORCA-algorithm/output45.xlsx"
    xml_to_excel(xml_file, output_excel)

