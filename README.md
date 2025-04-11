# Bug Tracker Web
# Author: Lorenz V. Wilkins
# Original Project: https://github.com/GucciRemyBoi/Bug-Tracker
## Stack
**Backend**: Python (Flask)  
**Frontend**: HTML, Bootstrap (will migrate to TailwindCSS + React)  
**Storage**: JSON files (will migrate to PostgreSQL)

## Resources
- Flask: https://flask.palletsprojects.com/en/stable/
- Flask file uploads: https://flask.palletsprojects.com/en/stable/
- send_from_directory documentation: https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory
- OS for understanding directory/file manipulation: https://docs.python.org/3/library/os.html
- Werkzeug for handling file names when saving uploads: https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.utils.secure_filename
- Form Data Handling: https://herotofu.com/terms/multipart-form-data
- Boostrap info for layout, tables, buttons, forms: https://getbootstrap.com/docs/5.3/getting-started/introduction/
- Bootstrap CDN: https://www.jsdelivr.com/?query=bootstrap
- Python JSON module: https://docs.python.org/3/library/json.html
- For best practicies with JSON structuring: https://spacetelescope.github.io/understanding-json/
- datetime module docs: https://docs.python.org/3/library/datetime.html
- Pytz timezone handling: https://pypi.org/project/pytz/
---

## Goal
A lightweight web-based bug tracker that allows frontend and backend developers to submit, view, and update bugs during the development phase. The app supports attachments, GitHub links, file names, and simulated user identity. This prototype lays the groundwork for a full-stack version with authentication and role-based access control.

---

## Project Structure
```
bug_tracker_web/
├── app.py                      # Main Flask file
├── bugs/                       # Folder where JSON bug files are currently stored
├── uploads/                    # Folder to store uploaded attachments
├── static/
│   └── style.css               # Custom CSS
├── templates/
│   ├── index.html              # Home page listing all bugs
│   ├── reportBug.html          # Form to submit new bugs
│   ├── viewBug.html            # Full bug details
│   └── updateBug.html          # Update status of a bug
└── README.md                   # Project documentation
```
---
## app.py - Application Core
This is the core of the project, responsible for routing, logic, and data management. Key imports include:
- `os`: for directory management
- `json`: for storing bugs as JSON
- `datetime` & `pytz`: for timestamping bugs in Pacific time
- `secure_filename`: for secure handling of uploaded filenames
- `send_from_directory`: for downloading uploaded attachments

## Key Routes and Functions:

### `index()`
- Loads all JSON bug files from the `bugs/` directory
- Renders `index.html` with a table view of all bugs

### `reportBug()`
- Handles GET/POST
- GET: renders the form to file a new bug
- POST: processes form inputs, handles optional file upload, saves data to a JSON file, simulates a user with `"Created By": "Lorenz"`

### `updateBug(bugId)`
- Handles GET/POST
- GET: loads bug and renders update form
- POST: updates status and timestamp

### `viewBug(bugId)`
- Renders all bug details (description, GitHub, attachment, etc.)
- Returns 404 if bug does not exist

### `uploadedFile(filename)`
- Securely serves attachment download via `/uploads/<filename>`

---

## Frontend Views

### `index.html`
- Displays a Bootstrap-styled table of bugs
- Columns: ID, Description, Status, Developer, Actions
- Future version will be Tailwind + React (currently Bootstrap via jsDelivr)

### `reportBug.html`
- Form fields:
  - Title
  - Description
  - File Name
  - Bug Type
  - Priority (dropdown)
  - Optional GitHub PR/Commit link
  - Optional Attachment upload
- Uses `enctype="multipart/form-data"` for file uploads

### `viewBug.html`
- Displays bug metadata:
  - Title, Description, File Name, Priority, Bug Type, Status
  - GitHub link (clickable)
  - Attachment download (if available)
  - Last Updated timestamp
  - Created By field

### `updateBug.html`
- Dropdown to change bug status
- Saves new status and updates timestamp
- (Future: full status history log)

---

## JSON Bug Format Example
```json
{
    "ID": 2,
    "Title": "Example",
    "Description": "this is an example upload of a bug, showing the structure of a json formatting",
    "File Name": "example.py",
    "Priority": "Low",
    "Bug Type": "example type",
    "GitHub PR/Commit": "https://github.com/GucciRemyBoi/Bug-Tracker",
    "Attachment": "bug-2_output.png",
    "Status": "Open",
    "Last Updated": "2025-04-10T10:49:21.091446-07:00",
    "Created By": "Lorenz"
}
```

---

## Features Implemented
-  Submit a new bug via form and save as JSON
-  Attachments saved in `/uploads` with download link
-  GitHub PR/Commit linking
-  View detailed bug page
-  Status update with UI
-  Simulated login with static username
-  Clean UI using Bootstrap
-  File validation with secure filename handling and max file size of 5MB

---

## Roadmap
This is the prototype for a full-stack bug tracking platform.

### Stack Goals:
- **Frontend**: React + TailwindCSS with `shadcn/ui` or Chakra UI
- **Backend**: Flask
- **Database**: PostgreSQL (replacing JSON)

### UI Features:
- Filterable bug tables
- Full bug activity timeline
- Collaborative comment threads

---

## AI Future Features

### 1. **Bug Priority Estimator**
Use GPT to suggest a bug's priority based on description.

### 2. **Suggested Repro Steps**
Ask GPT to infer likely reproduction steps from bug details.

### 3. **Duplicate Bug Detection**
Use embedding + vector search to flag similar past bugs.

---

## Final Notes
This project demonstrates not only my technical ability to build backend systems using Flask, but also my focus on scalable architecture, clean design, and AI-readiness. It's the foundation for a much larger system — and I'm excited to keep building on top of it.
