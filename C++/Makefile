CC = gcc

CFLAGS = -lpthread

SRC = sum-atomic.c

TARGET = a.out

$TARGET:
	$(CC) $(SRC) $(CFLAGS) -o $(TARGET)
.PHONY: clean

clean:
	rm $(TARGET)

.PHONY: run

run:
	./$(TARGET)
