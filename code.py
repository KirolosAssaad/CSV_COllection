import time
import csv
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
full_csv = []
t = open('/Users/kirolosmorcos/Desktop/to_save_file.txt','w+', encoding="UTF-8")

for folder , sub_folders , files in os.walk("/Users/kirolosmorcos/Desktop/test"):
    for f in files:
        data = open("/Users/kirolosmorcos/Desktop/test/" + f, encoding = "UTF-8")
        csv_data = csv.reader(data)
        lines = list(csv_data)
        lines.pop(0)
        for x in lines:
            full_csv.append(x)
for i in range(len(full_csv)):
    t.write ("line {}:".format(i+1))
    for j in range(len(full_csv[i])):
        t.write ("field {}: {}".format(j+1, full_csv[i][j]))
    t.write("----------------------------")

class Watcher:
    DIRECTORY_TO_WATCH = "/Users/kirolosmorcos/Desktop/test"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print (event.src_path)
            data = open(event.src_path, encoding = "UTF-8")
            csv_data = csv.reader(data)
            lines = list(csv_data)
            lines.pop(0)
            for x in lines:
                full_csv.append(x)

            for i in range(len(full_csv)):
                t.write("line {}:".format(i+1))
                for j in range(len(full_csv[i])):
                    t.write("field {}: {}".format(j+1, full_csv[i][j]))
                t.write("----------------------------")
            full_csv.clear()



if __name__ == '__main__':
    w = Watcher()
    w.run()

