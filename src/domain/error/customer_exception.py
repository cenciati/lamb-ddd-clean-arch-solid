# pylint: disable=missing-class-docstring


class CustomerNotFoundError(Exception):
    message = "Could not find specified customer."

    def __str__(self):
        return CustomerNotFoundError.message


class CustomersNotFoundError(Exception):
    message = "Could not find any customer."

    def __str__(self):
        return CustomersNotFoundError.message


class CustomerDuplicateEmailError(Exception):
    message = "Customer with specified email already exists."

    def __str__(self):
        return CustomerDuplicateEmailError.message


class CustomerDuplicateCpfError(Exception):
    message = "Customer with specified cpf already exists."

    def __str__(self):
        return CustomerDuplicateCpfError.message
