import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # your code here
    directory = 'download'
    parent_directory = 'C:/Users/Admin/sf/depract'
    path = os.path.join(parent_directory,directory)

    try:
        os.mkdir(path)
    except OSError as e:
        print(e)

    os.chdir(path)
    print(path)
    
    for url in download_uris:
        file_name = url.split('/')[-1]
        r = requests.get(url,allow_redirects = True)
        f = open(file_name,'wb')
        print('file is  downloaded in download folder......')
        f.write(r.content)
        try:
            shutil.unpack_archive(file_name,path)
            f.close()
            os.remove(file_name)
            print(file_name + ' is deleted after extraction')
        except OSError as e:
            print(e)

    pass


if __name__ == "__main__":
    main()
