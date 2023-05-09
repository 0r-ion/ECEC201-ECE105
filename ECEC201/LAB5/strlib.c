#include <stdio.h>

int my_strlen (const char *str){
    int i = 0;
    while( str[i] != '\0'){
        i++;
    }
    return i;
}
int my_strcmp (const char *str1, const char *str2){
    int i = -1;
    do{
        i++;
        if(str1[i] == '\0'){
            return str1[i] - str2[i];
        } 
    }while (str1[i] == str2[i]);
    return str1[i] - str2[i];

}
