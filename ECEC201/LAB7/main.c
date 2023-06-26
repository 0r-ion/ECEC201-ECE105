#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *ifp;
    FILE *ofp;
    int count = 0;
    int curln;
    int c;
    int linenum = 1;
    ifp = fopen("lore.txt", "r");
    ofp = fopen("count.txt", "w");
    if (!ifp || !ofp)
    {
        fprintf(stderr, "file pointer(s) failed to open");
        return 1;
    }
    /*count spaces*/
    while ((c = fgetc(ifp)) != EOF)
    {
        if(c == '\n')
        {
            fprintf(ofp, "%d:%d\n", linenum , count);
            count = 0;
            linenum++;
            continue;
        }
        count++;
    }
    fprintf(ofp, "%d:%d\n", linenum, count);
    return 0;
}