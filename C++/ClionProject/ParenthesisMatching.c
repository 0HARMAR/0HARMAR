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

void push(LinkStack *LS,char data){  //��Ԫ��ѹ��ջ
    LinkStack linkstack=(LinkStack) malloc(sizeof (LStack));
    linkstack->data=data;
    linkstack->next=*LS;
    *LS=linkstack;
}

void pop(LinkStack* LS){  //����ջ��Ԫ��
    LinkStack ls=*LS;
    (*LS)=(*LS)->next;
    free((LinkStack)(ls));
}

int main(){
    LinkStack L;
    init_link_stack(&L);
    char ParString[100];
    char *parString=ParString;
    printf("������������ַ���\n");
    gets(parString);
    while(*parString!='\0'){
        if (*parString == '(' || *parString == '[' || *parString == '{')
        {
            push(&L,*parString);
            parString++;
        }
        else if(*parString == ')'){
            if(L->data=='('){  //�����ŵ���ջ��Ԫ�أ�ƥ�䣬��ջ
                pop(&L);
                parString++;
            }
            else{
                printf("���Ų�ƥ��");
                return 0;
            }
        }
        else if(*parString == ']'){
            if(L->data=='['){  //�����ŵ���ջ��Ԫ�أ�ƥ�䣬��ջ
                pop(&L);
                parString++;
            }
            else{
                printf("���Ų�ƥ��");
                return 0;
            }
        }
        else if(*parString == '}'){
            if(L->data=='{'){  //�����ŵ���ջ��Ԫ�أ�ƥ�䣬��ջ
                pop(&L);
                parString++;
            }
            else{
                printf("���Ų�ƥ��");
                return 0;
            }
        }
    }
    if(L!=NULL){  //���ջΪ����ƥ��ɹ�������ʧ��
        printf("���Ų�ƥ��,ջ��Ϊ��");
    }
}*/