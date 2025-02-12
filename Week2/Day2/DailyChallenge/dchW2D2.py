# Create a class to handle paginated content in a website. 
# A pagination is used to divide long lists of content in a series of pages.
class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize)
        self.totalPages = len(self.items) // self.pageSize + (1 if len(self.items) % self.pageSize != 0 else 0)
        self.currentPage = 1

    def paginate(self):
        paginated_items = []
        for i in range(0, len(self.items), self.pageSize):
            paginated_items.append(self.items[i:i + self.pageSize])
        return paginated_items

    def getVisibleItems(self):
        try:
            choose_page = int(input(f"Enter the page number (1-{self.totalPages}): "))
            if 1 <= choose_page <= self.totalPages:
                self.currentPage = choose_page  # Update current page
                return self.paginate()[choose_page - 1]
            else:
                print("This page number is out of range.")
                return []
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return []

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
            return self.paginate()[self.currentPage - 1]
        else:
            print("You are already on the first page.")
            return []

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
            return self.paginate()[self.currentPage - 1]
        else:
            print("You are already on the last page.")
            return []

    def firstPage(self):
        self.currentPage = 1
        return self.paginate()[0] if self.totalPages > 0 else []

    def lastPage(self):
        self.currentPage = self.totalPages
        return self.paginate()[-1] if self.totalPages > 0 else []

# Example usage:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(f"Number of total pages is: {p.totalPages}")

print("The current page: ")
print(p.getVisibleItems())

print("The previous page: ")
print(p.prevPage())

print("The next page: ")
print(p.nextPage())

print("The first page: ")
print(p.firstPage)

print("The last page: ")
print(p.lastPage())