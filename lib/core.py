class Core:
    @staticmethod
    def version() -> str:
        return "1.0.0"

    @staticmethod
    def email() -> str:
        return "abhiea37@ea37.com"

    @staticmethod
    def developer() -> str:   
        return "Abhijith E A"

        
    @staticmethod
    def banner() -> None:
        print("\033[32m***************************************************************************************")
        print("*                                                                                     *")
        print("*                        __                                   __                      *")
        print("*        ____ ___  ___  / /_____ _____ ___  ____  _________  / /_  ____  ________     *")
        print("*       / __ `__ \/ _ \/ __/ __ `/ __ `__ \/ __ \/ ___/ __ \/ __ \/ __ \/ ___/ _ \    *")
        print("*      / / / / / /  __/ /_/ /_/ / / / / / / /_/ / /  / /_/ / / / / /_/ (__  )  __/    *")
        print("*     /_/ /_/ /_/\___/\__/\__,_/_/ /_/ /_/\____/_/  / .___/_/ /_/\____/____/\___/     *")
        print("*                                                  /_/                                *")
        print("*                                                                                     *")
        print(f"*  metamorphose {Core.version()}                                                                 *")
        print(f"*  Coded by {Core.developer()}                                                              *")
        print("*  EA37                                                                               *")
        print(f"*  {Core.email()}                                                                  *")
        print("***************************************************************************************")