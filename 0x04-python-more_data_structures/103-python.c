#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 *
 * @p: Python bytes object.
 *
 * Return: No return value.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	ssize_t len, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %zd\n", len);
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes: ", len < 10 ? len + 1 : 10);
	for (i = 0; i < len && i < 10; i++)
		printf("%02hhx%c", str[i], i + 1 < len && i + 1 < 10 ? ' ' : '\n');
}

/**
 * print_python_list - prints some basic info about Python lists.
 *
 * @p: Python list object.
 *
 * Return: No return value.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	ssize_t size, i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", Py_SIZE(list));
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0, size = Py_SIZE(list); i < size; i++)
	{
		printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
	}
}
