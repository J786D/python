import argparse

cmd_args = argparse.ArgumentParser(description="Name")
cmd_args.add_argument("first_name", help="fname")
cmd_args.add_argument("last_name", help="lname")
args = cmd_args.parse_args()

if __name__ == "__main__":
    x = "Hello {} is your firstname and {} is last name !!!".format(args.first_name, args.last_name)
    print(x)
