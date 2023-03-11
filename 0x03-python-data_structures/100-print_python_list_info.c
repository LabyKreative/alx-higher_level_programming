#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: A pointer to a PyObject list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
