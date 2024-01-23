#include <python.h>

/**
 * print_python_lsit_info - prints basic info about python list
 * @p: A pyobject list.
 */

void print_python_list_info(pyObject *p)
{
    int S, alloc, f;
    pyObject *obj;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the python List = %d\n", S);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);
        obj = Pylist_GetItem(p, i);
        printf("%s\n", Py_Type(obj)->tp_name);
    }
}
