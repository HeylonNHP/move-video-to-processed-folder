import os


def search_filenames(search_string, file_list):
    matching_files = []
    for file_name in file_list:
        base_name, ext = os.path.splitext(file_name)
        if base_name.startswith(search_string):
            matching_files.append(file_name)
    return matching_files


def process_video_files(directory_path):
    # create a new directory called "processed"
    processed_dir = os.path.join(directory_path, "processed")
    os.makedirs(processed_dir, exist_ok=True)

    # get a list of all files and directories in the specified directory
    file_list = os.listdir(directory_path)

    for file_name in file_list:
        # check if the file is a video file
        ext = os.path.splitext(file_name)[1]
        if ext in [".gif", ".mp4", ".mov", ".webm"]:
            # check if the file starts with the prefix
            if file_name.startswith("60.00fps-TargetFPS-mode3-rife-"):
                # remove the prefix and move the file to the "processed" directory
                new_file_name = file_name[len("60.00fps-TargetFPS-mode3-rife-"):]
                os.rename(os.path.join(directory_path, file_name), os.path.join(processed_dir, new_file_name))

                # See if corresponding source file exists
                matching_files = search_filenames(new_file_name[:new_file_name.rindex(".")], file_list)
                if len(matching_files) > 0:
                    matching_file = matching_files[0]
                    matching_file_ext = matching_file[matching_file.rindex("."):]
                    # add a "-" to the end of the filename before the file extension
                    new_file_name_non_interp = matching_file.split(matching_file_ext)[0] + "-" + ext
                    os.rename(os.path.join(directory_path, matching_file),
                              os.path.join(processed_dir, new_file_name_non_interp))


def main():
    while True:
        # prompt the user for a directory path
        directory_path = input("Enter a directory path: ")

        # check if the directory exists
        if os.path.isdir(directory_path):
            process_video_files(directory_path)
            break
        else:
            print("Error: Directory does not exist.")


main()
