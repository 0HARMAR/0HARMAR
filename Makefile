CC=gcc


SRC=uint-overflow.c

TARGET=a.out

all:$(TARGET)

$(TARGET):$(CC) $(SRC)

clean:
	rm $(TARGET)
