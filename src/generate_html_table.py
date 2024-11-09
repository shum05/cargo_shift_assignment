# src/generate_html_table.py

def generate_html_table(assignments):
    html_content = "<table><tr><th>Full Name</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th><th>Sunday</th><th>Shift</th><th>Assigned Locations and Day Offs</th></tr>"

    for assignment in assignments:
        html_content += f"<tr><td>{assignment['full_name']}</td>"
        # Add days, shift, and locations to the row
        # TODO: Populate with real assignment data
        html_content += "</tr>"

    html_content += "</table>"
    return html_content
