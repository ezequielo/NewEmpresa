__author__ = 'ezequiel'

class Empleado:

    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Init function

        :param nombre: Employee's name
        :param apellidos: Employee's surname
        :param dni: Employee's ID
        :param direccion: Employee's addres
        :param edad: Employee's age
        :param email: Employee's email
        :param salario: Employee's salary
        :param self: Employee
        """

        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario


    def get_salario(self):
        """
        Get salario function

        :return: employee's salary
        """

        return self.salario


    def get_dni(self):
        """
        Get DNI function

        :return: employee's ID
        """

        return self.dni


    def get_nombre_apellidos(self):
        """
        Get name and surname function

        :return: employee's name and surname
        """

        return self.apellidos + ', '  + self.nombre


    def get_edad(self):
        """
        Get age function

        :return: employee's age
        """

        return self.edad


    def get_email(self):
        """
        Get email function

        :return: employee's email
        """

        return self.email


    def get_direccion(self):
        """
        Get address function

        :return: employee's address
        """

        return self.direccion


    def get_salario_anual(self):
        """
        Get salary function

        :return: annual salary
        """

        return self.salario * 12