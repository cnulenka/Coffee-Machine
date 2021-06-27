class Results:

    """
        Used for passing errors, warnings, info
        after any operation.
    """

    def __init__(self) -> None:
        self.errors = []
        self.warnings = []
        self.info = []

    def reset_results(self):
        self.errors.clear()
        self.warnings.clear()
        self.info.clear()

    def print_results(self) -> None:
        error_list = self.errors
        if len(error_list) > 0:
            print("\n")
            for error in error_list:
                print("Error: " + error)

        warnings_list = self.warnings
        if len(warnings_list) > 0:
            print("\n")
            for warning in warnings_list:
                print("Warning: " + warning)

        info_list = self.info
        if len(info_list) > 0:
            print("\n")
            for info in info_list:
                print("Info: " + info)

    def append_results(self, results_to_add):
        error_list = results_to_add.errors
        if len(error_list) > 0:
            for error in error_list:
                self.errors.append(error)

        warnings_list = results_to_add.warnings
        if len(warnings_list) > 0:
            for warning in warnings_list:
                self.warnings.append(warning)

        info_list = results_to_add.info
        if len(info_list) > 0:
            for info in info_list:
                self.info.append(info)
