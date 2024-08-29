from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Load the financial data
df = pd.read_csv('financial_data.csv')

# Set the style for the plots
sns.set(style="darkgrid")

# Plot and save the graphs
def plot_total_revenue(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Fiscal Year', y='Total Revenue', hue='Company', marker="o")
    plt.title('Total Revenue over Time by Company')
    plt.ylabel('Total Revenue (in millions)')
    plt.xlabel('Fiscal Year')
    plt.xticks(df['Fiscal Year'].unique())
    plt.legend(title='Company')
    plt.tight_layout()
    plt.savefig('static/revenue_plot.png')  # Save the plot as an image
    plt.close()

def plot_net_income_comparison(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Company', y='Net Income', hue='Fiscal Year')
    plt.title('Net Income Comparison by Company and Fiscal Year')
    plt.ylabel('Net Income (in millions)')
    plt.xlabel('Company')
    plt.legend(title='Fiscal Year')
    plt.tight_layout()
    plt.savefig('static/net_income_plot.png')  # Save the plot as an image
    plt.close()

def plot_assets_vs_liabilities(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Total Assets', y='Total Liabilities', hue='Company', style='Fiscal Year', s=100)
    plt.title('Total Assets vs. Total Liabilities by Company and Fiscal Year')
    plt.ylabel('Total Liabilities (in millions)')
    plt.xlabel('Total Assets (in millions)')
    plt.legend(title='Company')
    plt.tight_layout()
    plt.savefig('static/assets_liabilities_plot.png')  # Save the plot as an image
    plt.close()

# Generate the plots when the app starts
plot_total_revenue(df)
plot_net_income_comparison(df)
plot_assets_vs_liabilities(df)

def get_response(query_type, company, year=None, year1=None, year2=None):
    if query_type == "total_revenue":
        revenue = df[(df['Company'] == company) & (df['Fiscal Year'] == year)]['Total Revenue'].values[0]
        return f"The total revenue for {company} in {year} was ${revenue} million."
    
    elif query_type == "net_income_change":
        income_year1 = df[(df['Company'] == company) & (df['Fiscal Year'] == year1)]['Net Income'].values[0]
        income_year2 = df[(df['Company'] == company) & (df['Fiscal Year'] == year2)]['Net Income'].values[0]
        change = income_year2 - income_year1
        return f"The net income for {company} changed by ${change} million from {year1} to {year2}."
    
    elif query_type == "total_assets":
        assets = df[(df['Company'] == company) & (df['Fiscal Year'] == year)]['Total Assets'].values[0]
        return f"The total assets for {company} in {year} were ${assets} million."
    
    elif query_type == "total_liabilities":
        liabilities = df[(df['Company'] == company) & (df['Fiscal Year'] == year)]['Total Liabilities'].values[0]
        return f"The total liabilities for {company} in {year} were ${liabilities} million."
    
    elif query_type == "cash_flow":
        cash_flow = df[(df['Company'] == company) & (df['Fiscal Year'] == year)]['Cash Flow from Op. Act.'].values[0]
        return f"The cash flow from operations for {company} in {year} was ${cash_flow} million."
    
    else:
        return "Sorry, I can only provide information on predefined queries. Type 'help' to see available options."

def simple_chatbot(user_query):
    # Convert the query to lower case for easier matching
    user_query = user_query.lower()

    # Help command
    if "help" in user_query:
        help_messages = [
            "Here are some examples of what you can ask:",
            "1. Total Revenue:",
            "   - What is the total revenue for [Company] in [Year]?",
            "     e.g., 'What is the total revenue for Apple in 2022?'",
            "2. Net Income Change:",
            "   - How has net income changed for [Company] from [Year1] to [Year2]?",
            "     e.g., 'How has net income changed for Microsoft from 2021 to 2022?'",
            "3. Total Assets:",
            "   - What are the total assets of [Company] in [Year]?",
            "     e.g., 'What are the total assets of Tesla in 2022?'",
            "4. Total Liabilities:",
            "   - What are the total liabilities of [Company] in [Year]?",
            "     e.g., 'What are the total liabilities of Microsoft in 2022?'",
            "5. Cash Flow from Operations:",
            "   - What is the cash flow from operations for [Company] in [Year]?",
            "     e.g., 'What is the cash flow from operations for Apple in 2022?'",
            "6. Graphs:",
            "   - Show me the total revenue graph",
            "   - Show me the net income graph",
            "   - Show me the assets vs liabilities graph"
        ]
        return "\n\n".join(help_messages)

    # Graph-related queries
    elif "total revenue graph" in user_query:
        return f"Here is the total revenue graph:<br><img src='{url_for('static', filename='revenue_plot.png')}' alt='Total Revenue Graph' width='600'>"

    elif "net income graph" in user_query:
        return f"Here is the net income comparison graph:<br><img src='{url_for('static', filename='net_income_plot.png')}' alt='Net Income Graph' width='600'>"

    elif "assets vs liabilities graph" in user_query:
        return f"Here is the assets vs liabilities graph:<br><img src='{url_for('static', filename='assets_liabilities_plot.png')}' alt='Assets vs Liabilities Graph' width='600'>"

    # Define a list of companies and years to search for in the query
    companies = df['Company'].unique().tolist()
    years = df['Fiscal Year'].unique().tolist()

    # Initialize variables to store extracted information
    company = None
    year = None

    # Extract the company name from the query
    for c in companies:
        if c.lower() in user_query:
            company = c  # This will match the exact format in the DataFrame
            break

    # Extract the year from the query
    for y in years:
        if str(y) in user_query:
            year = y  # This will match the exact format in the DataFrame
            break

    # Now match the query type and return the corresponding response
    if "total revenue" in user_query and company and year:
        return get_response("total_revenue", company, year)

    elif "net income" in user_query and company and "from" in user_query and "to" in user_query:
        # Extract years for net income change
        year1 = int(user_query.split("from")[1].split("to")[0].strip())
        year2 = int(user_query.split("to")[1].strip())
        return get_response("net_income_change", company, year1=year1, year2=year2)

    elif "total assets" in user_query and company and year:
        return get_response("total_assets", company, year)

    elif "total liabilities" in user_query and company and year:
        return get_response("total_liabilities", company, year)

    elif "cash flow" in user_query and company and year:
        return get_response("cash_flow", company, year)

    else:
        return "Sorry, I can only provide information on predefined queries. Type 'help' to see available options."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get('user_query')
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
