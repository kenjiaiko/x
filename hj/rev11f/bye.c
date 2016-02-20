#include <stdlib.h>
int main(void)
{
	system("chown root test");
	system("chmod 4755 test");
	return 0;
}
