#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - prints basic info on python objects
 * @p: PyObject
 */


void print_python_list(PyObject *p)
{
	int list_size, i, list_allocation;
	PyVarObject *var_object = (PyVarObject *)p;
	PyListObject *py_list = (PyListObject *)p;
	const char *element_type;

	list_size = var_object->ob_size;
	list_allocation = py_list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", list_allocation);

	for (i = 0; i < list_size; i++)
	{
		element_type = py_list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, element_type);
		if (strcmp(element_type, "bytes") == 0)
			print_python_bytes(py_list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints basic info of python bytes
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *py_bytes = (PyBytesObject *)p;
	unsigned char byte_size, byte;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", py_bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		byte_size = 10;
	else
		byte_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", byte_size);
	for (byte = 0; byte < byte_size; byte++)
	{
		printf("%02hhx", py_bytes->ob_sval[byte]);
		if (byte == (byte_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
