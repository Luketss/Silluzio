import os
import csv
import json
import re

db = {}


def get_csv_files_in_dir(dir_path=None, file_extension=".csv") -> list:
    """
    Returns a list of CSV file names in the specified directory.
    :param dir_path: The directory path to search for CSV files in. If None, the current working directory is used.
    :param file_extension: The file extension to search for. Default is ".csv".
    :return: A list of CSV file names.
    """
    dir_path = dir_path or os.getcwd()
    if not os.path.exists(dir_path):
        raise ValueError(f"Directory path {dir_path} does not exist.")
    csv_files = [
        os.path.join(dir_path, file)
        for file in os.listdir(dir_path)
        if file.endswith(file_extension)
    ]
    return csv_files


def file_content_to_dict(file_path: str) -> list[dict]:
    """
    This function takes a file path as input and returns a list of dictionaries containing the data from the CSV file. The function uses the csv module to read the file and convert it to a list of dictionaries. If the file cannot be opened or read, the function prints an error message and returns an empty list.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = list(csv.DictReader(f))
    except OSError as e:
        print(f"Error opening or reading file '{file_path}': {e}")
        data = []
    return data


def split_file_name(name: str) -> str:
    new_name = re.sub(".csv", "", name.split("\\")[::-1][0])
    return new_name


def extract_filename(filepath: str) -> str:
    if not isinstance(filepath, str):
        raise TypeError("Input filename should be a string")
    if not filepath.endswith(".csv"):
        raise ValueError("Input filename should end with .csv extension")
    filename, _ = os.path.splitext(os.path.basename(filepath))
    return filename


def write_dict_to_csv(name_file, dict_data: dict):
    # Get the keys -- to fix
    keys = list(set(k for d in dict_data.values() for k in d.keys()))

    # Get the values and split them
    values = [list(d.values()) for d in dict_data.values()]

    # Save to CSV
    with open(name_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(keys)
        writer.writerows(values)


def test_f(file_list: list):
    """
    Main function to anwser the questions:
    1. For every legislator in the dataset, how many bills did the legislator support (voted for the
    bill)? How many bills did the legislator oppose?
    2. For every bill in the dataset, how many legislators supported the bill? How many legislators
    opposed the bill? Who was the primary sponsor of the bill?
    Output two files with the result of 1 and 2. (and a database file to follow up)
    """
    for file in file_list:
        new_name = split_file_name(file)
        db[f"{new_name}"] = file_content_to_dict(file)

    legislator_counts = {}
    with open("database_visualizer.json", "w") as d:
        d.write(json.dumps(db))

    for legislator in db["legislators"]:
        id = legislator["id"]
        name = legislator["name"]
        support_count = 0
        oppose_count = 0
        for vote_results in db["vote_results"]:
            if vote_results["legislator_id"] == id:
                if int(vote_results["vote_type"]) == 1:
                    support_count += 1
                if int(vote_results["vote_type"]) == 2:
                    oppose_count += 1

        legislator_counts[legislator["id"]] = {
            "id": id,
            "name": name,
            "support": support_count,
            "oppose": oppose_count,
        }

    write_dict_to_csv("legislators-support-oppose-count.csv", legislator_counts)

    bill_votes = {}
    for vote in db["votes"]:
        support_count = 0
        oppose_count = 0
        sponsor = "Unknown"
        title = ""

        for vote_result in db["vote_results"]:
            if vote_result["vote_id"] == vote["id"]:
                if int(vote_result["vote_type"]) == 1:
                    support_count += 1
                if int(vote_result["vote_type"]) == 2:
                    oppose_count += 1

        for bill in db["bills"]:
            if vote["bill_id"] == bill["id"]:
                title = bill["title"]
                for legislator in db["legislators"]:
                    if bill["sponsor_id"] == legislator["id"]:
                        sponsor = legislator["name"]

        bill_votes[vote["bill_id"]] = {
            "bill_id": vote["bill_id"],
            "title": title,
            "sponsor": sponsor,
            "support": support_count,
            "oppose": oppose_count,
        }

    write_dict_to_csv("legislators-bills.csv", bill_votes)


if __name__ == "__main__":
    files = get_csv_files_in_dir()
    test_f(files)
