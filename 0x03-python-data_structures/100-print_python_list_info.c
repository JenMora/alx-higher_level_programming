#include "Python.h"
/**
*print_python_list_info - Prints information about python objects
*@p: PyObject pointer to print info about
*/
void print_python_list_info(PyObject *p)
{

Py_ssize_t a, py_list_size;

PyObject *item;

const char *item_type;

PyListObject *list_object_cast;

list_object_cast = (PyListObject *)p;

py_list_size = PyList_Size(p);

printf("[*] Size of the Python List = %d\n", (int) py_list_size);

printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);

for (a = 0; a < py_list_size; a++)
{
item = PyList_GetItem(p, a);

item_type = Py_TYPE(item)->tp_name;

printf("Element %d: %s\n", (int) a, item_type);
}
}
