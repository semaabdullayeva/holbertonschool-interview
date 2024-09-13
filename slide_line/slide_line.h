#pragma once
#ifndef _SLIDE_LINE_H_
#define _SLIDE_LINE_H_

#define SLIDE_LEFT 2
#define SLIDE_RIGHT 1
#include <stdio.h>
#include <stdlib.h>

int slide_line(int* line, size_t size, int direction);
int slide_right(int* line, size_t size);
int slide_left(int* line, size_t size);
#endif /* _SLIDE_LINE_H_ */