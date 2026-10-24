
# CS 340 – Grazioso Salvare Rescue Animal Dashboard

## Project Overview

For my CS 340 course at Southern New Hampshire University, I developed an interactive dashboard for Grazioso Salvare, an organization that identifies dogs suitable for search-and-rescue training.

The dashboard uses Python, MongoDB, and Dash to help users search through animal shelter records and identify dogs that meet specific training requirements. It includes filters for different rescue categories, an interactive data table, a breed distribution chart, and a geolocation map.

This project builds on the CRUD Python module I developed in Project One, which handles communication between the application and the MongoDB database.

## Project Features

- **Water Rescue Filter:** Identifies dogs that meet the preferred breed, age, and sex requirements for water rescue.
- **Mountain or Wilderness Rescue Filter:** Displays dogs suitable for mountain and wilderness rescue training.
- **Disaster or Individual Tracking Filter:** Identifies dogs that meet the requirements for disaster rescue or tracking.
- **Reset Filter:** Returns the dashboard to its original, unfiltered state.
- **Interactive Data Table:** Allows users to browse and sort animal shelter records.
- **Breed Distribution Chart:** Displays the distribution of breeds within the selected records.
- **Geolocation Map:** Displays geographic information associated with a selected animal.

## Technologies Used

- **Python:** Application development and database integration
- **MongoDB:** Storage and retrieval of animal shelter records
- **PyMongo:** Communication between Python and MongoDB
- **Dash and JupyterDash:** Interactive dashboard development
- **Pandas:** Data processing and organization
- **Plotly Express:** Data visualization
- **Dash Leaflet:** Geolocation mapping
- **Jupyter Notebook:** Development and testing

---

## CS 340 Module Eight – Portfolio Reflection

### 1. How do you write programs that are maintainable, readable, and adaptable?

When writing programs, I try to keep my code organized and separate different responsibilities so that making changes later is easier. One of the biggest examples of this was creating the CRUD Python module in Project One and reusing it for Project Two. Instead of rewriting database queries and connection logic throughout the dashboard, I could use the existing module to communicate with MongoDB.

This made the dashboard code easier to manage and allowed me to focus more on building the interface and its features. I also learned how important it is to write reusable code, especially when working on larger projects. In the future, I could use a similar CRUD module for inventory systems, management dashboards, or any application that needs to store and retrieve information from a database.

### 2. How do you approach a problem as a computer scientist?

I usually approach programming problems by first understanding what needs to be accomplished and then breaking the work into smaller steps. For the Grazioso Salvare project, I started by reviewing the client's requirements and figuring out how the database, filters, data table, and visualizations would need to work together.

This project was different from some of my previous assignments because I wasn't just writing code to solve one specific problem. I had to connect several different components into one working application. I also ran into challenges with importing my CRUD module, formatting MongoDB data for the dashboard, and getting the application to display correctly in Codio. Working through these issues helped me become more comfortable troubleshooting and understanding how different technologies interact.

For future projects, I want to continue using this approach by planning the application structure, separating responsibilities, and testing each component before putting everything together.

### 3. What do computer scientists do, and why does it matter?

I believe computer scientists use programming, technology, and problem-solving skills to develop solutions that make everyday tasks more efficient. Their work goes beyond just writing code because they also need to understand the problems people or organizations are trying to solve.

The Grazioso Salvare project is a good example of this. The organization needed a better way to identify dogs that could potentially be trained for different types of search-and-rescue work. By creating a dashboard that allows users to filter animal records and visualize the results, I was able to turn a large amount of database information into something much easier to navigate.

Instead of manually searching through shelter records, the organization could use the dashboard to narrow down potential candidates based on breed, age, and sex. This could save time, reduce errors, and help the organization focus on its rescue training efforts.

---

## Final Reflection

Overall, CS 340 helped me better understand how databases and software applications work together. Before this course, much of my programming experience focused on building individual features or solving specific coding problems. This project gave me more experience working with databases, reusable modules, and interactive applications as part of a larger system.

One of my biggest takeaways was learning that good software development isn't just about making something work. It's also about making the code understandable, reusable, and easier to improve in the future. These are skills I plan to continue developing as I work toward my computer science degree and pursue a career in software engineering.

