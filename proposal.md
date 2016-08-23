## Driver Reports - A Capstone Proposal



### Product Overview
**Driver Reports** is a reporting system for data obtained from a Driver's Education program administrator for the purpose of evaluating the effectiveness of student participants. This application will display Python-parsed mySQL data to a Bootstrap dashboard.

### Specific Functionality
* Login Screen
* Dashboard - Main 
	* Overview of student completion, hours driven, student enrollment vs. passing numbers
	* Sidebar links to data subsets 

### Data Model
**student** - Driver's education participant that is being evaluated

**instructor** - *Student's* Driver's Ed evaluator, submitting grades for drives and class

**program administrator** - evaluates effectiveness of *instructor* by looking at all student evaluations against *instructor*

### Technical Components
* Take data from Production database
* Parse data to JSON
* Plug JSON data to Bootstrap dashboard
* Streamline process to keep data retrieval time to a bare minimum
* Integrate existing branding to maintain product unity

![IMG TEXT](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/free-bootstrap-admin-dashboard-templates.jpg)
*I want to use this dashboard as the jumping off point for the Administrator reporting*

### Estimated Schedule
* Discover database scraping/removal from live Production content
* Python-based function to parse SQL data
* Connecting data to Bootstrap dashboard
* Refactor and streamline code to reduce time

### Functionality Beyond Your MVP
* Develop different Dashboard interfaces (Parents, Instructors)
* Find ways to include geolocation data (mapping drives, marking errors during drives)