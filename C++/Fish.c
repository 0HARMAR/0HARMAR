#include "macrobox.h"
#include <unistd.h>

void gen_fish();
void gen_fish_right();

int main()
{
    setbuf(stdout,NULL);
    int nfish;scanf("%d",&nfish);
    FORI(nfish)
    {
        gen_fish_right();
        sleep(1);
    }
}

void gen_fish_left()
{
    printf("<><_");
}

void gen_fish_right()
{
    printf("_><>");
}

void move()
{
    printf("---  ");
}
