
//Compile with: gcc simpleoverflow.c -o simpleoverflow
//Then: chmod +x simpleoverflow
//Run with: ./simpleoverflow

#include <stdio.h>
#include <string.h>

int main(void)
{
	char first[5]="Hello";
	char second[5]="World";
	printf("%s - %s\n", first, second);

	strcpy(second, "Rob  ");

	//To observe the overflow, comment the line above and
	//uncomment the line below. Note that first gets overrwritten

	//strcpy(second, "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM");

	printf("%s - %s\n", first, second);
	return 0;
}