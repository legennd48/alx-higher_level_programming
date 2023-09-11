#include <Python.h>
#include <object.h>
#include <listobject.h>


void print_python_list_info(PyObject *pyList)
{
	Py_ssize_t listSize, allocatedSize, index;

	listSize = PyList_Size(pyList);
	allocatedSize = ((PyListObject *)pyList)->allocated;
	printf("[*] Size of the Python List = %ld\n", listSize);
	printf("[*] Allocated = %ld\n", allocatedSize);
	for (index = 0; index < listSize; index++)
	{
		printf("Element %ld: %s\n", index,
		       (PY_TYPE(PyList_GetItem(pyList, index)))->tp_name);
	}
}
