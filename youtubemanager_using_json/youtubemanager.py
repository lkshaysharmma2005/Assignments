import json


def load_data():
    try:
        with open("youtube3.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube3.txt','w') as file:
        return json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']},Duration: {video['time']}")

def add_videos(videos):
    name = input("Enter the name of the video :")
    time = input("Enter the time : ")
    videos.append({"name":name , "time":time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter a number of a video to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Enter a valid index number!")


def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter a number of a video to delete : "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Enter a valid index number!")


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()