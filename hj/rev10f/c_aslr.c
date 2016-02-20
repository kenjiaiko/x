#include <stdio.h>
#include <dlfcn.h>
int main(int argc, char *argv[])
{
	void *h, *f;
	if(argc < 2)
		return -1;
	h = dlopen("libc.so.6", RTLD_LAZY);
	if(h == NULL)
		return -1;
	f = (void *)dlsym(h, argv[1]);
	printf("%s:%p\n", argv[1], f);
	dlclose(h);
	return 0;
}
