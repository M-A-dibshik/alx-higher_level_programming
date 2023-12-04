#include <python.h>

/**
 * print_python_list_info - Print basic info about python list.
 * @p: A pyobject list
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((PylistObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_Getltem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
