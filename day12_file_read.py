# file_read

# --- Which commands did we use in our project? ---
    # We use the `try-except` statement to handle potential errors 
        # that might occur during the execution of the code within the `try` block.
    # If any error occurs during the execution of the code inside the "try" block, Python will throw an exception.
    # We use multiple "except" blocks to catch specific types of exceptions:
    # strip()  ==> Removes the first and last characters from a string. By default, the character removed is a space.
    # split()  ==> 
                    # Total Hours :34.0
                    # This command, `split(":")[1]`, splits the sentence at the point where you see ":" to create a list.
                    # ["Total Hours", " 34.0"]
                    # [0] → "Total Hours"
                    # [1] → " 34.0"
                    # This is a list index. Indexes in lists start from 0.
                    # We want to get only the number, not the word "Total Hours".
                    # That's why we wrote it as [1].

# File reading (r)
# readlines()
# string split()
# simple data parsing
# extracting data to a list
# small analysis

def read_reports():
    try:
        with open("study_report.txt", "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("No report file found!")
        return []
    
lines = read_reports()

if not lines:
    print("No Data To Analyze.")
else:
    print("\n--- Previous Study Reports ---")

    totals = []
    averages = []

    for line in lines:
        if "Total Hours :" in line:
            totals.append(float(line.split(":")[1].strip()))
        if "Average Hours :" in line:
            averages.append(float(line.split(":")[1].strip()))

    print(f"Number of past records: {len(averages)}")
    print(f"Best total hours ever: {max(totals)}")
    print(f"Highest average ever: {max(averages):.2f}")