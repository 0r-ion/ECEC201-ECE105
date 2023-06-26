#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

#ifndef LINESIZE
#define LINESIZE 10
#endif

/* prints a line of 10 bytes (max) in hex with a space between each byte */
void print_bytes_hex(unsigned char *b, unsigned int nbytes)
{
  int i;
  for (i = 0; i < LINESIZE; i++)
  {
    (i < nbytes) ? printf("%02X ", b[i]) : printf("   ");
  }
  printf(" ");
}

/* prints a line of 10 bytes (max) in as characters.
 * non-printable bytes are printed as the period character. */
void print_bytes_char(unsigned char *b, unsigned int nbytes)
{
  int i;
  for (i = 0; i < nbytes; i++)
  {
    if (isprint(b[i]))
    {
      printf("%c", b[i]);
    }
    else
    {
      printf(".");
    }
  }
}

int main()
{
  FILE *fp = fopen("test.dat", "rb");
  unsigned char data[LINESIZE];
  int ret;
  int offset = 0;

  printf("Offset              Bytes              Characters\n");
  printf("------  -----------------------------  ----------\n");

  while (ret = fread(data, sizeof(*data), LINESIZE, fp))
  {
    printf("%6d  ", offset);
    print_bytes_hex(data, ret);
    print_bytes_char(data, ret);
    printf("\n");
    offset = offset + 10;
  }

  return 0;
}