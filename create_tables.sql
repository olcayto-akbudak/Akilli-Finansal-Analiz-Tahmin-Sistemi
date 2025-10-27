-- create_tables.sql
-- Basit finansal tablo şeması (SQL Server / PostgreSQL uyumlu temel SQL)

CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    AccountName NVARCHAR(200),
    AccountType NVARCHAR(50) -- e.g., Revenue, Expense, Asset
);

CREATE TABLE Transactions (
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    AccountID INT,
    TransactionDate DATE,
    Amount DECIMAL(18,2),
    Currency NVARCHAR(10),
    Description NVARCHAR(500),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);

-- Örnek: Zaman serisi özet tablosu (aylık)
CREATE TABLE MonthlySummaries (
    SummaryID INT IDENTITY(1,1) PRIMARY KEY,
    YearMonth CHAR(7), -- YYYY-MM
    AccountID INT,
    TotalAmount DECIMAL(18,2),
    CreatedAt DATETIME DEFAULT GETDATE()
);

-- Örnek veri ekleme (kendi veritabanına göre düzenleyin)
INSERT INTO Accounts (AccountID, AccountName, AccountType) VALUES (1, 'Total Revenue', 'Revenue');
INSERT INTO Accounts (AccountID, AccountName, AccountType) VALUES (2, 'Total Expense', 'Expense');

-- Örnek transaction verisi (örnek amaçlı, gerçek veriye göre düzenleyin)
INSERT INTO Transactions (AccountID, TransactionDate, Amount, Currency, Description) VALUES (1, '2023-01-01', 120000.00, 'TRY', 'Revenue Jan 2023');
INSERT INTO Transactions (AccountID, TransactionDate, Amount, Currency, Description) VALUES (1, '2023-02-01', 130000.00, 'TRY', 'Revenue Feb 2023');
INSERT INTO Transactions (AccountID, TransactionDate, Amount, Currency, Description) VALUES (1, '2023-03-01', 125000.00, 'TRY', 'Revenue Mar 2023');
