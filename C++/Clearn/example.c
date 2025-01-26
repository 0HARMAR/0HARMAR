#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 学生结构体
typedef struct {
    char name[50];
    int grade;
} Student;

Student* students = NULL;  // 学生数组
int studentCount = 0;      // 当前学生数量

// 函数声明
void addStudent();
void printStudent(const Student* student);
void printAllStudents();
void calculateAverage();
void findMaxGrade();
void findMinGrade();
void printSummary();

int main() {
    int choice;

    // 动态分配内存来存储学生信息
    students = (Student*)malloc(sizeof(Student) * 100);

    do {
        // 显示菜单
        printf("\nStudent Management System\n");
        printf("1. Add Student\n");
        printf("2. Print All Students\n");
        printf("3. Calculate Average Grade\n");
        printf("4. Find Max Grade\n");
        printf("5. Find Min Grade\n");
        printf("6. Print Summary\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        // 根据用户选择调用不同的函数
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                printAllStudents();
                break;
            case 3:
                calculateAverage();
                break;
            case 4:
                findMaxGrade();
                break;
            case 5:
                findMinGrade();
                break;
            case 6:
                printSummary();
                break;
            case 0:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 0);

    // 释放内存
    free(students);
    return 0;
}

// 添加学生函数
void addStudent() {
    if (studentCount >= 100) {
        printf("Cannot add more students.\n");
        return;
    }

    printf("Enter student's name: ");
    getchar();  // 清空缓冲区中的换行符
    fgets(students[studentCount].name, 50, stdin);
    students[studentCount].name[strcspn(students[studentCount].name, "\n")] = '\0';  // 去除换行符

    printf("Enter student's grade: ");
    scanf("%d", &students[studentCount].grade);

    studentCount++;
    printf("Student added successfully!\n");
}

// 打印学生信息
void printStudent(const Student* student) {
    printf("Name: %s, Grade: %d\n", student->name, student->grade);
}

// 打印所有学生信息
void printAllStudents() {
    if (studentCount == 0) {
        printf("No students to display.\n");
        return;
    }

    for (int i = 0; i < studentCount; i++) {
        printStudent(&students[i]);
    }
}

// 计算所有学生的平均分
void calculateAverage() {
    if (studentCount == 0) {
        printf("No students available to calculate average.\n");
        return;
    }

    int sum = 0;
    for (int i = 0; i < studentCount; i++) {
        sum += students[i].grade;
    }

    printf("Average grade: %.2f\n", (float)sum / studentCount);
}

// 查找最高分
void findMaxGrade() {
    if (studentCount == 0) {
        printf("No students to find max grade.\n");
        return;
    }

    int maxGrade = students[0].grade;
    for (int i = 1; i < studentCount; i++) {
        if (students[i].grade > maxGrade) {
            maxGrade = students[i].grade;
        }
    }

    printf("Max grade: %d\n", maxGrade);
}

// 查找最低分
void findMinGrade() {
    if (studentCount == 0) {
        printf("No students to find min grade.\n");
        return;
    }

    int minGrade = students[0].grade;
    for (int i = 1; i < studentCount; i++) {
        if (students[i].grade < minGrade) {
            minGrade = students[i].grade;
        }
    }

    printf("Min grade: %d\n", minGrade);
}

// 打印学生汇总信息
void printSummary() {
    if (studentCount == 0) {
        printf("No students to summarize.\n");
        return;
    }

    printf("\nStudent Summary:\n");
    printAllStudents();
    calculateAverage();
    findMaxGrade();
    findMinGrade();
}
