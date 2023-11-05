import sys
import os

if len(sys.argv) < 2:
    exit()


def seed_database():
    import db.tables


if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

    if sys.argv[1] == "seed":
        seed_database()
    elif sys.argv[1] == "drop-all":
        from db import tables

        tables.drop_all()
