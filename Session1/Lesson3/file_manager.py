import csv

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        rows = []

        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
                print(row)
        
        return rows

    def save_tasks(self, tasks):
        writer = csv.writer(open(self.filename, "w"))
        for task in tasks:
            print(task.__str__())
            writer.writerow(task.__str__())
