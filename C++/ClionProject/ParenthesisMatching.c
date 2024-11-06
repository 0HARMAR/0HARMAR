/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>


typedef struct LinkStack{
    char data;
    struct LinkStack*next;
}LStack,*LinkStack;

void init_link_stack(LinkStack *LS){
    *LS=NULL;
}

void push(LinkStack *LS,char data){  //将元素压入栈
    LinkStack linkstack=(LinkStack) malloc(sizeof (LStack));
    linkstack->data=data;
    linkstack->next=*LS;
    *LS=linkstack;
}

void pop(LinkStack* LS){  //弹出栈顶元素
    LinkStack ls=*LS;
    (*LS)=(*LS)->next;
    free((LinkStack)(ls));
}

int main(){
    LinkStack L;
    init_link_stack(&L);
    char ParString[100];
    char *parString=ParString;
    printf("请输入待检查的字符串\n");
    gets(parString);
    while(*parString!='\0'){
        if (*parString == '(' || *parString == '[' || *parString == '{')
        {
            push(&L,*parString);
            parString++;
        }
        else if(*parString == ')'){
            if(L->data=='('){  //右括号等于栈顶元素，匹配，出栈
                pop(&L);
                parString++;
            }
            else{
                printf("括号不匹配");
                return 0;
            }
        }
        else if(*parString == ']'){
            if(L->data=='['){  //右括号等于栈顶元素，匹配，出栈
                pop(&L);
                parString++;
            }
            else{
                printf("括号不匹配");
                return 0;
            }
        }
        else if(*parString == '}'){
            if(L->data=='{'){  //右括号等于栈顶元素，匹配，出栈
                pop(&L);
                parString++;
            }
            else{
                printf("括号不匹配");
                return 0;
            }
        }
    }
    if(L!=NULL){  //最后栈为空则匹配成功，否则失败
        printf("括号不匹配,栈不为空");
    }
}*/