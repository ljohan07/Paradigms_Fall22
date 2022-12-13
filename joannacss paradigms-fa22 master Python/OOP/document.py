class Document:
    # constructor 
    def __init__(self, author, creation_date): 
        self.author = author 
        self.creation_date = creation_date
    # operations
    def print(): 
        pass # empty method implementation
    def edit():
        pass # empty method implementation
    def __str__(self):
        return f"Created by {self.author} on {self.creation_date}"

# objects
d1 = Document("Alice", "2021-09-25")
d2 = Document("Bob", "2021-09-26")

print(d1)
print(d2)
