#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);

	/* Get the wide character string */
	Py_ssize_t size;
	wchar_t *wide_str = PyUnicode_AsWideCharString(p, &size);

	if (wide_str != NULL)
	{
		printf("  value: %ls\n", wide_str);
		/* Free the allocated wide character string */
		PyMem_Free(wide_str);
	}
	else
	{
		printf("  [ERROR] Unable to retrieve string value\n");
	}
}
