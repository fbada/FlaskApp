### Financial Chatbot Documentation

#### Summary
The Financial Chatbot is a web-based tool designed to provide quick and easy access to financial data for major companies. Built using Flask, the chatbot allows users to interact with a dataset containing financial information, such as total revenue, net income, assets, liabilities, and cash flow, across different fiscal years. Users can ask predefined queries or request specific graphs, and the chatbot will respond with the relevant data or visualizations.

### Steps to Download the Git Repository and Implement the Environment and App

#### 1. **Clone the Git Repository**
To start, you'll need to clone the repository containing the Financial Chatbot application. Open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/fbada/FlaskApp.git
```


#### 2. **Navigate to the Project Directory**
Once the repository is cloned, navigate to the project directory:

```bash
cd Flask-App
```

#### 3. **Set Up a Virtual Environment**
To keep your project's dependencies isolated, it's recommended to create a virtual environment. You can do this using `venv`, which is included with Python:

```bash
python -m venv venv
```

This command creates a virtual environment named `venv` in your project directory.

#### 4. **Activate the Virtual Environment**
After creating the virtual environment, activate it:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

When the virtual environment is activated, you'll see `(venv)` prefixed to your terminal prompt.

#### 5. **Install Required Dependencies**
With the virtual environment active, install the required Python libraries using `pip`. The repository should include a `requirements.txt` file listing all necessary dependencies:

```bash
pip install -r requirements.txt
```

This command installs all the packages needed to run the Flask application, including `Flask`, `pandas`, `matplotlib`, and `seaborn`.

#### 6. **Run the Flask Application**
With the environment set up and dependencies installed, you can now run the Flask application:

```bash
python app.py
```

This will start the Flask development server. By default, the application will be accessible at `http://127.0.0.1:5000/`.

#### 7. **Access the Application**
Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the Financial Chatbot. You can type queries into the chatbot and view the generated financial graphs directly through the web interface.

#### 8. **Deactivate the Virtual Environment (Optional)**
Once you're done working on the application, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your system’s default Python environment.

### Summary
- **Clone the Repository**: `git clone https://github.com/yourusername/financial-chatbot.git`
- **Navigate to Directory**: `cd financial-chatbot`
- **Create a Virtual Environment**: `python -m venv venv`
- **Activate the Virtual Environment**: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run the Application**: `python app.py`

By following these steps, you’ll have the Financial Chatbot up and running in your local environment.

#### How the Chatbot Works
- **User Interaction**: Users interact with the chatbot through a text input field on the web interface.
- **Query Processing**: The chatbot processes user queries to determine which financial data is being requested. It then retrieves the corresponding information from a CSV file containing financial data.
- **Response Generation**: The chatbot responds with either a text-based answer (e.g., specific financial figures) or a link to a static graph that visually represents the data.

#### Predefined Queries
The chatbot can respond to the following types of queries:
1. **Total Revenue**:
   - Example: "What is the total revenue for Apple in 2022?"
2. **Net Income Change**:
   - Example: "How has net income changed for Microsoft from 2021 to 2022?"
3. **Total Assets**:
   - Example: "What are the total assets of Tesla in 2022?"
4. **Total Liabilities**:
   - Example: "What are the total liabilities of Microsoft in 2022?"
5. **Cash Flow from Operations**:
   - Example: "What is the cash flow from operations for Apple in 2022?"
6. **Graph Requests**:
   - Example: "Show me the total revenue graph"
   - Example: "Show me the assets vs liabilities graph"

#### Limitations
- **Predefined Queries Only**: The chatbot can only respond to predefined queries related to total revenue, net income, assets, liabilities, and cash flow. It cannot handle arbitrary questions outside these categories.
- **Static Graphs**: The graphs generated are static images based on the available data and are not dynamically updated in response to new inputs.
- **Data Scope**: The chatbot is limited to the financial data provided in the CSV file. It cannot access external data sources or update its data set automatically.
