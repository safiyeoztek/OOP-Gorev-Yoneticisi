class TaskManager:
    def __init__(self, filename = "tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        with open(self.filename, "r", encoding="utf-8") as file:
                for satir in file:
                   self.tasks.append(satir.strip())

    def add_task(self, task):
       self.tasks.append(task)
       print(f"{task} listeye eklendi.")


    def list_tasks(self):
        print("----- GÖREV LİSTESİ -----")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Görevler kaydedildi. Çıkılıyor...")


methods = TaskManager()

while True:
    print("1-Görev ekle\n2-Görevleri listele\n3-Kaydet ve çık\n")
    secim = input("Seçim:")

    if secim == "1":
        task = input("Görev adı: ")
        methods.add_task(task)

    elif secim == "2":
        methods.list_tasks()

    elif secim == "3":
        methods.save_tasks()
        break
        

    