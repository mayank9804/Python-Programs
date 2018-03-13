def main():
    print("Love form India!")

if __name__ == '__main__':
    main()
else:
    print(__name__)


# If a Python program is directly invoked from the file name
# the namespace (__name__) is set __main__
# Therefore if this file is imported the main() function would
# never get called because then __name__ would get equal to
# name of the file 
