class Task:
    def __init__(self, name, difficulty, status="pending"):
        self.name = name
        self.difficulty = difficulty
        self.status = status
    
    def __str__(self):
        return f"Task: {self.name}, Difficulty: {self.difficulty}, Status: {self.status}"

    def mark_completed(self):
        self.status = "done"