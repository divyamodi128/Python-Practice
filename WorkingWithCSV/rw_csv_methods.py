import csv
import shutil
from tempfile import NamedTemporaryFile
import datetime


def read_data(user_id=None, email=None):
    file_name = "data.csv"
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # print list(reader), user_id, email
        for row in list(reader):
            if user_id is not None and email is None:
                if int(user_id) == int(row['Id']):
                    return row
                else:
                    msg = "No such User with id = {user_id} found.".format(user_id=user_id)
            elif email is not None and user_id is None:
                if email == row['Emailid']:
                    return row
                else:
                    msg = "No such User with email = {email} found.".format(email=email)
            elif user_id is not None and email is not None:
                if int(user_id) == int(row['Id']) and email == row['Emailid']:
                    return row
                else:
                    msg = "No such User with id = {user_id} email = {email} found.".format(user_id=user_id, email=email)
            else:
                return list(reader)
        return msg


read_data(user_id=2)
read_data(email="asd@asd.com")
read_data(user_id=2, email="asd@asd.com")
read_data()


def get_lenght(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)


def append_data(file_path, name, email):
    fieldnames = ['Id', 'Names', 'Emailid']
    next_id = get_lenght(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "Id": next_id,
            "Names": name,
            "Emailid": email,
        })

# append_data("data.csv", "Divya", "asd@asd.com")



def edit_data(edit_id=None, email=None, amt=None, sent=None):
    file_name = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)
    with open(file_name, 'rb') as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['Id', 'Names', 'Emailid', 'Amount', 'Sent', 'Date']
        # fieldnames = list(reader)[0].keys()
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        # print(temp_file.name)
        for row in reader:
            if edit_id is not None and email is None:
                if int(edit_id) == int(row['Id']):
                    row['Amount'] = amt
                    row['Sent']= sent
                    print(row)
            if email is not None and edit_id is not None:
                if int(edit_id) == int(row['Id']) and str(email) == str(row['Emailid']):
                    row['Amount'] = amt
                    row['Sent'] = sent
                    print(row)
            writer.writerow(row)
        shutil.move(temp_file.name,file_name)

# edit_data(4, 6543.2546, True)
# edit_data(edit_id=2, amt=999, sent=False)
# edit_data(edit_id=4, email='asd@asd.com', amt=1000, sent=True)


def delete_data(delete_id=None):
    file_name = "data.csv"
    temp_file = NamedTemporaryFile(delete=False)
    with open(file_name, 'rb') as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        # fieldnames = list(reader)[0].keys()
        fieldnames = ['Id', 'Names', 'Emailid', 'Amount', 'Sent', 'Date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        # print(temp_file.name)
        for row in reader:
            if delete_id is not None:
                if int(delete_id) != int(row['Id']):
                    writer.writerow(row)
                else:
                    print row, "Deleted"
        shutil.move(temp_file.name,file_name)


# delete_data(delete_id=3)

