from file_manager import FileManager

def interface():
    fm = FileManager()
    while True:
        print(fm.get_current_path())
        for directory in fm.view_Directories():
            print(f"\t/{directory}")

        for file in fm.view_files():
            print(f"\t {file}")
    
        print("For more information type 'Help'")
        operation = input('What would you like to do ? : ')
        match operation:
            case 'Quit':
                break

            case 'Back':
                fm.move_up()
            
            case 'Go-to':
                fm.move_to_directory()

            case 'CreateF':
                fm.create_file()
            
            case 'RemoveF':
                fm.delete_file()
            
            case 'Rename':
                fm.rename_file()
            
            case 'Move':
                fm.move_file()
            
            case 'Copy':
                fm.copy_file()

            case 'CreateD':
                fm.create_directory()

            case 'RemoveD':
                fm.delete_directory()

            case 'Help':
                print('''
                -Quit: Exit the filemanager application
                -Back: Move up one directory level
                -Go-to: Move to a specific directory
                -CreateF: Create a new file
                -RemoveF: Remove an existing file
                -Rename: Rename an existing file
                -Move: Move a file to a different location
                -Copy: Copy a file to a different location
                -CreateD: Create a new directory
                -RemoveD: Remove an existing directory and all of its content

                '''
                ) 

interface()