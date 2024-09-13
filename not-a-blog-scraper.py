import csv
from collections import defaultdict
from datetime import datetime

def count_blogs_by_month(file_path):
    blog_counts = defaultdict(int)
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        
        for row in csvreader:
            if len(row) >= 2 and row[1]:  # Check if date column exists and is not empty
                try:
                    date = datetime.strptime(row[1], "%d/%m/%Y")
                    month_year = date.strftime("%B %Y")
                    blog_counts[month_year] += 1
                except ValueError:
                    continue  # Skip rows with invalid dates
    
    # Print the results
    for month_year, count in sorted(blog_counts.items(), key=lambda x: datetime.strptime(x[0], "%B %Y")):
        print(f"{month_year}: {count} blogs")
    
    # Find and print the month with the most blogs
    max_month = max(blog_counts, key=blog_counts.get)
    print(f"\nMonth with the most blogs: {max_month} ({blog_counts[max_month]} blogs)")

def count_blogs_by_year(file_path):
    blog_counts = defaultdict(int)
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        
        for row in csvreader:
            if len(row) >= 2 and row[1]:  # Check if date column exists and is not empty
                try:
                    date = datetime.strptime(row[1], "%d/%m/%Y")
                    year = date.year
                    blog_counts[year] += 1
                except ValueError:
                    continue  # Skip rows with invalid dates
    
    # Print the results
    for year in sorted(blog_counts.keys()):
        print(f"{year}: {blog_counts[year]} blogs")
    
    # Find and print the year with the most blogs
    max_year = max(blog_counts, key=blog_counts.get)
    print(f"\nYear with the most blogs: {max_year} ({blog_counts[max_year]} blogs)")

# Usage
print("Blogs by Month:")
count_blogs_by_month('notablog.csv')
print("\nBlogs by Year:")
count_blogs_by_year('notablog.csv')
