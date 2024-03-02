from app import *

if __name__ == '__main__':

    with app.app_context():
        
        print(AccountCode.get_labels())