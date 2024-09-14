import csv
from collections import defaultdict
from datetime import datetime

def count_blogs_by_month(file_path):
    blog_counts = defaultdict(int)
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        for row in csvreader:
            if len(row) >= 2 and row[1]:
                try:
                    date = datetime.strptime(row[1], "%d/%m/%Y")
                    month_year = date.strftime("%B %Y")
                    blog_counts[month_year] += 1
                except ValueError:
                    continue
    
    for month_year, count in sorted(blog_counts.items(), key=lambda x: datetime.strptime(x[0], "%B %Y")):
        print(f"{month_year}: {count} blogs")
    
    max_month = max(blog_counts, key=blog_counts.get)
    print(f"\nMonth with the most blogs: {max_month} ({blog_counts[max_month]} blogs)")
    
    min_month = min(blog_counts, key=blog_counts.get)
    print(f"Month with the least blogs: {min_month} ({blog_counts[min_month]} blogs)")

def count_blogs_by_year(file_path):
    blog_counts = defaultdict(int)
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        for row in csvreader:
            if len(row) >= 2 and row[1]:
                try:
                    date = datetime.strptime(row[1], "%d/%m/%Y")
                    year = date.year
                    blog_counts[year] += 1
                except ValueError:
                    continue
    
    for year in sorted(blog_counts.keys()):
        print(f"{year}: {blog_counts[year]} blogs")
    
    max_year = max(blog_counts, key=blog_counts.get)
    print(f"\n{max_year} had the most ({blog_counts[max_year]}) blogs.")

    min_year = min(blog_counts, key=blog_counts.get)
    print(f"{min_year} had the least ({blog_counts[min_year]}) blogs.")

print("Blogs by Month:")
count_blogs_by_month('notablog.csv')
print("\nBlogs by Year:")
count_blogs_by_year('notablog.csv')
