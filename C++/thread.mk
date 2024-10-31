CC = gcc

CFLAGS = -lpthread -g 

SRC =" "

TARGET = a.out

$(TARGET) :
	$(CC) $(SRC) $(CFLAGS) -o $(TARGET)

.PHONY :clean

clean:
	rm $(TARGET)

.PHONY :run

run:
	./$(TARGET)