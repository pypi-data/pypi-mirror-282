import pandas as pd
import pkg_resources

# Load the dataset
data_path = pkg_resources.resource_filename(__name__, 'Complete_Indigenous_Land_Claims_and_Lawsuits.csv')
df = pd.read_csv(data_path)

def get_full_list():
    print(df)

def get_case(title):
    case = df[df['Title'].str.contains(title, case=False, na=False)]
    if not case.empty:
        print(case)
    else:
        print("Case not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Get the full list of cases")
        print("2. Search for a specific case by title")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_full_list()
        elif choice == '2':
            title = input("Enter the title or part of the title of the case: ")
            get_case(title)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
