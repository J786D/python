import argparse

if __name__ == "__main__":
    cmd_arg = argparse.ArgumentParser(description="abc")
    cmd_arg.add_argument("name", help="full_name")
    args = cmd_arg.parse_args()
    
    print(args.name)


