#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * copy_grid - Copy a 3x3 grid to another
 * @src: Source grid
 * @dest: Destination grid
 */
void copy_grid(int src[3][3], int dest[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			dest[i][j] = src[i][j];
		}
	}
}

/**
 * stabilize_grid - Check and stabilize a grid
 * @grid: 3x3 grid
 * @temp: Temporary 3x3 grid for stabilization
 *
 * Return: true if the grid was unstable, false otherwise
 */
bool stabilize_grid(int grid[3][3], int temp[3][3])
{
	int i, j;
	bool isUnstable = false;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
			{
				isUnstable = true;
				temp[i][j] -= 4;

				if (i > 0)
					temp[i - 1][j] += 1;
				if (i < 2)
					temp[i + 1][j] += 1;
				if (j > 0)
					temp[i][j - 1] += 1;
				if (j < 2)
					temp[i][j + 1] += 1;
			}
		}
	}

	return (isUnstable);
}

/**
 * make_stable - Make a grid stable if it is unstable
 * @grid: 3x3 grid
 */
void make_stable(int grid[3][3])
{
	int temp[3][3];
	bool isUnstable = true;

	while (isUnstable)
	{
		copy_grid(grid, temp);
		isUnstable = stabilize_grid(grid, temp);

		if (isUnstable)
		{
			printf("=\n");
			print_grid(grid);
			copy_grid(temp, grid);
		}
	}
}

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: 3x3 grid
 * @grid2: 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] += grid2[i][j];
		}
	}

	make_stable(grid1);
}
