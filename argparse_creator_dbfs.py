import os

print(os.listdir())

f = open("code.py", "a")
f.write("import argparse\n")
f.write("\n")
f.write("if __name__ == '__main__':\n")
f.write("    parser = argparse.ArgumentParser(description='test')\n")
f.write("    parser.add_argument('name', help='NAME')\n")
f.write("    args = parser.parse_args()\n")
f.write("    print(args.name)\n")
print("DONE")

