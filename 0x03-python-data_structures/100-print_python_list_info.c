#include <Python.h>

/**
 * print_python_list_info - prints basic info about python list
 * @p: pointer to a Python object of type PyObject
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *item;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
