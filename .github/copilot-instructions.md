<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

This project is a **Python-based inventory management system** for tracking parts related to **Purchase Orders and Requisitions**, designed for **engineering and maintenance teams**. The system should support CRUD operations for **parts, purchase orders, requisitions, and quotes**, while maintaining **foreign key relationships** in SQLite.

### **Prioritize**
- **Code readability & maintainability**  
  - Follow **PEP 8** standards for indentation, naming, and style.  
  - Use **absolute file paths** to avoid dependency issues.  
  - Keep functions **modular and reusable** across different features.  

- **Tabbed GUI with Tkinter**  
  - Ensure **dropdown selection** for foreign keys (e.g., selecting a company).  
  - Minimize unnecessary UI clutter while keeping **entry forms intuitive**.  
  - Comment **each section clearly** for beginner-level users.
  - Keep the UI spaced out a little and make sure there is space between text boxes.

- **Automated inventory updates using SQLite triggers**  
  - Example: **Increase stock count** when parts are received.  
  - Prevent inconsistent data using **referential integrity checks**.  

- **Beginner-friendly code comments**  
  - Write **all comments and guidance** as if written by me.
  - Explain **each function** as if teaching a new Python student.  
  - Include **tips for debugging** common SQLite, Python and other issues.  

### **Preferred Libraries**
- **SQLite** – Data storage with lightweight relational database capabilities.  
- **Pillow** – Image handling (if applicable for parts tracking).  
- **Pandas** – Used for structured data processing, reports, and imports.  

This system should be **minimalist yet scalable**, making it intuitive for engineers, maintenance personnel, and Python learners.