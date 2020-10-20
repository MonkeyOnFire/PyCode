from selenium import webdriver

def main():
    file = open("./a.txt","x")
    file.write("aaa")
    file.close()
if __name__ == '__main__':
    main()
