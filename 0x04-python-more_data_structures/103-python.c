#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print basic info about a Python list
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Print basic info about a Python bytes object
 * @p: PyObject pointer to the Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_data;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		return;

	size = PyBytes_Size(p);
	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size < 10)
		printf("  first %ld bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	bytes_data = PyBytes_AsString(p);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02hhx", bytes_data[i]);
	printf("\n");
}
