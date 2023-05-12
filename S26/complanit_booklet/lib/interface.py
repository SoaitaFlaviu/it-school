class CLIMenu:

    def __init__(self, program_name, command_map) -> None:
        """command map will have this form:
        {
            "menu_text" : action / menu sub_menu

        }
        
        """
        self.__command_map = command_map
        self.program_name = program_name


    def show_main(self):
        print(f"{self.program_name:=^50}")
