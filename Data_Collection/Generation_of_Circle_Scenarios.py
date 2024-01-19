import math
import random

def calculate_circle_coordinates(num_agents, radius, center, rotation_direction='clockwise'):
    # Calculate angle between each agent
    angle_step = 2 * math.pi / num_agents

    # Determine rotation direction
    if rotation_direction == 'counter-clockwise':
        angle_step *= -1

    # Introduce a random offset to the starting angle
    random_offset = random.uniform(0, 2 * math.pi)
    angle_offset = random_offset * (1 if rotation_direction == 'clockwise' else -1)

    # Calculate agent coordinates and their antipodal points
    coordinates = []
    for i in range(num_agents):
        angle = i * angle_step + angle_offset
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        coordinates.append((x, y))

    # Calculate antipodal coordinates (with respect to the center)
    antipodal_coordinates = [(2 * center[0] - x, 2 * center[1] - y) for x, y in coordinates]

    return coordinates, antipodal_coordinates

def generate_xml(points, antipodal_points):
    xml_output = '<agents number="{}" type="orca">\n'.format(len(points))
    xml_output += '    <default_parameters size="0.3" movespeed="1" agentsmaxnum="{}" timeboundary="5.4" sightradius="3.0" timeboundaryobst="33"/>\n'.format(len(points))

    for i, (point, antipodal_point) in enumerate(zip(points, antipodal_points)):
        xml_output += '    <agent id="{}" start.xr="{}" start.yr="{}" goal.xr="{}" goal.yr="{}"/>\n'.format(i, point[0], point[1], antipodal_point[0], antipodal_point[1])

    xml_output += '</agents>\n'
    xml_output += '<obstacles number="1">\n'
    # Add obstacle details if needed
    xml_output += '</obstacles>'

    return xml_output

# Example: for 10 agents, radius 10, and center (32, 32), rotating counter-clockwise
num_agents = 10
radius = 10
center = (32, 32)

# Rotate counter-clockwise with a random starting point
agent_coordinates, antipodal_coordinates = calculate_circle_coordinates(num_agents, radius, center, rotation_direction='counter-clockwise')

# Generate XML representation
xml_representation = generate_xml(agent_coordinates, antipodal_coordinates)

# Print the XML representation
print(xml_representation)