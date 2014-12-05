from unittest import TestCase
from src.Departamento import *
from mockito import *

__author__ = 'ezequiel'


class TestDepartamento(TestCase):

    def test_get_salario_total(self):
        """
        test_get_salario_total

        Tests get_salario_total() method from Departamento class
        :return: void
        """

        # create emp mocks
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)

        # define methods
        when(e1).get_salario().thenReturn(1000.0)
        when(e2).get_salario().thenReturn(1000.0)
        when(e3).get_salario().thenReturn(1000.0)

        # create department
        dpt = Departamento("Contabilidad", 1)

        # empty dpt
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 0.0)

        # add the first employee
        dpt.add_empleado(e1)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 1000.0)

        # add second employee
        dpt.add_empleado(e2)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 2000.0)

        # add third employee
        dpt.add_empleado(e3)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 3000.0)


    def test_get_salario_total_anual(self):
        """
        test_get_salario_total_anual

        Tests get_salario_total_anual() method from Departamento class
        :return: void
        """

        # create emp mocks
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)

        # define methods
        when(e1).get_salario().thenReturn(1000.0)
        when(e2).get_salario().thenReturn(1000.0)
        when(e3).get_salario().thenReturn(1000.0)

        # create department
        dpt = Departamento("HR", 2)

        # empty dpt
        self.assertIsNotNone(dpt.get_salario_total_anual())
        self.assertIsInstance(dpt.get_salario_total_anual(), float)
        self.assertEqual(dpt.get_salario_total_anual(), 0.0)

        # add the first employee
        dpt.add_empleado(e1)
        self.assertIsNotNone(dpt.get_salario_total_anual())
        self.assertIsInstance(dpt.get_salario_total_anual(), float)
        self.assertEqual(dpt.get_salario_total_anual(), 1000.0 * 12)

        # add second employee
        dpt.add_empleado(e2)
        self.assertIsNotNone(dpt.get_salario_total_anual())
        self.assertIsInstance(dpt.get_salario_total_anual(), float)
        self.assertEqual(dpt.get_salario_total_anual(), 2000.0 * 12)

        # add third employee
        dpt.add_empleado(e3)
        self.assertIsNotNone(dpt.get_salario_total_anual())
        self.assertIsInstance(dpt.get_salario_total_anual(), float)
        self.assertEqual(dpt.get_salario_total_anual(), 3000.0 * 12)