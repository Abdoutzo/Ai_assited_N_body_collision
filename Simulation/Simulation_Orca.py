'''
For simulating the behavior of 10 robots in antipodal positions, we use the 'Antipodal_task.xml' file as input for the C++ code.
 The output is the 'Antipodal_task_10_log.xml' file, which contains the paths of the ten robots.
 Subsequently, this file becomes the input for our Python code, 'Simulation_Orca.py'.
'''
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Path to your XML file
xml_file_path = "Path to the file Antipodal_task_10_log.xml"

# Parse the XML content from the file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Find the log element and iterate over agent elements
log_element = root.find('.//log')
agents = log_element.findall('.//agent')

# Create a figure and axis
fig, ax = plt.subplots()
plt.title('Agent Paths')

# Set axis limits from 0 to 64
ax.set_xlim(0, 64)
ax.set_ylim(0, 64)

# Set proper aspect ratio
ax.set_aspect('equal')

# Initialize scatter plots for each agent
scatters = [ax.scatter([], [], marker='o', label=f'Agent {agent.get("id")}') for agent in agents]

# Initialize line plots for each agent's trail
trails = [ax.plot([], [], linestyle='-', alpha=0.3)[0] for _ in agents]

# Function to initialize the plot
def init():
    for scatter, trail in zip(scatters, trails):
        scatter.set_offsets(np.empty((0, 2)))  # Set an empty array for the initial offset
        trail.set_data([], [])  # Set an empty array for the initial trail
    return scatters + trails

# Function to update the plot for each frame
def update(frame):
    for i, agent in enumerate(agents):
        path_element = agent.find('./path')

        if path_element is not None:
            steps = path_element.findall('./step')
            if frame < len(steps):
                step = steps[frame]
                xr = float(step.get('xr'))
                yr = float(step.get('yr'))

                # Update the position for the current step
                scatters[i].set_offsets(np.array([[xr, yr]]))

                # Update the trail by appending the current position
                trail_x, trail_y = trails[i].get_data()
                trails[i].set_data(np.append(trail_x, xr), np.append(trail_y, yr))
            else:
                # If the frame exceeds the number of steps, set offsets to an empty array
                scatters[i].set_offsets(np.empty((0, 2)))
        else:
            scatters[i].set_offsets(np.empty((0, 2)))

    return scatters + trails

# Set up the animation with a delay of 200 milliseconds between frames
ani = animation.FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, interval=200)

# Set legend size
ax.legend(loc='upper left', fontsize='small')

# Display the animation
plt.show()
