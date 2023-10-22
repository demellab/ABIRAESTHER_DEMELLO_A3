# ReadMe: Bank Account Application

This bank account application showcases basic operations that can be performed on bank accounts such as Savings and Chequing accounts.

## Table of Contents
1. Modules & Classes
2. Application Workflow
3. Running the Application
4. Future Enhancements

## 1. Modules & Classes

The application uses three external modules:

### a. BankModule

It contains the `Bank` class which keeps track of all accounts (both Savings and Chequing) in a list.

### b. ChequingAccountModule

It contains the `ChequingAccount` class which represents a chequing account in the bank.

### c. SavingsAccountModule

It contains the `SavingsAccount` class which represents a savings account in the bank.

## 2. Application Workflow

1. Displays the current account information of a list of customers.
2. Demonstrates operations such as withdrawal and deposit on various accounts.
3. Shows error scenarios like trying to withdraw more than the balance or depositing negative amounts.
4. Removes a specific account from the list.
5. Displays updated account information.

## 3. Running the Application

To run the application, ensure that all the required modules (`BankModule`, `ChequingAccountModule`, and `SavingsAccountModule`) are present in the same directory as the main application script.

Execute the main script:

```bash
$ python main_script_name.py
```

Replace `main_script_name.py` with the name of the script containing the `Application` class.

## 4. Future Enhancements

The application currently has basic operations. Here are some suggestions for future enhancements:

- Introduce interest calculation for savings accounts.
- Add overdraft facilities for chequing accounts.
- Incorporate user input to allow users to perform transactions on the go.
- Add transaction history for each account.
- Implement authentication for added security.

---

**Note**: The exact functionality and attributes of `Bank`, `SavingsAccount`, and `ChequingAccount` classes are based on their definitions in their respective modules, which are not provided in this document.
