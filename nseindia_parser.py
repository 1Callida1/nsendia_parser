from nseindia_parser_helper import *

def main():
    helper = Helper()

    helper.go_to_main_page()

    print("[Log] Starting an activity")
    helper.first_activity()
    print("[Log] Activity was complete")

    print("[Log] Starting parsing")
    helper.parse_data()
    print("[Log] Writing and parsing was finished")

    print("[Log] Starting an fake activity")
    helper.fake_activity()
    print("[Log] Fake activity was complete")

    helper.close_driver()
    print("[Log] Driver was closed, program is completed correctly")
    

if __name__ == "__main__": 
    main()