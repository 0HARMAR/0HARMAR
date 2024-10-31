typedef struct {
    char magic[20];  // magic
    int filesize;  //filesize
    int textsize;  //textsize
    int datasize;  //datasize
    void * textptr;  //start of text
    void * dataptr;  // start of data
} UE;

#define UEHEADER 48