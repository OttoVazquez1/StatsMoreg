import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def filter_dataframe_by_name(df, name):
    filtered_df = df[df["Nombre"].str.contains(name)]
    return filtered_df

def filter_dataframe_by_id(df, number):
    filtered_ID = df[df['Documento'].str[:2] == number]
    return filtered_ID


def filter_and_plot_name():
    name = entry.get().strip().upper()
    if not name:
        messagebox.showinfo('No Input', 'Please enter a name.')
        return

    filtered_df = filter_dataframe_by_name(df, name)
    count = len(filtered_df)
    if count == 0:
        messagebox.showinfo('No Results', 'No matching records found.')
    else:
        plot_name_stats(filtered_df, name.capitalize())

def plot_name_stats(dataf, name):
    total_count = len(df)
    name_count = len(dataf)
    
    percentage_name = lambda: (name_count * 100) / total_count

    result_percentage_name = percentage_name()

    result_percentage_others = 100 - result_percentage_name

    labels = [name, 'Others']
    sizes = [result_percentage_name, result_percentage_others]
    colors = ['lightblue', 'lightgray']
    explode = (0.2, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.title(f'Percentage of People named {name}')
    plt.show()

def plot_id_stats(dataf, name):
    total_count = len(df)
    name_count = len(dataf)
    
    percentage_name = lambda: (name_count * 100) / total_count

    result_percentage_name = percentage_name()

    result_percentage_others = 100 - result_percentage_name

    labels = [name, 'Others']
    sizes = [result_percentage_name, result_percentage_others]
    colors = ['red', 'lightgray']
    explode = (0.2, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.title(f'Percentage of People with DNI finished in {name}')
    plt.show()

def filter_and_plot_ID():
    id = entryTWO.get().strip()
    if not id.isdigit():
        messagebox.showinfo('No Input', 'Please enter a valid number.')
        return

    filtered_df = filter_dataframe_by_id(df, id)
    count = len(filtered_df)
    if count == 0:
        messagebox.showinfo('No Results', 'No matching records found.')
    else:
        plot_id_stats(filtered_df, id)

# Read the CSV file into a DataFrame
csv_file_path = 'stats_moreg.csv'
df = pd.read_csv(csv_file_path)

# Create the UI
root = tk.Tk()
root.title('Stats Filter')
root.geometry('300x200')

label = tk.Label(root, text='Enter name:')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Filter and Plot', command=filter_and_plot_name)
button.pack()

labelTWO = tk.Label(root, text='Enter 2 numbers:')
labelTWO.pack()

entryTWO = tk.Entry(root)
entryTWO.pack()

buttonTWO = tk.Button(root, text='Filter and Plot', command=filter_and_plot_ID)
buttonTWO.pack()

root.mainloop()