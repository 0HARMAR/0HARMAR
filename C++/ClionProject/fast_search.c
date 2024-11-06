#include <stdio.h>

#define MAXSIZE 50
typedef int ElemType;

typedef struct {
    ElemType r[MAXSIZE + 1];
    int length;
} SqList;

void Create(SqList *L);
int Partition(SqList *L, int low, int high);
void QuickSort(SqList *L, int low, int high);
void Print(SqList L);

void Create(SqList *L) {
    int i;
    scanf("%d", &L->length);
    for (i = 1; i <= L->length; i++)
        scanf("%d", &L->r[i]);
}

int Partition(SqList *L, int low, int high) {
    L->r[0] = L->r[low];
    while (low < high) {
        while (low < high && L->r[high] >= L->r[0])
            high--;
        L->r[low] = L->r[high];
        while (low < high && L->r[low] <= L->r[0])
            low++;
        L->r[high] = L->r[low];
    }
    L->r[low] = L->r[0];
    return low;
}

void QuickSort(SqList *L, int low, int high) {
    int i;
    if (low < high) {
        i = Partition(L, low, high);
        QuickSort(L, low, i - 1);
        QuickSort(L, i + 1, high);
    }
}

void Print(SqList L) {
    int i;
    if (L.length == 0)
        return;
    printf("%d", L.r[1]);
    for (i = 2; i <= L.length; i++)
        printf(" %d", L.r[i]);
    printf("\n");
}

int main() {
    SqList L;
    int low, high;
    Create(&L);
    low = 1;
    high = L.length;
    QuickSort(&L, low, high);
    Print(L);
    return 0;
}
