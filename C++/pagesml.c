#include<stdio.h>
#include<malloc.h>
#include<assert.h>
#include<sys/mman.h>

#ifdef _WIN32
#else
    #define __int32 __int32_t
#endif

#define PADDRSPC 4096  //4096 physical memory space
#define PAGESIZE 4  //4 byts per page
#define NPAGE PADDRSPC/PAGESIZE  //num of pages
#define CADDR(PAGENUB) (PAGENUB*PAGESIZE)  //calculate physical page addr for given page num

#define BADPAGENUM -1
void *addrstart;  //physical memory addr start

typedef struct pscpagetable  //physical page table
{
    int pagenumber[NPAGE];
    int npage;
}pscpagetable;


__int32 rpage(pscpagetable pt,int pagenum);  //read a data
int wpage(pscpagetable pt,__int32 data,int pagenum);  //write a page

int main()
{
    addrstart=malloc(PADDRSPC);  //physical 4096 bytes memory

    assert(addrstart!=NULL);  //malloc succeed

    mprotect(addrstart, PADDRSPC, PROT_READ | PROT_WRITE | PROT_EXEC);  //add exec permission

    
    pscpagetable pt;
    pt.npage=NPAGE;
    for(int i=0;i<NPAGE;i++)  //alloc page number for per page
    {
        pt.pagenumber[i]=i+1;
    }

    wpage(pt,114514,514);
    printf("%d",rpage(pt,514));
}


__int32 rpage(pscpagetable pt,int pagenum)
{
    assert(CADDR(pagenum)+addrstart!=NULL);
    return *(__int32*)(CADDR(pagenum)+addrstart);
}

int wpage(pscpagetable pt,__int32 data,int pagenum)
{
    if(pagenum>1024||pagenum<1)return BADPAGENUM;
    *(__int32*)(CADDR(pagenum)+addrstart)=data;
    return 0;
}
