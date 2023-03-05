SRC = $(wildcard source/*.cpp)
SRC += main.cpp


OUPUT_OBJ_PATH=./output
OBJ = $(patsubst %.cpp,$(OUPUT_OBJ_PATH)/%.o,$(SRC))
OUPUT_OBJ_SUB_PATH=$(sort $(dir $(OBJ)))

INCLUDE = ./include
CPPFLAGS= -I$(INCLUDE)


.PHONY: all



all:prepare $(OBJ) link


prepare:
	@mkdir -p $(OUPUT_OBJ_SUB_PATH)

$(OBJ):$(OUPUT_OBJ_PATH)/%.o:%.cpp
	gcc -c $(CPPFLAGS) $< -o $@

link:$(OBJ)
	@gcc $^ -o $(OUPUT_OBJ_PATH)/main