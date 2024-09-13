#include <stdlib.h>
#include <stdio.h>

#include "slide_line.h"

/**
 * print_array - Prints out an array of integer, followed by a new line
 *
 * @array: Pointer to the array of integer to be printed
 * @size: Number of elements in @array
 */
static void print_array(int const* array, size_t size)
{
	size_t i;

	printf("Line: ");
	for (i = 0; i < size; i++)
		printf("%s%d", i > 0 ? ", " : "", array[i]);
	printf("\n");
}

/**
 * main - Entry point
 *
 * Return: EXIT_SUCCESS or EXIT_FAILURE
 */
int main(void)
{
	int line[] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2 };
	int direction = SLIDE_LEFT;
	size_t size = sizeof(line) / sizeof(line[0]);

	/* Print the array */
	print_array(line, size);

	/* Slide and merge */
	if (!slide_line(line, size, direction))
	{
		fprintf(stderr, "Failed to slide and merge line\n");
		return (EXIT_FAILURE);
	}

	/* Print the array */
	print_array(line, size);

	return (EXIT_SUCCESS);
}