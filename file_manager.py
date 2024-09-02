import os, shutil

class FileManager:
    def __init__(self):
        self.__directory = "/home/aziz" 
    
    def get_current_path(self):
        return(self.__directory)
    
    def move_up(self):
        if self.__directory == "/":
            return
        else: self.__directory = os.path.dirname(self.__directory)

    def move_to_directory(self):
        while True: 
            directory = input('Enter the directory path you want to go to: ')
            directory_path = os.path.join(self.__directory, directory)
            try: 
                if not os.path.isdir(directory_path):
                    raise FileNotFoundError(f"Directory {directory_path} does not exist")
                self.__directory = directory_path
                break
            except Exception as e:
                print(f"An error occured {e}")


    def view_files(self):
        all_files = [file for file in os.listdir(self.__directory) if os.path.isfile(os.path.join(self.__directory, file))]
        files = list(filter(lambda file : not file.startswith('.'), all_files))
        return files

    def create_file(self):
        while True:
            file_name = input('Enter the name for the file you want to create: ')
            if file_name.strip():
                with open(os.path.join(self.__directory, file_name), 'w') as file:
                    break
                
            else:
                print("Invalid filename")

    def delete_file(self):
        while True:
            file_to_delete = input('Enter the name for the file you want to delete: ')
            file_path = os.path.join(self.__directory, file_to_delete)
            try :
                os.remove(file_path)
                break
            except FileNotFoundError:
                print(f"File {file_path} does not exist")
            except PermissionError:
                print(f"Permission Denied cannot delete {file_path}")
            except Exception as e:
                print(f"An error occured {e}")

    def rename_file(self):
        while True:
            file_to_rename = input('Enter the name for the file/directory you want to rename: ')
            file_path = os.path.join(self.__directory, file_to_rename)
            try :
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File/Directory {file_path} does not exist")
                elif file_to_rename == "":
                    raise FileNotFoundError(f"File/Directory {file_path} does not exist")
                while True:
                    new_name = input('new name: ')
                    if new_name == '':
                        print("Invalid filename/directoryname")
                    else:
                        new_path = os.path.join(self.__directory, new_name)
                        if os.path.exists(new_path):
                            print(f"A file/directory with the name '{new_name}' already exists.")
                        else:
                            os.rename(file_path, os.path.join(self.__directory, new_name))
                            break
                break    
            except PermissionError:
                print(f"Permission Denied cannot rename {file_path}")
            except Exception as e:
                print(f"An error occured {e}")

    def move_file(self):
        while True:
            file_to_move = input('Enter the name for the file/directory you want to move: ')
            file_path = os.path.join(self.__directory, file_to_move)
            move_path = input('Enter the destination (full path required!):')
            destination_path = os.path.join(move_path, file_to_move)

            if file_to_move == "":
                print('Invalid path provided')
                continue
            if not os.path.exists(file_path):
                print(f"The source file/directory '{file_path}' does not exist.")
                continue

            if not os.path.isdir(move_path):
                print(f"The destination '{move_path}' is not a valid directory.")
                continue

            if  os.path.exists(destination_path):
                print(f"The destination file/directory '{destination_path}' already exists.")
                continue
            try:  
                shutil.move(file_path, destination_path)
                break
            except PermissionError:
                print(f"Permission Denied cannot move {file_path}")    
            except ValueError:
                print('Invalid path provided')
            except OSError as e:
                print(f"An error occured {e}")
            except Exception as e:
                print(f"An error occured {e}")

    def copy_file(self):
        while True:
            file_to_copy = input('Enter the name for the file/directory you want to copy: ')
            file_path = os.path.join(self.__directory, file_to_copy)
            base_name, extension = os.path.splitext(file_path)
            copy_name = f"{base_name}_copy{extension}"

            if file_to_copy == "":
                print('Invalid path provided')
                continue
            if not os.path.exists(file_path):
                print(f"The source file/directory '{file_path}' does not exist.")
                continue
            try:
                shutil.copy(file_path, copy_name)
                break
            except PermissionError:
                print(f"Permission Denied cannot copy {file_path}")
            except ValueError:
                print('Invalid path provided')
            except OSError as e:
                print(f"An error occured {e}")
            except Exception as e:
                print(f"An error occured {e}")   

    def view_Directories(self):
        all_directories = [directory for directory in os.listdir(self.__directory) if os.path.isdir(os.path.join(self.__directory, directory))]
        directories = list(filter(lambda directory : not directory.startswith('.'), all_directories))
        return directories

    def create_directory(self):
        while True:
            directory_name = input('Enter the name of the directory you want to create: ')
            if directory_name.strip():
                os.mkdir(os.path.join(self.__directory, directory_name))
                break
            else: print('Invalid directory name')

    def delete_directory(self):
        prompt = input("This will remove the directory and all it's content do you still want to proceed [y/n]? :")
        if prompt == 'y':
            directory_to_delete = input('Enter the name of the directory you wish to delete: ')
            if not directory_to_delete :
                print('Invalid directory name')
                return
            directory_path = os.path.join(self.__directory, directory_to_delete)

            if not os.path.exists(directory_path):
                print('Directory does not exist.')
                return
                
            try:
                shutil.rmtree(directory_path)
            except Exception as e:
                print(f"An error occured: {e}")
        else: return



