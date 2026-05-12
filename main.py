import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.ui.dashboard import Dashboard

def main():
    print("Starting School Cashier Queue System...")
    app = Dashboard()
    app.mainloop()

if __name__ == "__main__":
    main()