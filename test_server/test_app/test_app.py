import requests
import os

# check if the serves response with the correct code
def test_servers():
    
    try:
        response1 = requests.get('http://nginx_servers:8081')
        if response1.status_code != 200:
            print("Custom server test failed")
            return False

        response2 = requests.get('http://nginx_servers:8082')
        if response2.status_code != 500:
            print("Error server test failed")
            return False

        print("All tests passed successfully")
        return True

    except Exception as e:
        print(f"Test failed with error: {e}")
        return False

#  creates a file with a name according to the test result
def main():
    success = test_servers()

    if success:
        with open("/result/succeeded", "w"):
            print("created succeeded file")
    else:
        with open("/result/fail", "w"):
            print("created fail file")


if __name__ == "__main__":
    main()
