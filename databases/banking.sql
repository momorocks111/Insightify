-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    date_of_birth TEXT,
    join_date TEXT
);

-- Insert 1000 customers
INSERT INTO customers (first_name, last_name, email, phone, address, city, state, zip_code, date_of_birth, join_date)
SELECT 
    'FirstName' || num,
    'LastName' || num,
    'email' || num || '@example.com',
    '555-' || SUBSTR('0000' || CAST(ABS(RANDOM()) % 10000 AS TEXT), -4, 4),
    'Address ' || CAST(ABS(RANDOM()) % 1000 AS TEXT),
    'City' || CAST(ABS(RANDOM()) % 50 AS TEXT),
    'State' || CAST(ABS(RANDOM()) % 50 AS TEXT),
    SUBSTR('00000' || CAST(ABS(RANDOM()) % 100000 AS TEXT), -5, 5),
    DATE('1950-01-01', '+' || CAST(ABS(RANDOM()) % 25000 AS TEXT) || ' days'),
    DATE('2010-01-01', '+' || CAST(ABS(RANDOM()) % 5000 AS TEXT) || ' days')
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e'),
    (SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS num FROM customers LIMIT 1000);

-- Accounts table
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    account_type TEXT,
    balance REAL,
    open_date TEXT,
    last_activity_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert 2000 accounts
INSERT INTO accounts (customer_id, account_type, balance, open_date, last_activity_date)
SELECT 
    CAST(ABS(RANDOM()) % 1000 + 1 AS INTEGER),
    CASE CAST(ABS(RANDOM()) % 3 AS INTEGER)
        WHEN 0 THEN 'Checking'
        WHEN 1 THEN 'Savings'
        ELSE 'Money Market'
    END,
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 100000, 2),
    DATE('2010-01-01', '+' || CAST(ABS(RANDOM()) % 5000 AS TEXT) || ' days'),
    DATE('2023-01-01', '+' || CAST(ABS(RANDOM()) % 365 AS TEXT) || ' days')
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 2000;

-- Transactions table
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    transaction_date TEXT,
    description TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Insert 100,000 transactions
INSERT INTO transactions (account_id, transaction_type, amount, transaction_date, description)
SELECT 
    CAST(ABS(RANDOM()) % 2000 + 1 AS INTEGER),
    CASE CAST(ABS(RANDOM()) % 4 AS INTEGER)
        WHEN 0 THEN 'Deposit'
        WHEN 1 THEN 'Withdrawal'
        WHEN 2 THEN 'Transfer'
        ELSE 'Payment'
    END,
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 1000, 2),
    DATE('2023-01-01', '+' || CAST(ABS(RANDOM()) % 365 AS TEXT) || ' days'),
    'Transaction ' || CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS TEXT)
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 100000;

-- Loans table
CREATE TABLE loans (
    loan_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    loan_type TEXT,
    amount REAL,
    interest_rate REAL,
    term_months INTEGER,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert 500 loans
INSERT INTO loans (customer_id, loan_type, amount, interest_rate, term_months, start_date, end_date)
SELECT 
    CAST(ABS(RANDOM()) % 1000 + 1 AS INTEGER),
    CASE CAST(ABS(RANDOM()) % 3 AS INTEGER)
        WHEN 0 THEN 'Personal'
        WHEN 1 THEN 'Auto'
        ELSE 'Mortgage'
    END,
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 500000, 2),
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 10, 2),
    CAST(ABS(RANDOM()) % 360 + 12 AS INTEGER),
    DATE('2020-01-01', '+' || CAST(ABS(RANDOM()) % 1825 AS TEXT) || ' days'),
    DATE('2025-01-01', '+' || CAST(ABS(RANDOM()) % 3650 AS TEXT) || ' days')
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 500;

-- Credit Cards table
CREATE TABLE credit_cards (
    card_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    card_number TEXT,
    card_type TEXT,
    credit_limit REAL,
    current_balance REAL,
    expiration_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert 750 credit cards
INSERT INTO credit_cards (customer_id, card_number, card_type, credit_limit, current_balance, expiration_date)
SELECT 
    CAST(ABS(RANDOM()) % 1000 + 1 AS INTEGER),
    SUBSTR('0000000000000000' || CAST(ABS(RANDOM()) % 10000000000000000 AS TEXT), -16, 16),
    CASE CAST(ABS(RANDOM()) % 4 AS INTEGER)
        WHEN 0 THEN 'Visa'
        WHEN 1 THEN 'MasterCard'
        WHEN 2 THEN 'American Express'
        ELSE 'Discover'
    END,
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 20000, 2),
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 10000, 2),
    DATE('2025-01-01', '+' || CAST(ABS(RANDOM()) % 1825 AS TEXT) || ' days')
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 750;

