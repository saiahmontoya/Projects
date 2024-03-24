from sqlalchemy import create_engine, text

# Database connection information
username = "postgres"
password = ""
host_url = "localhost"
port = 5432
database_name = "postgres"
app_schema = "homework"

# Initialize a string for the connection settings.
connection_string = f"postgresql+psycopg2://{username}:{password}@{host_url}:{port}/{database_name}"

# Create a SQLAlchemy engine, using the connection string and schema parameters.
engine = create_engine(connection_string, connect_args={"options": f"-csearch_path={app_schema}"})

def get_employee_summary(last_name, first_name):
    with engine.connect() as conn:
        query = text(
            "SELECT * FROM employees WHERE lastname = :last_name AND firstname = :first_name"
        )

        result = conn.execute(query, {"last_name": last_name, "first_name": first_name})
        employee = result.first()

        if employee:
            print(f"{employee.firstname} {employee.lastname}, employee {employee.employeenumber}, {employee.email}")
            
            office_query = text("SELECT * FROM offices WHERE officecode = :officecode")
            office_result = conn.execute(office_query, {"officecode": employee.officecode})
            office = office_result.first()
            if office:
                print(f"Works at {office.city}, {office.country} (#{office.officecode}) office")
            
            customer_query = text("SELECT customername, customernumber FROM customers WHERE salesrepemployeenumber = :employee_number")
            customers_result = conn.execute(customer_query, {"employee_number": employee.employeenumber})
            customers = customers_result.fetchall()
            if customers:
                print("Customers:")
                for customer in customers:
                    print(f"{customer.customername} (#{customer.customernumber})")
            else:
                print("No customers found for this employee.")
        else:
            print(f"No employee found with last name '{last_name}' and first name '{first_name}'.")

if __name__ == "__main__":
    last_name = input("Enter the last name of the employee: ")
    first_name = input("Enter the first name of the employee: ")
    get_employee_summary(last_name, first_name)

