#include "macrobox.h"

int main(int argc, char *argv[]) {
    int a = 2;
    PyObject *str = PyLong_FromLong(a);

    const char *code =
      "a = 10\n"
      "print(f\"hello {a} {str}\")";
    python(code);
}