-- Branches table
CREATE TABLE branches (
    branch_id INTEGER PRIMARY KEY,
    branch_name TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    manager_id INTEGER
);

-- Insert 50 branches
INSERT INTO branches (branch_name, address, city, state, zip_code, manager_id)
SELECT 
    'Branch ' || CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS TEXT),
    'Address ' || CAST(ABS(RANDOM()) % 1000 AS TEXT),
    'City' || CAST(ABS(RANDOM()) % 50 AS TEXT),
    'State' || CAST(ABS(RANDOM()) % 50 AS TEXT),
    SUBSTR('00000' || CAST(ABS(RANDOM()) % 100000 AS TEXT), -5, 5),
    CAST(ABS(RANDOM()) % 200 + 1 AS INTEGER)
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 50;

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    position TEXT,
    hire_date TEXT,
    salary REAL,
    branch_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Insert 200 employees
INSERT INTO employees (first_name, last_name, position, hire_date, salary, branch_id)
SELECT 
    'FirstName' || CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS TEXT),
    'LastName' || CAST(ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS TEXT),
    CASE CAST(ABS(RANDOM()) % 5 AS INTEGER)
        WHEN 0 THEN 'Teller'
        WHEN 1 THEN 'Loan Officer'
        WHEN 2 THEN 'Branch Manager'
        WHEN 3 THEN 'Financial Advisor'
        ELSE 'Customer Service Representative'
    END,
    DATE('2010-01-01', '+' || CAST(ABS(RANDOM()) % 5000 AS TEXT) || ' days'),
    ROUND(30000 + CAST(ABS(RANDOM()) AS REAL) * 70000, 2),
    CAST(ABS(RANDOM()) % 50 + 1 AS INTEGER)
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 200;

-- Investment Products table
CREATE TABLE investment_products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    product_type TEXT,
    risk_level TEXT,
    minimum_investment REAL,
    annual_return_rate REAL
);

-- Insert 20 investment products
INSERT INTO investment_products (product_name, product_type, risk_level, minimum_investment, annual_return_rate)
VALUES
    ('High Yield Savings', 'Savings', 'Low', 0, 2.5),
    ('Money Market Fund', 'Money Market', 'Low', 500, 3.0),
    ('Short-Term Bond Fund', 'Bond', 'Low', 1000, 3.5),
    ('Intermediate-Term Bond Fund', 'Bond', 'Low-Medium', 2500, 4.0),
    ('Long-Term Bond Fund', 'Bond', 'Medium', 5000, 4.5),
    ('Balanced Fund', 'Mixed', 'Medium', 2500, 5.0),
    ('Large-Cap Stock Fund', 'Stock', 'Medium-High', 5000, 7.0),
    ('Mid-Cap Stock Fund', 'Stock', 'High', 5000, 8.0),
    ('Small-Cap Stock Fund', 'Stock', 'High', 5000, 9.0),
    ('International Stock Fund', 'Stock', 'High', 5000, 8.5),
    ('Emerging Markets Fund', 'Stock', 'Very High', 10000, 10.0),
    ('Real Estate Investment Trust (REIT)', 'Real Estate', 'Medium-High', 5000, 6.5),
    ('Commodity Fund', 'Commodity', 'High', 10000, 7.5),
    ('Hedge Fund', 'Alternative', 'Very High', 100000, 12.0),
    ('Private Equity Fund', 'Alternative', 'Very High', 250000, 15.0),
    ('Target Date 2030 Fund', 'Mixed', 'Medium', 1000, 6.0),
    ('Target Date 2040 Fund', 'Mixed', 'Medium-High', 1000, 7.0),
    ('Target Date 2050 Fund', 'Mixed', 'High', 1000, 8.0),
    ('Socially Responsible Fund', 'Mixed', 'Medium', 2500, 6.5),
    ('Dividend Growth Fund', 'Stock', 'Medium', 5000, 6.0);

-- Customer Investments table
CREATE TABLE customer_investments (
    investment_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    investment_amount REAL,
    purchase_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES investment_products(product_id)
);

-- Insert 1000 customer investments
INSERT INTO customer_investments (customer_id, product_id, investment_amount, purchase_date)
SELECT 
    CAST(ABS(RANDOM()) % 1000 + 1 AS INTEGER),
    CAST(ABS(RANDOM()) % 20 + 1 AS INTEGER),
    ROUND(CAST(ABS(RANDOM()) AS REAL) * 100000, 2),
    DATE('2020-01-01', '+' || CAST(ABS(RANDOM()) % 1825 AS TEXT) || ' days')
FROM (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
    CROSS JOIN (SELECT 'a' UNION SELECT 'b' UNION SELECT 'c' UNION SELECT 'd' UNION SELECT 'e')
LIMIT 1000;
