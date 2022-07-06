#include <Python.h>

void print_python_list_info(PyObject *p)
{
        int len_list;

	len_list = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", len_list);
}
