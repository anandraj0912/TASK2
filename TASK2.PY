import tkinter as tk
from tkinter import messagebox
import sqlite3
import logging

# Set up logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Database setup
def setup_database():
    conn = sqlite3.connect('calculator_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY,
            operation TEXT,
            result REAL
        )
    ''')
    conn.commit()
    return conn

def log_operation(conn, operation, result):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO history (operation, result) VALUES (?, ?)', (operation, result))
    conn.commit()

def calculate(operation, x, y):
    try:
        x = float(x)
        y = float(y)
        if operation == '+':
            return x + y
        elif operation == '-':
            return x - y
        elif operation == '*':
            return x * y
        elif operation == '/':
            if y == 0:
                raise ValueError("Cannot divide by zero.")
            return x / y
        else:
            raise ValueError("Invalid operation.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None

def on_calculate():
    operation = operation_var.get()
    x = entry_x.get()
    y = entry_y.get()
    result = calculate(operation, x, y)
    if result is not None:
        result_label.config(text=f"Result: {result}")
        log_operation(conn, f"{x} {operation} {y}", result)
        logging.info(f"Performed: {x} {operation} {y} = {result}")

# GUI setup
conn = setup_database()
root = tk.Tk()
root.title("Calculator")

operation_var = tk.StringVar(value='+')

tk.Label(root,)