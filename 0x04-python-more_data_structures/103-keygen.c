#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * findMax - finds maximum number
 * @username: user's name
 * @length: len of username
 * Return: Max
 */
int findMax(char *username, int length)
{
	int current;
	int max;
	unsigned int randNum;

	current = *username;
	max = 0;

	while (max < length)
	{
		if (current < username[max])
			current = username[max];
		max += 1;
	}

	srand(current ^ 14);
	randNum = rand();

	return (randNum & 63);
}

/**
 * multiplyChars - multiplies each char of username
 * @username: user's name
 * @length: len of username
 * Return: multiplied char
 */
int multiplyChars(char *username, int length)
{
	int current;
	int result;

	current = result = 0;

	while (result < length)
	{
		current = current + username[result] * username[result];
		result += 1;
	}

	return (((unsigned int)current ^ 239) & 63);
}

/**
 * generateRandomChar - generates a random char
 * @username: user's name
 * Return: a random char
 */
int generateRandomChar(char *username)
{
	int current;
	int result;

	current = result = 0;

	while (result < *username)
	{
		current = rand();
		result += 1;
	}

	return (((unsigned int)current ^ 229) & 63);
}

/**
 * main - Entry point
 * @argc: arguments count
 * @argv: arguments vector
 * Return: Always 0
 */
int main(int ac, char **av)
{
	char keygen[7];
	int length, current, result;
	long alphabet[] = {
		0x3877445248432d41, 0x42394530534e6c37, 0x4d6e706762695432,
		0x74767a5835737956, 0x2b554c59634a474f, 0x71786636576a6d34,
		0x723161513346655a, 0x6b756f494b646850 };
	(void) ac;

	for (length = 0; av[1][length]; length++)
		;
	/* ----------- findMax ----------- */
	keygen[0] = ((char *)alphabet)[(length ^ 59) & 63];
	/* ----------- multiplyChars ----------- */
	current = result = 0;
	while (result < length)
	{
		current = current + av[1][result];
		result = result + 1;
	}
	keygen[1] = ((char *)alphabet)[(current ^ 79) & 63];
	/* ----------- generateRandomChar ----------- */
	current = 1;
	result = 0;
	while (result < length)
	{
		current = av[1][result] * current;
		result = result + 1;
	}
	keygen[2] = ((char *)alphabet)[(current ^ 85) & 63];
	/* ----------- findMax ----------- */
	keygen[3] = ((char *)alphabet)[findMax(av[1], length)];
	/* ----------- multiplyChars ----------- */
	keygen[4] = ((char *)alphabet)[multiplyChars(av[1], length)];
	/* ----------- generateRandomChar ----------- */
	keygen[5] = ((char *)alphabet)[generateRandomChar(av[1])];
	keygen[6] = '\0';
	for (current = 0; keygen[current]; current++)
		printf("%c", keygen[current]);
	return (0);
}
