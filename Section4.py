
# 12
def read_and_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        words = text.split()
        chars = len(text)
        
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {chars}")


# 13
import datetime

def write_log():
    with open('log.txt', 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"Script run at: {timestamp}\n")


# 14
import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['marks']) > 75:
                print(row['name'])
