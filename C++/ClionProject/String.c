/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<stdbool.h>
#define MAXSIZE 100
typedef struct string{
    char *ch;
    int length;
}string;

void create_string(string* s,int n){
    s->ch=(char*) malloc(sizeof (char)*MAXSIZE);
    s->length=0;
    char* p=s->ch;
    for(int i=0;i<n;i++){
        *p=getchar();
        getchar();
        p++;
        (s->length)++;
    }
    *p='\0';
}

void display(string s){
    int n=0;
    char *p=s.ch;
    while(n<s.length){
        printf("%c",*p);
        p++;
        n++;
    }
}

bool string_match(string s,char *sub_string,int len){  //BF算法
    char *p_master=s.ch,*p_sub=sub_string;
    bool flag=true;
    for(int i=0;i<s.length;i++){
        flag=true;
        for(int j=0;j<len;j++){
            if(*p_master!=*p_sub){flag=false;break;}
            p_sub++;p_master++;
        }
        if(flag)return true;
        p_master=s.ch+i+1;
        p_sub=sub_string;
    }
    return false;
}

void string_reserve(string s,char *p,char c)
{
    if(*p=='\0')return;
    else
    {
        string_reserve(s,p+1,s.ch[s.length-(p+2-s.ch)]);
        *p=c;
    }
}
int main(){
    string s;
    create_string(&s,7);
    char sub_string[4]={'a','b','c','d'};
    if(string_match(s,sub_string,4))printf("match");
    else printf("not match");
    string_reserve(s,s.ch,*(s.ch+s.length-1));
    display(s);
}*/